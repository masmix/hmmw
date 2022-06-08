# hmmw

This project contains source code and supporting files for a serverless application.

> Based on codebase from the project https://github.com/MichalLeszczynski/task-two

# Functionalities

- create ec2 instance from jinja predefined cloudformation template
- API which accept requests with ec2 machine parameters
- upload changes to DynamoDb

## Prereqisities - tools

1. Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) 
2. [Create specific user with restricted permissons (optional)](Permissions-accounts-set-up/README.md) 
3. [Python 3 with venv installed](https://www.python.org/downloads/)

### Virtual local environment setup

```bash
cd hmmw
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r stack_creator_function/requirements.txt
```

# Deploy lambda functions stack

```bash
make deploy
```

# Unit and integration tests

```bash
make test
```

# Create ec2 instance

```bash
make deploy_payload
```

# Ssh login into ec2 instance

# Destroy ec2 instance

```bash
make delete_payload
```

## Destroy lambda functions stack

```bash
make destroy
```