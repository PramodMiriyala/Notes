"""This module will have necessary functions to work with aws
"""
import boto3

def get_client():
    """This fuction establish connection with aws using aws cli credentials

    Returns:
        EC2.Client: str "Ec2.client"
    """
    return boto3.client('ec2')

def start_ec2(instance_id: str):
    """this method starts ec2 instance 

    Args:
        instance_id (str): insatnce_id
    """
    client = get_client()
    response = client.start_instances(
    InstanceIds=[
        instance_id
    ]
    )
    state = response['StartingInstances'][0]['CurrentState']['Name']
    print(state)
def stop_ec2(instance_id: str):
    """this method stops ec2 instance 
 
    Args:
        instance_id (str): insatnce_id
    """
    client = get_client()
    response = client.stop_instances(
    InstanceIds=[
        instance_id
    ]
    )
    state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(state)

if __name__ == '__main__':
    stop_ec2('i-016a0b5ae17607811')
    