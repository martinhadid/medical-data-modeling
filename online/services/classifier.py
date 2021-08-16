from abc import ABC, abstractmethod

import pandas as pd


class Classifier(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def predict(self, features: pd.DataFrame):
        pass
