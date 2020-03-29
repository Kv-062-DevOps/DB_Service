from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import os


dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name=os.environ['Region'],
                          endpoint_url=os.environ['Db_url'])
dynamodb_client = boto3.client('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name=os.environ['Region'],
                          endpoint_url=os.environ['Db_url'])
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