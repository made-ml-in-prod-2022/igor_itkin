import logging
import os
import pickle

from hydra.utils import to_absolute_path
from sklearn import metrics
from sklearn.pipeline import Pipeline

from src.data.dataloader import DataLoader

logger = logging.getLogger(__name__)


class Trainer:
    def __init__(self, dataloader: DataLoader, data: str, model, save_to: str, accuracy_on_train=False):
        self.dataloader = dataloader
        self.model = model
        self.save_to = save_to
        self.accuracy_on_train = accuracy_on_train
        self.data = data

    def __call__(self, *args, **kwargs):
        return self.fit()

    def fit(self):
        x, y = self.dataloader.read_data(to_absolute_path(self.data))

        pipeline = []
        for entry in self.model:
            name = list(entry.keys())[0]
            value = entry[name]
            pipeline.append((name, value))
        self.model = Pipeline(pipeline)
        logger.info(f"Fitting model {self.model.__class__.__name__}")
        self.model.fit(x, y)
        if self.save_to:
            logger.info(f"Saving model to {self.save_to}")
            self.save_to = to_absolute_path(self.save_to)
            working_dir = os.path.dirname(self.save_to)
            os.makedirs(working_dir, exist_ok=True)
            with open(self.save_to, "wb") as f:
                pickle.dump(self.model, f)

        if self.accuracy_on_train:
            y_pred = self.model.predict(x)
            logger.info("Prediction on train:")
            for metric in self.accuracy_on_train['metrics']:
                value = getattr(metrics, metric)(y, y_pred)
                logger.info(f"\t{metric}: {value}")
