from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='Employees',
    KeySchema=[
        {
            'AttributeName': 'types',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'emp_id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'types',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'emp_id',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)