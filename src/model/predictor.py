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

    def __call__(self, *args, **kwargs):
        return self.predict()

    def predict(self):
        logger.info(f"Loading model from {self.load_from}")
        with open(to_absolute_path(self.load_from), "rb") as f:
            model = pickle.load(f)
        X, _ = self.dataloader.read_data(self.data)
        logger.info(f'Predicting')
        predictions = model.predict(X)
        out_fullpath = os.path.join(self.save_predictions_to['dir'], self.save_predictions_to['filename'])
        logger.info(f'Saving predictions to {out_fullpath}')
        os.makedirs(self.save_predictions_to['dir'], exist_ok=True)
        pd.DataFrame(predictions).to_csv(out_fullpath)
