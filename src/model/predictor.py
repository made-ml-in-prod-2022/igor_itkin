import os
import pickle
from dataclasses import dataclass

import pandas as pd
from hydra.utils import to_absolute_path

from src.data.dataloader import DataLoader

import logging

logger = logging.getLogger(__name__)


@dataclass
class Predictor:
    data: str
    load_from: str
    save_predictions_to: str
    dataloader: DataLoader
    model = None

    def __call__(self, *args, **kwargs):
        return self.predict()

    def predict(self):
        logger.info(f"Loading model from {self.load_from}")
        if self.model is None:
            with open(to_absolute_path(self.load_from), "rb") as f:
                self.model = pickle.load(f)
        X, _ = self.dataloader.read_data(self.data)
        logger.info("Predicting")
        predictions = self.model.predict(X)
        return predictions
