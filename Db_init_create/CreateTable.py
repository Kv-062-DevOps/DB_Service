from __future__ import print_function # Python 2/3 compatibility
import boto3
import os

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name=os.environ['Region'],
                          endpoint_url=os.environ['Db_url'])
table_name = 'Employees'
existing_tables= dynamodb.list_tables()['TableNames']

if table_name not in existing_tables:
    table = dynamodb.create_table(
        TableName= table_name,
        KeySchema=[
            {
                'AttributeName': 'types',
                'KeyType': 'HASH'  #Partition keygit
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

    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print("Table status:", table.table_status)