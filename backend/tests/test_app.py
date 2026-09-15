import importlib
import os
import boto3
from moto import mock_aws

# Dynamically import the handler to bypass the reserved keyword 'lambda'
app = importlib.import_module("backend.lambda.app")
lambda_handler = app.lambda_handler


@mock_aws
def test_lambda_handler():
  os.environ["TABLE_NAME"] = "test-resume-stats"
  dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

  dynamodb.create_table(
      TableName="test-resume-stats",
      KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
      AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
      BillingMode="PAY_PER_REQUEST",
  )

  res = lambda_handler({}, {})
  assert res["statusCode"] == 200
  assert '{"count": 1}' in res["body"]