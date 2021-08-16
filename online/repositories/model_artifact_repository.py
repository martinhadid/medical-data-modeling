from aws_clients import s3_resource

BUCKET = "MY-BUCKET"


def download_model(model_location: str, target_location: str):
    bucket = s3_resource.Bucket(BUCKET)
    bucket.download_file(model_location, target_location)
