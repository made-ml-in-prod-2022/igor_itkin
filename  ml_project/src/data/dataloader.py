from dataclasses import dataclass

from hydra.utils import to_absolute_path
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


@dataclass
class DataLoader:
    categorical: list
    target: str

    def read_data(self, path: str) -> (pd.DataFrame, pd.Series):
        df = pd.read_csv(to_absolute_path(path))
        names2drop = []
        new_dfs = []
        for catdata in self.categorical:
            name = catdata['name']
            names2drop.append(name)
            data = df[name].values.reshape(-1, 1)
            transformed = pd.DataFrame(OneHotEncoder(categories=[catdata['values']], sparse=False).fit_transform(data))
            transformed.columns = [f"{name}_{value}" for value in catdata['values']]
            new_dfs.append(transformed)
        df = df.drop(names2drop, axis=1, errors='ignore')
        df = pd.concat((df, *new_dfs), axis=1)
        target = df[self.target] if self.target in df.columns else None
        df.drop(self.target, axis=1, inplace=True, errors='ignore')
        return df, target
