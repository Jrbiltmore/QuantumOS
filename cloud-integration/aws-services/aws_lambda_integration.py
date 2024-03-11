import boto3
import json
import base64

# AWS configuration
aws_profile = 'default'  # Your AWS profile
lambda_function_name = 'MyLambdaFunction'
lambda_handler = 'lambda_function.lambda_handler'  # File and method name
lambda_runtime = 'python3.8'
lambda_role = 'arn:aws:iam::123456789012:role/your-lambda-role'  # Update with your Lambda execution role ARN
lambda_zip_file = 'function.zip'  # Path to your zip file containing the Lambda code

# Initialize a session using Boto3
session = boto3.Session(profile_name=aws_profile)
lambda_client = session.client('lambda')

def create_lambda_function():
    """
    Create a new AWS Lambda function.
    """
    with open(lambda_zip_file, 'rb') as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName=lambda_function_name,
        Runtime=lambda_runtime,
        Role=lambda_role,
        Handler=lambda_handler,
        Code=dict(ZipFile=zipped_code),
    )

    print(f"Lambda function {lambda_function_name} created.")
    return response

def invoke_lambda_function():
    """
    Invoke the specified AWS Lambda function.
    """
    response = lambda_client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',  # Use 'Event' for asynchronous invocation
        Payload=json.dumps({'key': 'value'}),  # Payload to pass to the Lambda function
    )

    result = json.loads(response['Payload'].read())
    print(f"Lambda function invoked. Response: {result}")

def delete_lambda_function():
    """
    Delete the specified AWS Lambda function.
    """
    response = lambda_client.delete_function(
        FunctionName=lambda_function_name
    )

    print(f"Lambda function {lambda_function_name} deleted.")

if __name__ == '__main__':
    # Uncomment the functions below to create, invoke, or delete the Lambda function
    # create_lambda_function()
    # invoke_lambda_function()
    # delete_lambda_function()
