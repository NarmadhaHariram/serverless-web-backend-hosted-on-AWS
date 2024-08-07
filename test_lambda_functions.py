import json
import boto3
from moto import mock_dynamodb2, mock_sqs, mock_sns
import lambda1_function
import lambda2_function

# Mock setup
@mock_dynamodb2
def test_lambda1():
    # Setup DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='orders',
        KeySchema=[
            {'AttributeName': 'orderID', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'orderID', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='orders')

    # Define test event
    test_event = {
        'Records': [
            {
                'body': json.dumps({'item': 'latex gloves', 'customerID': '12345'})
            }
        ]
    }

    # Invoke Lambda function
    lambda1_function.lambda_handler(test_event, None)

    # Verify the data is in DynamoDB
    response = table.get_item(Key={'orderID': '12345'})
    assert 'Item' in response
    assert response['Item']['order'] == '{"item": "latex gloves", "customerID": "12345"}'


@mock_dynamodb2
@mock_sns
def test_lambda2():
    # Setup DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='orders',
        KeySchema=[
            {'AttributeName': 'orderID', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'orderID', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
        StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_IMAGE'
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='orders')

    # Setup SNS
    sns = boto3.client('sns', region_name='us-east-1')
    topic = sns.create_topic(Name='POC-Topic')
    topic_arn = topic['TopicArn']

    # Define test event
    test_event = {
        'Records': [
            {
                'eventName': 'INSERT',
                'dynamodb': {
                    'NewImage': {
                        'orderID': {'S': '12345'},
                        'order': {'S': '{"item": "latex gloves", "customerID": "12345"}'}
                    }
                }
            }
        ]
    }

    # Invoke Lambda function
    lambda2_function.lambda_handler(test_event, None)

    # Verify the SNS publish
    response = sns.list_subscriptions()
    assert any(sub['Endpoint'] == 'test@example.com' for sub in response['Subscriptions'])
