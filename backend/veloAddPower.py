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
    # try:
        table = dynamodb.Table('VeloDB')
        ID = str(event['queryStringParameters']['Bicycle ID'])
        t = str(event["queryStringParameters"]['time'])
        v = Decimal(str(event["queryStringParameters"]['value']))
        r = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq(ID))
        
        volt = r['Items'][0]['Voltage']
        volt[-1][t] = v
        
        item = {
            'Bicycle ID': ID,
            'username': r['Items'][0]['username'],
            'password': r['Items'][0]['username'],
            'Voltage': volt
        }
        
        table.put_item(Item=item)

        
        response2 = {
            "statusCode": 200,
            "body": json.dumps('Power added!')
        }
        
        return response2
    # except:
    #     response2 = {
    #         "statusCode": 400,
    #         "body": json.dumps('Could not add power')
    #     }
    #     return response2