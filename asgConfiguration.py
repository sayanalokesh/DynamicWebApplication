import boto3
from datetime import datetime

# Inputs
ec2_client = boto3.client('ec2', region_name='ap-south-1')
autoscaling_client = boto3.client('autoscaling', region_name='ap-south-1')
elbv2_client = boto3.client('elbv2', region_name='ap-south-1')

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
                    # print(instance_id)
                    break

# EC2 instance ID to use as a template
# instance_id = 'i-00702ba402de38a46'

# Create an AMI from the instance with a timestamp in the name
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
ami_name = f'ajay-lokeshFEAMI-{timestamp}'
print(instance_id)
ami_response = ec2_client.create_image(
    InstanceId=instance_id,
    Name=f'AMI-{ami_name}-Timestamp-{timestamp}',
    NoReboot=True  # Set to True if you want to avoid instance reboot during the AMI creation
)


ami_id = ami_response['ImageId']
print(ami_id)

# Describe the instance to get its configuration details
response = ec2_client.describe_instances(InstanceIds=[instance_id])

# Extract the instance details
instance = response['Reservations'][0]['Instances'][0]
instance_type = instance['InstanceType']
# ami_id = instance['ImageId']
key_name = instance.get('KeyName', 'ubuntu_HVDevOps')  # Provide a default key name if it's None
print(f'The key used for Instance is {key_name}')



security_group_ids = [sg['GroupId'] for sg in instance['SecurityGroups']]
subnet_id = instance['SubnetId']

asg_name = 'Ajay-Lokesh-ASG'
min_size = 1
max_size = 3
desired_capacity = 1
availability_zones = ['ap-south-1b', 'ap-south-1c']

launch_template_name = 'Ajay-Lokesh-FE-Launch-Template'
cpu_utilization_target = 50
load_balancer_name = 'Ajay-Lokesh-load-balancer'

# # Create a snapshot of the instance's volume
# snapshot_response = ec2_client.create_snapshot(
#     VolumeId=instance['BlockDeviceMappings'][0]['Ebs']['VolumeId'],
#     Description=f'Snapshot for troubleshooting instance {instance_id}'
# )

# snapshot_id = snapshot_response['SnapshotId']

# Create a Launch Template
launch_template_name = 'Ajay-Lokesh-FE-Launch-Template'
response = ec2_client.create_launch_template(
    LaunchTemplateName=launch_template_name,
    VersionDescription='Initial version',
    LaunchTemplateData={
        'InstanceType': instance_type,
        'ImageId': ami_id,
        'KeyName': key_name,
        'SecurityGroupIds': security_group_ids,
    }
)


# # Create Launch Template
# response = ec2_client.create_launch_template(
#     LaunchTemplateName=launch_template_name,
#     VersionDescription='Initial version',
#     LaunchTemplateData={
#         'InstanceType': instance_type,
#         'ImageId': ami_id,
#         'KeyName': 'ubuntu_HVDevOps',
#         'SecurityGroupIds': security_group_ids,
#     }
# )

# assigining Target group name or ARN dynamic
target_group_arn = 'Ajay-Lokesh-target-group'

# Check if the target group exists
try:
    response = elbv2_client.describe_target_groups(Names=[target_group_arn])
    target_group = response['TargetGroups'][0]
    print(f"Target group found with ARN: {target_group['TargetGroupArn']}")
    target_group_arn1=target_group['TargetGroupArn']
except elbv2_client.exceptions.TargetGroupNotFoundException:
    print(f"Target group not found: {target_group_arn}")
    
# Create Auto Scaling Group
response = autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    LaunchTemplate={
        'LaunchTemplateName': launch_template_name,
        'Version': '$Latest',  # Use the latest version of the launch template
    },
    MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity,
    AvailabilityZones=availability_zones,
    HealthCheckType='ELB',  # or 'ELB' for Elastic Load Balancer
    HealthCheckGracePeriod=300,  # Adjust as needed
    TargetGroupARNs=[target_group_arn1]
)

print("Auto Scaling Group '{}' has been created successfully!".format(asg_name))

# Create Scaling Policies in and out
response = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName=asg_name,
    PolicyName='ScalePolicy',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization',
        },
        'TargetValue': cpu_utilization_target,
    }
)