import boto3
import subprocess

# Initialize Boto3 clients for EC2 and ELB:
ec2_client = boto3.client('ec2', region_name='ap-south-1')
elbv2_client = boto3.client('elbv2', region_name='ap-south-1')

# Create a new ALB:
alb_response = elbv2_client.create_load_balancer(
    Name='Ajay-Lokesh-load-balancer',
    Subnets=['subnet-0ea24e054cba9cad2', 'subnet-0ea185273ead71a27', 'subnet-054d138c719f3f355'],
    SecurityGroups=['sg-072870334bab90a65'],
    Scheme='internet-facing',
)

print(f"ALB created with ARN: {alb_response['LoadBalancers'][0]['LoadBalancerArn']}")


# Create a target group:
target_group_response = elbv2_client.create_target_group(
    Name='Ajay-Lokesh-target-group',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-0c5a8881cff1146d8',
    TargetType='instance',
)

print(f"Target group created with ARN: {target_group_response['TargetGroups'][0]['TargetGroupArn']}")

# Register your existing EC2 instances with the target group:
# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Replace 'your-region' with your AWS region

# Define the instance name you want to look up
instance_name = 'ajay-lokeshFE'  # Replace with the instance name you're searching for

# Use describe_instances to retrieve information about your instances
response = ec2_client.describe_instances()

# Iterate through reservations and instances to find the instance ID
instance_id = None

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name' and tag['Value'] == instance_name and instance['State']['Name'] == 'running':
                    instance_id = instance['InstanceId']
                    break

# Check if the instance_id has been found
if instance_id:
    ec2_instance_ids = [instance_id]  # Replace with your EC2 instance IDs
    print(f"Instance ID for {instance_name} is {instance_id}")
else:
    print(f"No instance with the name {instance_name} found.")

for instance_id in ec2_instance_ids:
    elbv2_client.register_targets(
        TargetGroupArn=target_group_response['TargetGroups'][0]['TargetGroupArn'],
        Targets=[{'Id': instance_id}]
    )

    print(f"Instance {instance_id} registered with target group.")

print("ALB created, target group created, and instances registered successfully.")

# Create a listener for the ALB that listens on port 80 (HTTP):
listener_response = elbv2_client.create_listener(
    LoadBalancerArn=alb_response['LoadBalancers'][0]['LoadBalancerArn'],
    Protocol='HTTP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': target_group_response['TargetGroups'][0]['TargetGroupArn'],
        },
    ],
)

print("ALB created, target group created, instances registered, and listener with forward action added successfully.")

# Run another Python script autoscaling configuration
subprocess.run(['python', 'asgConfiguration.py'])