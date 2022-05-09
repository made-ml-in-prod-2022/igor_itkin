from dataclasses import dataclass


@dataclass
class Predictor:
    data: str
    model_path: str

    def predict(self):
        pass