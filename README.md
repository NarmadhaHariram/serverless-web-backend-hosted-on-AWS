# AWS Serverless web backend POC

## Overview

This project demonstrates a serverless architecture using AWS services:
- **DynamoDB** for data storage
- **SQS** for queuing messages
- **Lambda** for processing
- **SNS** for notifications
- **API Gateway** for interfacing

## Deployment

1. **Upload Lambda Code:**
   - Package the `lambda1_function.py` and `lambda2_function.py` files into `.zip` files.
   - Upload these `.zip` files to your S3 bucket.
   - Update the CloudFormation template with your S3 bucket name and object keys.

2. **Deploy CloudFormation Stack:**
   - Open the AWS Management Console.
   - Navigate to CloudFormation and create a new stack using the `template.yaml` file.
   - Provide the necessary parameters, including the email address for SNS notifications.
    1. **Save the CloudFormation Template:**
    Save the CloudFormation template as `template.yml`.

    2. **Deploy the Stack:**
    Use AWS CLI to create the stack:
    ```bash
    aws cloudformation create-stack --stack-name my-stack --template-body file://template.yml

3. **API Gateway Endpoint:**
   - After deployment, find the API endpoint in the CloudFormation Outputs section.
   - Use this endpoint to test the setup by sending HTTP POST requests.

## Testing
To test the Lambda functions locally, follow these steps:

1. **Install Dependencies:**
   - Install the required Python packages using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Tests:**
   - Use `pytest` to run the tests:
     ```bash
     pytest test_lambda_functions.py
     ```

   - Ensure you have your AWS credentials configured for the local environment.


## Cleanup

- Delete the CloudFormation stack to remove all resources.
