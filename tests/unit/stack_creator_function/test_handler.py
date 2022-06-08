import json

import pytest

from unittest.mock import patch, mock_open
from stack_creator_function import main


@pytest.fixture()
def apigw_event():
    """ Generates Dynamo DB insert record trigger event"""

    return {
        'Records': [{'eventID': 'b67a38dccfaf24818ac94f2cf51b7325', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'eu-central-1', 'dynamodb': {'ApproximateCreationDateTime': 1654679429.0, 'Keys': {'Stackname': {'S': 'wkacz-ec2-stack'}, 'Timestamp': {'S': '2022-06-08T09:10:29.012715'}}, 'NewImage': {'LaunchParams': {'M': {'template_filename': {'S': 'internal-stack.yaml.j2'}, 'template_params': {'M': {'ssh_key_name': {'S': 'wkacz-ssh-key'}, 'bucket_name': {'S': 'wkacz-ec2-bucket'}}}}}, 'Action': {'S': 'Create'}, 'Stackname': {'S': 'wkacz-ec2-stack'}, 'Timestamp': {'S': '2022-06-08T09:10:29.012715'}}, 'SequenceNumber': '100000000002062083200', 'SizeBytes': 258, 'StreamViewType': 'NEW_AND_OLD_IMAGES'}, 'eventSourceARN': 'arn:aws:dynamodb:eu-central-1:626122381776:table/wkacz-cfn-actions/stream/2022-06-08T09:08:48.408'}]

    }


def test_lambda_handler(apigw_event, mocker):

    ret = main.stream_handler(apigw_event, "")
    print(type(ret))
    print(ret)

    assert ret == 'Uninitialized'
    
