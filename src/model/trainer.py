from dataclasses import dataclass
import pickle

from sklearn import metrics

from src.data.dataloader import DataLoader
import logging
logger = logging.getLogger(__name__)

@dataclass
class Trainer:
    def __init__(self, dataloader: DataLoader, data: str, model, save_to: str, accuracy_on_train=False):
        self.dataloader = dataloader
        self.model = model
        self.save_to = save_to
        self.accuracy_on_train = accuracy_on_train
        self.data = data

    def fit(self):
        x, y = self.dataloader.read_data(self.data)
        logger.info(f"Fitting model {self.model.__class__.__name__}")
        self.model.fit(x, y)
        if self.save_to:
            logger.info(f"Saving model to {self.save_to}")
            with open(self.save_to, "wb") as f:
                pickle.dump(self.model, f)

        if self.accuracy_on_train:
            y_pred = self.model.predict(x, y)
            for metric in self.accuracy_on_train['metrics']:
                logger.info(metric, getattr(metrics, metric)(y, y_pred))
