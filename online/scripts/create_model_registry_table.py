from aws_clients import dynamo_client, dynamo_resource

MODEL_REGISTRY_TABLE_NAME = "MODEL-REGISTRY"


def create_model_registry_table():
    dynamo_client.create_table(
        TableName="MODEL-REGISTRY",
        AttributeDefinitions=[
            {"AttributeName": "run_id", "AttributeType": "S"},
            {"AttributeName": "start_date", "AttributeType": "S"},
        ],
        KeySchema=[
            {"AttributeName": "run_id", "KeyType": "HASH"},  # partition key
            {"AttributeName": "start_date", "KeyType": "RANGE"},  # sort key
        ],
        BillingMode="PAY_PER_REQUEST",
    )


def delete_model_registry_table():
    model_registry_table = dynamo_resource.Table(MODEL_REGISTRY_TABLE_NAME)
    model_registry_table.delete()


if __name__ == "__main__":
    delete_model_registry_table()
    create_model_registry_table()
