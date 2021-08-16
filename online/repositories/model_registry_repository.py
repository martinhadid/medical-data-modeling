from dataclasses import asdict
from typing import Optional

from aws_clients import dynamo_resource
from repositories.data.model_record import ModelRecord

MODEL_REGISTRY_TABLE_NAME = "MODEL-REGISTRY"

model_registry_table = dynamo_resource.Table(MODEL_REGISTRY_TABLE_NAME)


def put_model(model: ModelRecord):
    model_registry_table.put_item(Item=asdict(model))


def remove_model(run_id: str, start_date: str):
    model_registry_table.delete_item(Key={"id": run_id, "start_date": start_date})


def fetch_latest_model() -> Optional[ModelRecord]:
    response = model_registry_table.scan()
    items = response.get("Items")
    sorted_items = sorted(items, key=lambda x: x.get("start_date"), reverse=True)
    item = next(iter(sorted_items))
    model = None

    if item is not None:
        model = ModelRecord(run_id=item.get("run_id"), start_date=item.get("start_date"))

    return model
