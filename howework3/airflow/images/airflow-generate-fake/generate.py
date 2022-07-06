import os

import click
import numpy as np
import pandas as pd

CATEGORICAL = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
FEATURES_FILE = "features.csv"


@click.command("generate")
@click.option("--data-sample")
@click.option("--out-dir")
@click.option("--number-of-samples", default=100)
@click.option("--no_probs", default=False)
def generate(data_sample: str, out_dir: str, number_of_samples: int, no_probs: bool):
    df = pd.read_csv(data_sample)
    statistics = df.describe()
    cat_features_values = dict()
    cat_features_probs = dict()
    answer = dict()
    for c in CATEGORICAL:
        keys = list(df.value_counts(c).to_dict().keys())
        values = list(df.value_counts(c, normalize=True).to_dict().values())
        cat_features_values[c] = keys
        cat_features_probs[c] = values
    for col in statistics:
        if col not in CATEGORICAL:
            if not no_probs:
                mean = statistics[col].loc['mean']
                std = statistics[col].loc['std']
                answer[col] = np.random.normal(loc=mean, scale=std, size=number_of_samples)
            else:
                answer[col] = np.random.uniform(
                    low=statistics[col]['min'], high=statistics[col]['max'], size=number_of_samples
                )
        else:
            if not no_probs:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, p=cat_features_probs[col], size=number_of_samples
                )
            else:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, size=number_of_samples
                )

    filename = os.path.abspath(os.path.join(out_dir, FEATURES_FILE))
    new_df = pd.DataFrame()
    for col in df.columns:
        new_df[col] = answer[col]
    new_df.to_csv(filename)


if __name__ == "__main__":
    generate()
