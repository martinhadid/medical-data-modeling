from dataclasses import asdict
from datetime import datetime
from typing import List

import pandas as pd

from repositories.data.patient import Patient
from repositories.data.patient_features import PatientFeatures
from services.features_service import get_patient_features
from services.lightgbm_classifier import LightGBMClassifier

classifier = LightGBMClassifier()


def predict(patient_id: str,
            timestamp: List[datetime],
            measurement_x: List[float],
            measurement_y: List[float],
            measurement_z: List[float]) -> float:

    patient = Patient(
        patient_id=patient_id,
        timestamp=timestamp,
        measurement_x=measurement_x,
        measurement_y=measurement_y,
        measurement_z=measurement_z,
    )

    features = get_patient_features(
        measurement_x=patient.measurement_x,
        measurement_y=patient.measurement_y,
        measurement_z=patient.measurement_z,
    )

    patient_features = PatientFeatures(
        measurement_x_std=features.get("measurement_x_std"),
        measurement_x_mean=features.get("measurement_x_mean"),
        measurement_x_median=features.get("measurement_x_median"),
        measurement_y_std=features.get("measurement_y_std"),
        measurement_y_mean=features.get("measurement_y_mean"),
        measurement_y_median=features.get("measurement_y_median"),
        measurement_z_std=features.get("measurement_z_std"),
        measurement_z_mean=features.get("measurement_z_mean"),
        measurement_z_median=features.get("measurement_z_median"),
        measurement_x_lr_slope=features.get("measurement_x_lr_slope"),
        measurement_x_lr_corr=features.get("measurement_x_lr_corr"),
        measurement_y_lr_slope=features.get("measurement_y_lr_slope"),
        measurement_y_lr_corr=features.get("measurement_y_lr_corr"),
        measurement_z_lr_slope=features.get("measurement_z_lr_slope"),
        measurement_z_lr_corr=features.get("measurement_z_lr_corr"),
        measurement_x_quad_a=features.get("measurement_x_quad_a"),
        measurement_x_quad_b=features.get("measurement_x_quad_b"),
        measurement_y_quad_a=features.get("measurement_y_quad_a"),
        measurement_y_quad_b=features.get("measurement_y_quad_b"),
        measurement_z_quad_a=features.get("measurement_z_quad_a"),
        measurement_z_quad_b=features.get("measurement_z_quad_b"),
    )

    classifier.update()
    df_features = pd.DataFrame.from_dict(data=asdict(patient_features), orient="index")
    estimations = classifier.predict(df_features=df_features.transpose())
    return next(iter(estimations)).item()
