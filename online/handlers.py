import logging
import os

from services.prediction_service import predict

logging.getLogger().setLevel(os.getenv("LOG_LEVEL", logging.INFO))

logger = logging.getLogger(__name__)


def handle_prediction(message: dict, context):
    logger.info("Received message")

    patient_id = message.get("id")
    timestamp = message.get("timestamp")
    measurement_x = message.get("measurement_x")
    measurement_y = message.get("measurement_y")
    measurement_z = message.get("measurement_z")

    estimation = predict(
        patient_id=patient_id,
        timestamp=timestamp,
        measurement_x=measurement_x,
        measurement_y=measurement_y,
        measurement_z=measurement_z,
    )

    return {"StatusCode": 200, "body": {"estimation": estimation}}
