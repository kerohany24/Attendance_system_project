import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Attendance')

def lambda_handler(event, context):
    try:
        print("Received event:", event)

        body = json.loads(event['body'])
        user_id = body.get('UserID')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing userID'})
            }

        table.put_item(Item={
            'UserID': user_id,
            'Timestamp': timestamp
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Checked in at {timestamp}'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }