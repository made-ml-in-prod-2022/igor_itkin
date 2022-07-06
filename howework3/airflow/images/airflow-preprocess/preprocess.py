import os
import pickle

import click
import pandas as pd

INPUT_FILE = "data.csv"
OUTPUT_FILE = "data.csv"
PREPROCESSOR_FILE = "preprocessor.pkl"


@click.command("preprocess")
@click.option("--model-dir")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(models_dir: str, input_dir: str, output_dir: str):
    features = pd.read_csv(os.path.join(input_dir, INPUT_FILE))
    model_fullpath = os.path.join(models_dir, PREPROCESSOR_FILE)
    with open(model_fullpath, "rb") as f:
        preprocessor = pickle.load(f)
    features = preprocessor.transform(features)

    os.makedirs(output_dir, exist_ok=True)
    features.to_csv(os.path.join(output_dir, OUTPUT_FILE))


if __name__ == '__main__':
    preprocess()
