import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TABLE_NAME", "cloud-resume-stats")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": "visitors"},
            UpdateExpression="ADD #c :inc",
            ExpressionAttributeNames={"#c": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW"
        )
        count = int(response["Attributes"]["count"])
    except Exception as e:
        print(f"DynamoDB Error: {e}")
        count = 0

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({"count": count})
    }