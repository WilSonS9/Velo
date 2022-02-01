# AWS lambda function to fetch the latest array of voltages

import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Key

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
        response = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq(event['BicycleID'])
        )
        response2 = {
          "statusCode": 200,
          "body": json.dumps(response['Items'][0]['Power'][-1], cls=DecimalEncoder)
        }
        return response2
    except:
        response2 = {
            "statusCode": 400,
            "body": json.dumps(event)
        }
        return response2