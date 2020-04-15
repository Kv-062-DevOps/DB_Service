from flask import Flask, Response
from flask import request, jsonify, url_for

import prometheus_client
import boto3
import yaml
import os
import time

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=os.environ['access_key'],
                          aws_secret_access_key=os.environ['secret_key'],
                          region_name=os.environ['region'])
table = dynamodb.Table('Employees')

# <PROMETHEUS>

COUNT = prometheus_client.Counter(
    'request_count', 'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status']
)

LATENCY = prometheus_client.Histogram('request_latency_seconds', 'Request latency',
                                      ['app_name', 'endpoint']
                                      )

content_type_latest = str('text/plain; version=0.0.4; charset=utf-8')


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    resp_time = time.time() - request.start_time
    LATENCY.labels('dbservice', request.path).observe(resp_time)
    return response


def record_request_data(response):
    COUNT.labels('dbservice', request.method, request.path,
                 response.status_code).inc()
    return response


def setup_metrics(app):
    app.before_request(start_timer)
    # The order here matters since we want stop_timer
    # to be executed first
    app.after_request(record_request_data)
    app.after_request(stop_timer)

# </PROMETHEUS>

app = Flask(__name__)

setup_metrics(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id
# Own code
# Return List
@app.route('/list')
def show_all_employees():
    pe = "emp_id, types, first_name, second_name, default_salary, experience "
    response = table.scan(
        ProjectionExpression=pe
    )
    return (yaml.dump(response['Items']))


@app.route('/add', methods=['POST'])
def add_employee():
    req_data = yaml.safe_load(request.data)
    #emp_id = req_data['emp_id']
    types = req_data['types']
    first_name = req_data['first_name']
    second_name = req_data['second_name']
    default_salary = req_data['default_salary']
    experience = req_data['experience']
    # get new emp_id
    pe = "emp_id"
    response = table.scan(
        ProjectionExpression=pe
    )
    emp_id = 0
    for i in response['Items']:
        if int(i['emp_id']) > emp_id:
            emp_id = int(i['emp_id'])

    emp_id += 1
    emp_id_str = str(emp_id)
    #put in DB
    table.put_item(
        Item={
            'types': types,
            'emp_id': emp_id_str,
            'first_name': first_name,
            'second_name': second_name,
            'default_salary': default_salary,
            'experience': experience,
        }
    )
    resp = jsonify(success=True)
    return resp


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=content_type_latest)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ['host_port'], debug=True)
