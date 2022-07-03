import argparse
import os

import numpy as np
import pandas as pd

CATEGORICAL = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str,
                        default="C:\\Users\\igor\\PycharmProjects\\ml_in_prod\\data\\heart_cleveland_upload.csv")
    parser.add_argument("--num_samples", type=int, default=100)
    parser.add_argument("--no_probs", action="store_true")
    parser.add_argument("--output", type=str, default="generated.csv")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    df = pd.read_csv(args.data)
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
            if not args.no_probs:
                mean = statistics[col].loc['mean']
                std = statistics[col].loc['std']
                answer[col] = np.random.normal(loc=mean, scale=std, size=args.num_samples)
            else:
                answer[col] = np.random.uniform(
                    low=statistics[col]['min'], high=statistics[col]['max'], size=args.num_samples
                )
        else:
            if not args.no_probs:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, p=cat_features_probs[col], size=args.num_samples
                )
            else:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, size=args.num_samples
                )

    filename = os.path.abspath(args.output)
    new_df = pd.DataFrame()
    for col in df.columns:
        new_df[col] = answer[col]
    logger.info(f"Writing output to {filename}")
    new_df.to_csv(filename)


if __name__ == "__main__":
    main()
