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
        r2 = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq('0'))
        
        curUser = r2['Items'][0]['currentUser']
        
        if not curUser == '0':
            r = table.query(
            KeyConditionExpression=Key('Bicycle ID').eq(curUser))
            power = r['Items'][0]['Power']
            power.append([])
            energy = r['Items'][0]['Energy']
            energy.append([])
            item = {
                'Bicycle ID': curUser,
                'username': r['Items'][0]['username'],
                'password': r['Items'][0]['password'],
                'Power': power,
                'Energy': energy
            }
            table.put_item(Item=item)
            item2 = {
                'Bicycle ID': '0',
                'isLoggedIn': False,
                'currentUser': '0',
                'maxUser': r2['Items'][0]['maxUser']
            }
            table.put_item(Item=item2)
            
            response2 = {
                "statusCode": 200,
                "body": json.dumps('User logged out!')
            }
            
        else:
            response2 = {
                "statusCode": 201,
                "body": json.dumps('No user logged in!')
            }    
        
        

        
        
        return response2
    # except:
    #     response2 = {
    #         "statusCode": 400,
    #         "body": json.dumps('Could not add power')
    #     }
    #     return response2