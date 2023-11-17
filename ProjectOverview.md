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

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/d4ae362c-a55c-447d-801c-fa8219f6f21c)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/ef8e6210-7334-4819-93ac-511eea7dd92c)

2 Instances have been created using the code.

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/df2dc753-4be8-45d9-801b-4a89830974fd)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/ada6872e-6d3c-4d4e-bad3-c4cc81e4062e)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/ec5afa52-7d74-4dfd-92f7-92b4fb9f616b)

The code worked fine and successfully launched the application.

### Load Balancing with ELB

Within this phase, utilizing `boto3`, I facilitated the deployment of an Application Load Balancer (ALB) and the registration of EC2 instances with the ALB.
The primary objective of this code is to construct a Load Balancer and associate EC2 instances with the Target Group, set up a listener for the ALB on port 80, and trigger another Python script (`asgConfiguration.py`) for autoscaling configuration.

Refer to the [LoadBalancing.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/LoadBalancing.py) for the boto3 code snippet.

Enclosed are the relevant screenshots linked to the code.
Load Balancer:

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/1fb8cd20-7c67-42e8-a904-4234f845810d)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/50646d48-cda6-4ca2-bdff-4dbd7c9e0f21)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/a34ea9df-f8a3-46d2-99f3-c883b2f69428)

Target Groups

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/b92720e9-767f-48b9-ade2-5e0ce3bf8a9e)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/a7b9b8e5-b5db-47bd-8eb3-56c0147e0e79)


### Auto Scaling Group (ASG) Configuration

In this phase, the code utilizes the Boto3 library to perform various tasks on AWS services. It identifies an EC2 instance named 'ajay-lokeshFE', creates an Amazon Machine Image (AMI) from it, extracts its configuration details, creates a Launch Template, and establishes an Auto Scaling Group (ASG) with scaling policies based on CPU utilization. Additionally, it assigns a Target Group and sets upscaling policies for the Auto Scaling Group to adjust capacity based on the average CPU utilization.
Refer to the [asgConfiguration.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/asgConfiguration.py) for the boto3 code snippet.

Enclosed are the relevant screenshots tied to the code.

Launch Template with the same configuration as Frontend Instance.

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/d1218a24-63fe-4e39-8760-05bdbf8661c4)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/79955e53-9237-4ee1-940c-b1c5a8a89053)

AMI

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/6cac15a9-c446-4a5c-ac3c-3c8134b52ad8)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/cd9f50b2-fd41-4fec-b290-d63745cdabc6)

Auto Scaling Group

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/797e42ea-285e-40cd-a4ff-15f6d2f0e82e)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/e0c4d83e-7d28-4f5e-8c16-0e0468ec0c11)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/578ef47f-d576-4613-9e97-079edd1e09fc)

Instance with the desired number

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/35c4838b-f60e-4266-9cee-e519f74fb5f1)


### Lambda-based Health Checks & Management

Within this phase, I crafted a Lambda function to routinely examine the health status of the web application/Instances (Frontend) via the ALB. Should the health check consistently fail, the Lambda function captures a snapshot of the failing instance for debugging purposes. It then terminates the problematic instance, allowing the ASG to replace it. Additionally, the code sends a notification through SNS to administrators. The EventBridge will check every 10 minutes.

Refer to the [backup_lambda.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/backup_lambda.py) for the boto3 code snippet.

Enclosed are the  screenshots related to the code.

A function has been created

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/3508fa03-0154-4097-a9ba-434b237dc35c)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/4eb57499-14bb-44d8-8610-aa7cbb0eb37d)

Code Source has been attached using the same code

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/e9f562dd-71f3-4ea1-8c6f-788d9b6ae253)

CloudWatch Logs

![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/e793b447-7f8c-4b5b-a9ac-548b7652e53d)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/b63f1ccf-4fd9-4a42-814f-b847f5248040)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/f1e588ef-8e52-4eff-bc6c-ea5c774960ce)
![image](https://github.com/sayanalokesh/DynamicWebApplication/assets/105637305/7d566e73-a080-4d5d-9592-e9ae6b67f69d)


The below screenshot shows the snapshots of unhealthy Instances for debugging purposes.

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
