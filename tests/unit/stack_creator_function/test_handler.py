import json

import pytest

from unittest.mock import patch, mock_open
from stack_creator_function import main


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        'version': '2.0', 'routeKey': '$default', 'rawPath': '/', 'rawQueryString': '', 'headers': {'x-amz-content-sha256': 'ea312c639462d02a46868ff7efdf45ecc7a54329af34bc5638f005c984696774', 'content-length': '197', 'x-amz-date': '20220608T091028Z', 'x-forwarded-proto': 'https', 'x-forwarded-port': '443', 'x-forwarded-for': '176.120.127.150', 'accept': '*/*', 'x-amzn-trace-id': 'Root=1-62a06784-79cc801b222c1cca16a7823f', 'host': 'q5krik222hjfsjuawxbdxu2l3y0kzlck.lambda-url.eu-central-1.on.aws', 'content-type': 'application/json', 'accept-encoding': 'gzip, deflate', 'user-agent': 'python-requests/2.26.0'}, 'requestContext': {'accountId': '626122381776', 'apiId': 'q5krik222hjfsjuawxbdxu2l3y0kzlck', 'authorizer': {'iam': {'accessKey': 'AKIAZDR6NLHIHNXBWC5O', 'accountId': '626122381776', 'callerId': 'AIDAZDR6NLHIJYXNRWYZT', 'cognitoIdentity': None, 'principalOrgId': 'o-oyrsmm2n78', 'userArn': 'arn:aws:iam::626122381776:user/wkacz', 'userId': 'AIDAZDR6NLHIJYXNRWYZT'}}, 'domainName': 'q5krik222hjfsjuawxbdxu2l3y0kzlck.lambda-url.eu-central-1.on.aws', 'domainPrefix': 'q5krik222hjfsjuawxbdxu2l3y0kzlck', 'http': {'method': 'POST', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '176.120.127.150', 'userAgent': 'python-requests/2.26.0'}, 'requestId': '6b969129-c4df-4c3e-a303-3212b85cb9c7', 'routeKey': '$default', 'stage': '$default', 'time': '08/Jun/2022:09:10:28 +0000', 'timeEpoch': 1654679428573}, 'body': '{"action":"Create","stack_name":"wkacz-ec2-stack","launch_params":{"template_filename":"internal-stack.yaml.j2","template_params":{"bucket_name":"wkacz-ec2-bucket","ssh_key_name":"wkacz-ssh-key"}}}', 'isBase64Encoded': False

    }


def test_lambda_handler(apigw_event, mocker):

    ret = main.stream_handler(apigw_event, "")
    print(type(ret))
    print(ret)

    assert ret == 'Uninitialized'
    
