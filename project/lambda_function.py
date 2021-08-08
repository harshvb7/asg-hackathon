import json
import boto3
import logging
import paramiko

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

LIFECYCLE_KEY = "LifecycleHookName"
ASG_KEY = "AutoScalingGroupName"
EC2_KEY = "EC2InstanceId"


def lambda_handler(event, context):
    detail = event['detail']

    logger.debug(event)

    instance_id = detail[EC2_KEY]

    logger.debug(instance_id)

    ec2_client = boto3.client('ec2')
    asg_client = boto3.client('autoscaling')
    s3_client = boto3.client('s3')
    instances = ec2_client.describe_instances(InstanceIds=[instance_id])
    ip_address = instances['Reservations'][0]['Instances'][0]['PublicIpAddress']

    s3_client.download_file('testasgpem', 'testASGKP.pem', '/tmp/file.pem')

    key = paramiko.RSAKey.from_private_key_file("/tmp/file.pem")

    ssh_client = paramiko.SSHClient()

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host = ip_address

    print("Connecting to : " + host)

    ssh_client.connect(hostname=host, username="ubuntu", pkey=key)

    print("Connected to :" + host)

    commands = [
        "sudo apt-get update",
        "sudo apt-get install awscli --assume-yes",
        "mkdir app",
        "aws s3 sync s3://hackathonstack-myhackathonbucket61d90195-b7zzxqp481hn /home/ubuntu/app",
        "chmod +x /home/ubuntu/app/startup.sh",
        "/home/ubuntu/app/startup.sh"
    ]

    for command in commands:
        print("Executing {command} ", command)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read())
        print('\n')
        print(stderr.read())
        print('\n')

    asg_client.complete_lifecycle_action(
        LifecycleHookName=detail[LIFECYCLE_KEY],
        AutoScalingGroupName=detail[ASG_KEY],
        LifecycleActionResult='CONTINUE',
        InstanceId=instance_id
    )
    return
