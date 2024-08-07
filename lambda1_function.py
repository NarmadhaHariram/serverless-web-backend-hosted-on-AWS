import boto3, uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("orders")


def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        table.put_item(Item={'orderID': str(uuid.uuid4()), 'order': payload})
