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
        ID = str(event['Bicycle ID'])
        e = Decimal(str(event['energy']))
        p = Decimal(str(event['power']))
        r = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq(ID))
        
        power = r['Items'][0]['Power']
        power[-1].append(p)
        energy = r['Items'][0]['Energy']
        energy[-1].append(e)
        
        item = {
            'Bicycle ID': ID,
            'username': r['Items'][0]['username'],
            'password': r['Items'][0]['username'],
            'Power': power,
            'Energy': energy
        }
        
        table.put_item(Item=item)

        
        response2 = {
            "statusCode": 200,
            "body": json.dumps('Power and energy added!')
        }
        
        return response2
    # except:
    #     response2 = {
    #         "statusCode": 400,
    #         "body": json.dumps('Could not add power')
    #     }
    #     return response2