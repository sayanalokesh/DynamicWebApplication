import boto3
from datetime import datetime

# Define the ELB name and SNS topic ARN
elb_name = "arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Ajay-Lokesh-target-group/88fbd1f3ebb1a0ee"  # Replace with your ELB ARN
sns_topic_arn = "arn:aws:sns:ap-south-1:295397358094:Ajay-Lokesh-LambdaBasedHealthChecks"  # Replace with your SNS topic ARN

# Initialize the ELB and EC2 clients
elbv2_client = boto3.client('elbv2')
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Describe the target health of registered instances
    response = elbv2_client.describe_target_health(TargetGroupArn=elb_name)

    # Check if any instances are unhealthy
    # if you want to test whether the instance is healthy remove ! and comment the code from the line 51-57
    unhealthy_instances = [instance for instance in response['TargetHealthDescriptions'] if instance['TargetHealth']['State'] != 'healthy'] 

    if unhealthy_instances:
        for instance in unhealthy_instances:
            instance_id = instance['Target']['Id']

            # Retrieve information about the instance
            response = ec2_client.describe_instances(InstanceIds=[instance_id])

            # Extract the EBS volume ID attached to the instance
            volume_ids = [block_device['Ebs']['VolumeId'] for reservation in response['Reservations'] for instance in reservation['Instances'] for block_device in instance['BlockDeviceMappings']]

            if volume_ids:
                # Create snapshots for the retrieved volume IDs
                for volume_id in volume_ids:
                    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                    snapshot_name = f"FEDebug_snapshot_{volume_id}_{timestamp}"
                    snapshot = ec2_client.create_snapshot(VolumeId=volume_id, Description=f"{snapshot_name}")

                    # Build a detailed message about unhealthy instances and snapshots
                    message = f"Instance ID: {instance_id} is unhealthy.\n"
                    message += f"Snapshot ID: {snapshot['SnapshotId']} with name '{snapshot_name}' has been created for volume {volume_id}.\n"

                    # Terminate the unhealthy instance
                    ec2_client.terminate_instances(InstanceIds=[instance_id])

                    # Publish the message to the SNS topic
                    sns_client.publish(
                        TopicArn=sns_topic_arn,
                        Message=message,
                        Subject="ELB Unhealthy Instances Alert"
                    )
    # else:
    #     # Send a message indicating everything is fine
    #     sns_client.publish(
    #         TopicArn=sns_topic_arn,
    #         Message="All instances are healthy. No action required.",
    #         Subject="All Instances Healthy"
    #     )
