REGION = eu-central-1
AWS_PROFILE = 'developer1_pulumi'
build:
	sam build 
test: 
	python -m pytest tests/ -v 
deploy:
	sam deploy
deploy_payload:
	awscurl -X POST --service apigateway --region $(REGION) -H 'Content-Type: application/json' --data '$(shell cat ec2-payload.json | jq  -c)' $(shell cat url.txt) -v --profile $(AWS_PROFILE)
