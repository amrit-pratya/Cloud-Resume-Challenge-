import importlib
import os
import boto3
from moto import mock_aws


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

  # Import inside the test function so it runs within the @mock_aws context
  app = importlib.import_module("backend.lambda.app")
  lambda_handler = app.lambda_handler

  res = lambda_handler({}, {})
  assert res["statusCode"] == 200
  assert '{"count": 1}' in res["body"]