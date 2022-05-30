import logging

from omegaconf import OmegaConf
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline

from src.data.dataloader import DataLoader

logger = logging.getLogger(__name__)


class Validator:
    def __init__(self, dataloader: DataLoader, data: str, model, cross_validate_params: OmegaConf = None):
        self.data = data
        self.dataloader = dataloader
        self.model = model
        if cross_validate_params is None:
            cross_validate_params = {}
        else:
            cross_validate_params = OmegaConf.to_container(cross_validate_params)
        self.cross_validate_params = cross_validate_params

    def __call__(self, *args, **kwargs):
        return self.fit_predict()

    def fit_predict(self):
        X, y = self.dataloader.read_data(self.data)

        pipeline = []
        for entry in self.model:
            name = list(entry.keys())[0]
            value = entry[name]
            pipeline.append((name, value))
        self.model = Pipeline(pipeline)
        logger.info(f"Fitting model {self.model.__class__.__name__}")
        scores = cross_validate(self.model, X, y, **dict(self.cross_validate_params))
        for name, value in scores.items():
            logger.info(f"{name}: {value}")
        return scores
