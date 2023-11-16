import boto3
import zipfile

# File names
function_code_file = 'backup_lambda.py'
zip_file = 'backup_lambda.zip'

# Zip the Lambda function code
with zipfile.ZipFile(zip_file, 'w') as z:
    z.write(function_code_file)

# Read the zipped Lambda function code
with open(zip_file, 'rb') as file:
    lambda_code = file.read()

# Initialize the boto3 clients
lambda_client = boto3.client('lambda')
events_client = boto3.client('events')

# Define your Lambda function name and existing role ARN
function_name = 'Ajay-LokeshBoto3LambdaFuntion1'
role_arn = 'arn:aws:iam::295397358094:role/service-role/Ajay-Lokesh-LambdaBasedHealthChecks-role-a9vi6y8e'  # Replace with your existing IAM role ARN

# Create the Lambda function
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime='python3.11',
    Role=role_arn,
    Handler='backup.lambda_handler',  # Replace 'backup' with your script's filename (without the extension)
    Code={
        'ZipFile': lambda_code,
    }
)

# Create a rule to trigger the Lambda function every 10 minutes
response = events_client.put_rule(
    Name='TriggerLambdaEvery10Minutes',
    ScheduleExpression='rate(10 minutes)',
    State='ENABLED'
)

# Add permission to the rule to trigger the Lambda function
response = lambda_client.add_permission(
    FunctionName='Ajay-LokeshBoto3LambdaFuntion1',
    StatementId='AllowCloudWatchToInvokeLambda',
    Action='lambda:InvokeFunction',
    Principal='events.amazonaws.com',
    SourceArn=response['RuleArn']
)

# Connect the rule to the Lambda function
response = events_client.put_targets(
    Rule='TriggerLambdaEvery10Minutes',
    Targets=[
        {
            'Id': '1',
            'Arn': response['RuleArn'],
            'Input': '{}'
        }
    ]
)

# # Schedule the Lambda function to run every 10 minutes
# events_client.put_rule(
#     Name='ScheduledRuleAjayLokeshUnhealthyStateCheck1',
#     ScheduleExpression='rate(10 minutes)',
#     State='ENABLED'
# )

# events_client.put_targets(
#     Rule='ScheduledRuleAjayLokeshUnhealthyStateCheck1',
#     Targets=[
#         {
#             'Id': '1',
#             'Arn': response['FunctionArn']
#         }
#     ]
# )
