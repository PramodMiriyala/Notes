"""This module will have necessary functions to work with aws
"""
import boto3

def get_client(resource = 'ec2', region_name = 'ap-south-1'):
    """This fuction establish connection with aws using aws cli credentials

    Returns:
        EC2.Client: str "Ec2.client"
    """
    return boto3.client(resource,region_name)

def list_regions():
    client = get_client()
    response = client.describe_regions(
    Filters=[],
    RegionNames=[]
    )
    regions = [region['RegionName'] for region in response['Regions']]
    return regions

def get_resource_by_tag(name, value, action):
    Instance_Ids=[]
    Region_Name =[]
    for region in list_regions():
        client = get_client(region_name = region)
        response = client.describe_instances(
        Filters=[
            {
                'Name': f"tag:{name}",
                'Values': [
                    value
                ]
            }
        ]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                id = (instance['InstanceId'])
                if action == 'start'.lower():
                    start_ec2(id)
                elif action == 'stop'.lower():
                    stop_ec2(id)

def start_ec2(Instance_Ids):
    """this method starts ec2 instance 

    Args:
        instance_id (str): insatnce_id
    """
    client = get_client('ec2')
    response = client.start_instances(
    InstanceIds=[
        Instance_Ids
    ]
    )
    state = response['StartingInstances'][0]['CurrentState']['Name']
    print(state)
def stop_ec2(Instance_Ids):
    """this method stops ec2 instance 
 
    Args:
        instance_id (str): insatnce_id
    """

    client = get_client('ec2')
    response = client.stop_instances(
    InstanceIds=[
        Instance_Ids
    ]
    )
    state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(state)

if __name__ == '__main__':
    get_resource_by_tag('ENV','DEV','stop')