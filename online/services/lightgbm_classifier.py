import lightgbm as lgb
import pandas as pd

from repositories.model_registry_repository import fetch_latest_model
from services.classifier import Classifier

MODEL_LOCATION = "../artifacts/model.txt"


class LightGBMClassifier(Classifier):
    model_run_id = None

    def __init__(self):
        self.model_classifier = None

    def update(self):
        latest_model = fetch_latest_model()
        latest_model_run_id = latest_model.run_id

        if self.model_run_id is None or self.model_run_id != latest_model_run_id:
            self.model_classifier = lgb.Booster(model_file=MODEL_LOCATION)
            self.model_run_id = latest_model_run_id

    def predict(self, df_features: pd.DataFrame):
        return self.model_classifier.predict(X=df_features)
