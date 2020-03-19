from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import yaml
from yaml import load, dump
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb", region_name='us-east-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')


types="manager"
emp_id="1"

try:
    response = table.get_item(
        Key={
            'types': types,
            'emp_id': emp_id
            
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']#Python Dictionary
    print("GetItem succeeded:")
    print(item)