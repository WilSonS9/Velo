# AWS lambda function that returns whether or not a user is currently logged in as well as the currently logged in user

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
            KeyConditionExpression=Key('Bicycle ID').eq('0')
        )
        # if response['Items'][0]['isLoggedIn'] == '1':
        #     response2 = 'True'
        # else:
        #     response2 = 'False'
        response2 = {
          "statusCode": 200,
          "body": json.dumps((response['Items'][0]['isLoggedIn'], response['Items'][0]['currentUser']), cls=DecimalEncoder)
        }
        return response2
    except:
        response2 = {
            "statusCode": 400,
            "body": json.dumps('such wow, much except')
        }
        return response2