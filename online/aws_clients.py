import boto3

s3_client = boto3.client("s3")
dynamo_client = boto3.client("dynamodb")
dynamo_resource = boto3.resource("dynamodb")
s3_resource = boto3.resource("s3")
