from dataclasses import dataclass


@dataclass
class Trainer:
    data: str
    model: str
    model_path: str
    mode: str

    def fit(self):
        pass

    def predict(self):
        pass