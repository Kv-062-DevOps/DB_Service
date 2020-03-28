from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")
dynamodb_client = boto3.client('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")
table_name='Employees'
table = dynamodb.Table(table_name)
waiter = dynamodb_client.get_waiter('table_exists')
waiter.wait(TableName=table_name)
if (table.item_count == 0):
    with open("LoadData.json") as json_file:
        employees = json.load(json_file)
        for employee in employees:
            emp_id = employee['emp_id']
            types = employee['types']
            first_name = employee['first_name']
            second_name = employee['second_name']
            default_salary = employee['default_salary']
            experience = employee['experience']

            print("Adding employees:", types, emp_id)

            table.put_item(
                Item={
                    'types': types,
                    'emp_id': emp_id,
                    'first_name': first_name,
                    'second_name': second_name,
                    'default_salary': default_salary,
                    'experience' : experience,
                    }
            )
else:
    print ("Already loaded")