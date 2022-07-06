import os
import pickle

import click
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

INPUT_FILE = "train_data.csv"
TARGETS_FILE = "train_targets.csv"
MODEL_FILE = "model.pkl"


@click.command("train")
@click.option("--model-dir")
@click.option("--train-dir")
def train(model_dir: str, train_dir: str):
    features = pd.read_csv(os.path.join(train_dir, INPUT_FILE))
    targets = pd.read_csv(os.path.join(train_dir, TARGETS_FILE))

    model = RandomForestClassifier()
    model.fit(features, targets)

    os.makedirs(model_dir, exist_ok=True)
    model_fullpath = os.path.join(model_dir, MODEL_FILE)
    with open(model_fullpath, "wb") as f:
        pickle.dump(f)


if __name__ == '__main__':
    train()
