import boto3, json

sns = boto3.client('sns')


def lambda_handler(event, context):
    for record in event["Records"]:
        if record['eventName'] == 'INSERT':
            new_record = record['dynamodb']['NewImage']
            sns.publish(
                TargetArn='arn:aws:sns:us-east-1:<account ID>:POC-Topic',
                Message=json.dumps({'default': json.dumps(new_record)}),
                MessageStructure='json'
            )
