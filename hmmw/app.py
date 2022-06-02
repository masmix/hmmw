# Copyright 2019-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import boto3
import logging
import traceback
import sys
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def invoke_cloudformation():
    
    template_file_location = 'lambda/mystack.json'
    
    directory = os.getcwd()

    dir_list = os.listdir(directory)

    logger.debug("Current path: %s", dir_list)
    
    with open(template_file_location, 'r') as content_file:
        content = content_file.read()
    
    params = [
        {
            "ParameterKey" : "KeyName",
            "ParameterValue" : "keypair1"
        }
        ]
    
    client = boto3.client('cloudformation')
    response = client.create_stack(StackName='ec2-wkacz', TemplateBody=content, Parameters=params)
    for item in dir(client):
        print(item)
    return 'hello'

def handler(event, context):
    """
    Lambda handler function to be triggered by saveProduct API.
    """
    try:
        requestJson = json.loads(event["body"])
        stackId = requestJson['id']
        InstanceType = requestJson['InstanceType']
        KeyName = requestJson['KeyName']
        Description = requestJson['Description']

        logger.debug("Stack Id: %s", stackId)
        logger.debug("Product InstanceType: %s", InstanceType)
        logger.debug("Product KeyName: %s", KeyName)
        logger.debug("Description: %s", Description)

        logger.info("Saving product...")
        response = invoke_cloudformation()
        response = 'hello'
        print(json.dumps(event))
        logger.info("Success: %s", response)
        returnResp = {
            "isBase64Encoded": True,
            "statusCode": 200,
            "body": json.dumps(response)
        }
        return returnResp
    except Exception as e:
        logger.error("Unknow exception occured when saving product. %s", e)
        #traceback.print_exc()
        returnResp = {
            "isBase64Encoded": True,
            "statusCode": 500,
            "body": e
        }
        return returnResp