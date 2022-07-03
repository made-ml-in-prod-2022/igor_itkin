import logging
import os

import pandas as pd
from fastapi import FastAPI, HTTPException
from hydra import initialize, compose
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf
from pydantic import BaseModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()


class DataConfig(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: int
    slope: int
    ca: int
    thal: int
    condition: int


COLUMNS_ORDER = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "condition"
]

predictor = None
config = None


def startup(cfg: DictConfig) -> None:
    global predictor
    logger.info("Working directory : {}".format(os.getcwd()))
    predictor = instantiate(cfg.mode, dataloader=cfg.dataloader)


@app.on_event("startup")
async def startup_event():
    global config
    initialize(config_path="configs", job_name="test_app")
    config = compose(config_name="config")
    logger.info(f"{OmegaConf.to_yaml(config)}")
    startup(config)


@app.get("/", status_code=200)
def root():
    return {"message": "service is up"}


@app.get("/health", status_code=200)
def health():
    logger.info("starting health service")
    logger.info(f"Loading data from: {config.mode.data}")
    try:
        data = pd.read_csv(config.mode.data)
        predictor(data)
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"{ex}")


@app.post("/predict")
async def predict(item: DataConfig):
    data = []
    for f in COLUMNS_ORDER:
        data.append(getattr(item, f))
    try:
        preds = predictor(data)
        return {"predictions": preds.tolist(), "errors": []}
    except Exception as ex:
        return {"predictions": [], "errors": f"{ex}"}
