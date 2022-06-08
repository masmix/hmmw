# hmmw

This project contains source code and supporting files for a serverless application.

> Based on codebase from the project https://github.com/MichalLeszczynski/task-two

# Functionalities

- create ec2 instance from jinja predefined cloudformation template
- API which accept requests with ec2 machine parameters


## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 with venv installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

# Virtual local environment setup

```bash
cd hmmw
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r stack_creator/requirements.txt
```
# Package
```bash
make package 
```

# Deploy

```bash
make deploy
```

## Destroy 

```bash
make deploy
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
