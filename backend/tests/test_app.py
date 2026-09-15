import os

# Set dummy AWS credentials and default region before importing boto3/app
os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["TABLE_NAME"] = "test-resume-stats"

import importlib
import boto3
from moto import mock_aws

@mock_aws
def test_lambda_handler():
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    dynamodb.create_table(
        TableName="test-resume-stats",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    app = importlib.import_module("backend.lambda.app")
    lambda_handler = app.lambda_handler

    res = lambda_handler({}, {})
    assert res["statusCode"] == 200
    assert '{"count": 1}' in res["body"]