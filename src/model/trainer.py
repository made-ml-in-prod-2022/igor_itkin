from dataclasses import dataclass


@dataclass
class Trainer:
    dataloader: str
    model: str

    def fit(self):
        pass

    def predict(self):
        pass

    def fit_predict(self):
        pass
