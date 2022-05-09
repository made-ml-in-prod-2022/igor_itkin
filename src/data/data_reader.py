from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def _categorize_column(catdata, column):
    values = catdata['values']
    return OneHotEncoder(categories=values).fit_transform(column)


@dataclass
class DataReader:
    categorical: list
    target: str

    def read_data(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path)

        for catdata in self.categorical:
            name = catdata['name']
            df[name] = OneHotEncoder(categories=catdata['values']).fit_transform(df[name])
