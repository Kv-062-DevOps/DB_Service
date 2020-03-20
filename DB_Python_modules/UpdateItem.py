from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
#class DecimalEncoder(json.JSONEncoder):
#    def default(self, o):
#        if isinstance(o, decimal.Decimal):
#            if o % 1 > 0:
#                return float(o)
#            else:
#                return int(o)
#        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')

emp_id = str(1)
types = "manager"

response = table.update_item(
    Key={
        'emp_id': emp_id,
        'types': types
    },
    UpdateExpression="set experience=:e, default_salary=:d",
    ExpressionAttributeValues={
        ':e': str(2),
        ':d': str(2000),
        
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
#print(json.dumps(response, indent=4, cls=DecimalEncoder))
print(response)