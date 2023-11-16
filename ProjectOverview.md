## Table of Contents

1. **[Web Application Deployment](#web-application-deployment)**
    - Launching EC2 Instances with `boto3`
    - Configuring EC2 instances as Nginx web servers
    - Deploying the web application onto EC2 instances
    - Code snippets for launching instances: [boto3S3LaunchFE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3S3LaunchFE.py), [boto3S3LaunchBE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3InstanceBE.py).

2. **[Load Balancing with ELB](#load-balancing-with-elb)**
    - Deploying an Application Load Balancer (ALB) using `boto3`
    - Registering EC2 instances with the ALB
    - Code snippet for Load Balancing: [LoadBalancing.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/LoadBalancing.py)

3. **[Auto Scaling Group (ASG) Configuration](#auto-scaling-group-asg-configuration)**
    - Creating an ASG with deployed EC2 instances as templates
    - Configuring scaling policies based on metrics
    - Code snippet for ASG configuration: [asgConfiguration.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/asgConfiguration.py)

4. **[Lambda-based Health Checks & Management](#lambda-based-health-checks--management)**
    - Developing a Lambda function for health checks
    - Handling failing instances and notifications through SNS
    - Screenshots related to the code

5. **[S3 Logging & Monitoring](#s3-logging--monitoring)**
    - Content related to S3 Logging and monitoring (not provided in the given information)


    
### Web Application Deployment

During this phase, specific tasks are executed elegantly:
- Using `boto3`, I launched two EC2 instances (Frontend and Backend), configuring them as Nginx web servers. Subsequently, I deployed the web application onto these EC2 instances.
The code sequence involves instance launching, downloading Git dependencies, cloning files from the [repository](https://github.com/UnpredictablePrashant/TravelMemory.git)", navigating to TravelMemory, installing NodeJS and NPM, setting up reverse proxy, and executing the application on port 80.
Kindly refer to the codes for launching instances:
    1. [boto3S3LaunchFE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3S3LaunchFE.py)
    2. [boto3S3LaunchBE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3InstanceBE.py)

Enclosed are the relevant screenshots related to the code.

### Load Balancing with ELB

Within this phase, utilizing `boto3`, I facilitated the deployment of an Application Load Balancer (ALB) and the registration of EC2 instances with the ALB.
The primary objective of this code is to construct a Load Balancer and associate EC2 instances with the Target Group.
Refer to the [LoadBalancing.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/LoadBalancing.py) for the boto3 code snippet.

Enclosed are the relevant screenshots linked to the code.

### Auto Scaling Group (ASG) Configuration

In this phase, employing `boto3`, I created an ASG, utilizing the deployed EC2 instance as a template. Additionally, I configured scaling policies to dynamically scale in/out based on metrics such as CPU utilization or network traffic.
Refer to the [asgConfiguration.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/asgConfiguration.py) for the boto3 code snippet.

Enclosed are the relevant screenshots tied to the code.

### Lambda-based Health Checks & Management

Within this phase, I crafted a Lambda function to routinely examine the health status of the web application/Instances (Frontend) via the ALB. Should the health check consistently fail, the Lambda function captures a snapshot of the failing instance for debugging purposes. It then terminates the problematic instance, allowing the ASG to replace it. Additionally, the code sends a notification through SNS to administrators.

Refer to the [backup_lambda.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/backup_lambda.py) for the boto3 code snippet.

Enclosed are the  screenshots related to the code.

The below screenshot shows the snapshots of unhealthy Instances.
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/a813c98c-e053-40b9-9078-4706cc27f109)

The instance is getting terminated after invoking the lambda code.
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/d93a5fb9-87dd-4407-b461-e4d941f0e179)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/14ad5697-2e4f-41b3-8b6f-fa855c57aaaa)

The below screenshot shows the unhealthy state of an Instance via email.
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/0bf0a580-4c00-48fa-8e05-51a4958ce5fb)

The below screenshot shows the healthy state of an Instance via email.
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/7d5967af-d524-4f27-8d00-e04b08c41213)






### S3 Logging & Monitoring

The content for S3 Logging & Monitoring is currently not provided.
