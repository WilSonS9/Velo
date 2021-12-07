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
        u = event['queryStringParameters']['username']
        p = event["queryStringParameters"]['password']
        # u = event['username']
        # p = event['password']
        r = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq('0'))
        uid = str(int(r['Items'][0]['maxUser']) + 1)
        
        item = {
            'Bicycle ID': uid,
            'username': u,
            'password': p,
            'Voltage': [{}]
        }
        
        table.put_item(Item=item)
        
        r['Items'][0]['maxUser'] = str(int(r['Items'][0]['maxUser']) + 1)
        
        table.put_item(Item = r['Items'][0])
        
        response2 = {
            "statusCode": 200,
            "body": json.dumps('User added!')
        }
        
        return response2
    except:
        response2 = {
            "statusCode": 400,
            "body": json.dumps('Could not add user')
        }
        return response2