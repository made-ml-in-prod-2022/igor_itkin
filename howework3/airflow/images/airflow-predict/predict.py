import os
import pickle

import click
import pandas as pd

INPUT_FILE = "features.csv"
OUTPUT_FILE = "prediction.csv"
MODEL_FILE = "model.pkl"


@click.command("predict")
@click.option("--model-dir")
@click.option("--input-dir")
@click.option("--output-dir")
def predict(model_dir: str, input_dir: str, output_dir: str):
    features = pd.read_csv(os.path.join(input_dir, INPUT_FILE))
    model_fullpath = os.path.join(model_dir, MODEL_FILE)
    with open(model_fullpath, "rb") as f:
        model = pickle.load(f)
    predictions = model.train(features)

    os.makedirs(output_dir, exist_ok=True)
    predictions.to_csv(os.path.join(output_dir, OUTPUT_FILE))


if __name__ == '__main__':
    predict()
