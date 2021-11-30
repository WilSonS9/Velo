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
# try:
    s = 0
    l = []
    d = []
    table = dynamodb.Table('VeloDB')
    response = table.scan()
    for item in response['Items']:
        for vDict in item['Voltage']:
            keys = list(map(lambda x: int(x)/1000, sorted(list(vDict.keys()))))
            values = list(map(int, vDict.values()))
            times = []
            for i in range(len(keys)-1):
                times.append(keys[i+1] - keys[i])
            times.append(sum(times)/len(times)) # Adds the average for the final time
            for i in range(len(keys)):
                s += values[i] * times[i]
            # s += sum(vDict.values())
    response2 = {
      "statusCode": 200,
      "body": json.dumps(s, cls=DecimalEncoder)
    }
    return response2
# except:
    response2 = {
        "statusCode": 400,
        "body": json.dumps(e)
    }
    return response2