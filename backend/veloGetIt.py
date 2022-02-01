# AWS lambda function to fetch the all-time energy production for all users

import boto3
import json
from decimal import Decimal

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    try:
        table = dynamodb.Table('VeloDB')
        response = table.scan()
        s = 0
        for item in response['Items']:
            for l in item['Energy']:
                s += sum(map(lambda x: x[0], l))
        response2 = {
          "statusCode": 200,
          "body": json.dumps(s, cls=DecimalEncoder)
        }
        return response2
    except:
        response2 = {
            "statusCode": 400,
            "body": json.dumps(e)
        }
        return response2