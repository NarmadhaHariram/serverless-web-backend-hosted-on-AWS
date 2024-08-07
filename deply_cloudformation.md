## Deploying Resources Using AWS CloudFormation
1. Save Your CloudFormation Template
Save the provided CloudFormation template to a file named template.yml.

2. Deploying Resources Using AWS CloudFormation
You can use the AWS Management Console or the AWS CLI to deploy your CloudFormation stack. Below are the instructions for both methods:

Using AWS CLI
Configure AWS CLI:
Ensure you have AWS CLI installed and configured. If not, you can install it and configure it using:

bash
Copy code
aws configure
Enter your AWS Access Key ID, Secret Access Key, region, and output format.

Create a CloudFormation Stack:
Run the following command to create a new stack:

bash
Copy code
aws cloudformation create-stack --stack-name my-stack --template-body file://template.yml
Replace my-stack with your desired stack name.

Update Stack (If needed):
If you need to update the stack after changes, use:

bash
Copy code
aws cloudformation update-stack --stack-name my-stack --template-body file://template.yml
Check Stack Status:
You can check the status of your stack creation or update with:

bash
Copy code
aws cloudformation describe-stacks --stack-name my-stack
Verify Resources:
Once the stack is created successfully, verify that all resources (DynamoDB table, SQS queue, Lambda functions, etc.) are created in the AWS Management Console.

Using AWS Management Console
Open CloudFormation Console:
Go to the AWS CloudFormation Console.

Create a Stack:
Click on “Create stack” and choose “With new resources (standard).”

Upload Your Template:
On the “Specify template” page, choose “Upload a template file” and upload your template.yml file.

Specify Stack Details:
Enter a stack name (e.g., my-stack) and provide any required parameters.

Configure Stack Options:
You can configure options like tags, permissions, and advanced options if needed. Click “Next.”

Review and Create:
Review your settings and click “Create stack.”

Monitor Stack Creation:
Monitor the progress of stack creation in the CloudFormation console. Ensure that all resources are created successfully.

3. Deploy Lambda Functions
Ensure that your Lambda function code is properly uploaded to S3 and referenced in the template.yml under the CodeUri property. The CloudFormation stack will handle the deployment of Lambda functions.

4. Testing the Deployment
Once the stack is deployed, test your setup:

Send a Test Request:
Use API Gateway to send a test request to the SQS queue. Go to the API Gateway console, choose your API, and use the “Test” feature to send a test payload.

Verify Lambda Execution:
Check the CloudWatch logs for your Lambda functions to verify that they are triggered correctly and that they execute as expected.

Check DynamoDB:
Verify that data is being correctly written to the DynamoDB table from the SQS-triggered Lambda function.

Verify SNS Notifications:
Check if you receive an email notification from SNS when a new record is added to DynamoDB.



# Configure AWS CLI (if not configured)
aws configure

# Create CloudFormation stack
aws cloudformation create-stack --stack-name my-stack --template-body file://template.yml

# Update CloudFormation stack (if needed)
aws cloudformation update-stack --stack-name my-stack --template-body file://template.yml

# Check stack status
aws cloudformation describe-stacks --stack-name my-stack
