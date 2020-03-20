from flask import Flask
from flask import request

import boto3
import json
import decimal
import yaml
from yaml import load, dump

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Employees')

app = Flask(__name__)

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
#Own code
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
    req_data=yaml.load(request.data)
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
    emp_id=0
    for i in response['Items']:
        if int(i['emp_id'])>emp_id:
            emp_id=int(i['emp_id'])
    
    emp_id+=1
    emp_id_str=str(emp_id)
    #put in DB
    table.put_item(
           Item={
               'types': types,
               'emp_id': emp_id_str,
               'first_name': first_name,
               'second_name': second_name,
               'default_salary': default_salary,
               'experience' : experience,
            }
    )
           

    
      
if __name__ == '__main__':
    app.run()
