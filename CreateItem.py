from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')

types = "designer"
emp_id = str(4)
first_name = "Korolenko"
second_name = "Konstantyn"
default_salary = str(2000)
experience = str(3)

response = table.put_item(
   Item={
        'types': types,
        'emp_id': emp_id,
        'first_name' : first_name,
        'second_name' : second_name,
        'default_salary': default_salary,
        'experience':experience
    }
)

print("PutItem succeeded:")
print(response)