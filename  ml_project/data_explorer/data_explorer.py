import argparse
import base64
import datetime
import logging
import os
from io import BytesIO

import pandas as pd
from matplotlib import pyplot as plt

from report_template import TEMPLATE

logging.basicConfig()
logger = logging.getLogger(__name__)

CATEGORICAL = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str)
    parser.add_argument("--output", type=str, default="report.html")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    df = pd.read_csv(args.data)
    statistics = df.describe()
    na_values = df.isna().sum(axis=0)
    na_values = pd.DataFrame(na_values).T
    na_values.index = ["#NA values"]
    cat_features_values = ""
    for c in CATEGORICAL:
        keys = list(sorted(df.value_counts(c).to_dict().keys()))
        cat_features_values += f"{c}: {keys}    "
    fig = plt.figure(figsize=(16, 8))
    ax = fig.subplots(1, 1)
    df.hist(ax=ax)
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png', dpi=400)
    encoded_image = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    template = TEMPLATE.format(date=datetime.datetime.now().strftime("%d/%m/%Y"),
                               statistics=statistics.round(2).to_html(),
                               na_values=na_values.to_html(),
                               cat_values=cat_features_values,
                               encoded_image=encoded_image)
    filename = os.path.abspath(args.output)
    logger.info(f"Writing output to {filename}")
    with open(filename, "wt") as f:
        f.write(template)


if __name__ == "__main__":
    main()
