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
    
    def userFind(user, name):
        try:
            return user['username'] == name
        except:
            return False
        
    name = event['username']
    r = list(filter(lambda user: userFind(user, name), table.scan()['Items']))
    
    r2 = table.query(
        KeyConditionExpression=Key('Bicycle ID').eq('0'))
    
    ID = r[0]

    item = {
        'Bicycle ID': '0',
        'isLoggedIn': True,
        'currentUser': ID,
        'maxUser': r2['Items'][0]['maxUser']
    }
    table.put_item(Item=item)
    
    response2 = {
        "statusCode": 200,
        "body": json.dumps('User logged in!')
    }
    
    return response2
    # except:
    #     response2 = {
    #         "statusCode": 400,
    #         "body": json.dumps('Could not add power')
    #     }
    #     return response2