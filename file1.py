import boto3, os, json
from botocore.exceptions import ClientError
from datetime import datetime, timezone, timedelta

def create_launch_template_with_new_ami_id(image_id_input):
    response = ec2.create_launch_template_version(
    LaunchTemplateId="lt-0c1406dfc25823518",
    SourceVersion="$Default",
    VersionDescription="Latest-AMI",
    LaunchTemplateData={
    "ImageId": image_id_input
                }
    )
def modifying_launch_temp_version():
    response = ec2.modify_launch_template(
        LaunchTemplateId="lt-0c1406dfc25823518",
        DefaultVersion="$Default"
    )
def updating_auto_scaling_group():
    response1 = asg.update_auto_scaling_group(
        AutoScalingGroupName='MY-ASG',
        LaunchTemplate={
            'LaunchTemplateId': 'lt-0c1406dfc25823518',
            'Version': '$Latest'
        }
        )
# Taking1 ami id as input #
image_id_input=input("Input AMI ID :   ")
ec2=boto3.client('ec2')
asg=boto3.client("autoscaling")
data=ec2.describe_launch_template_versions(LaunchTemplateId='lt-0c1406dfc25823518')
x=data["LaunchTemplateVersions"][0]["LaunchTemplateData"]["ImageId"]
print(x)
if(x!="image_id_input"):
    # ---- caliing function to create launch template with ami id -----
    create_launch_template_with_new_ami_id(image_id_input)
    # ---- calling function to modify temp version ----
    modifying_launch_temp_version()
    # ---- updating auto scaling group ----
    updating_auto_scaling_group()

