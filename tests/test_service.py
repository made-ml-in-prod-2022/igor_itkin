from fastapi import FastAPI
from fastapi.testclient import TestClient

from service import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'service is up'}


BAD_DATA_REQUEST = {
    "age": 30,
    "sex": 1,
    "cp": "int",
    "trestbps": 10,
    "chol": 10,
    "fbs": 34,
    "restecg": 1,
    "thalach": 0,
    "exang": 1,
    "oldpeak": 54,
    "slope": 5,
    "ca": 1,
    "thal": 1,
    "condition": 0
}

BAD_RESP = {'detail': [{'loc': ['body', 'cp'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}

GOOD_DATA_REQUEST = {
    "age": 30,
    "sex": 1,
    "cp": 1,
    "trestbps": 10,
    "chol": 10,
    "fbs": 34,
    "restecg": 1,
    "thalach": 0,
    "exang": 1,
    "oldpeak": 54,
    "slope": 5,
    "ca": 1,
    "thal": 1,
    "condition": 0
}


def test_predict_bad_request():
    response = client.post("/predict", json=BAD_DATA_REQUEST)
    assert response.status_code == 422
    assert response.json() == BAD_RESP


def test_predict_good_request():
    response = client.post("/predict", json=GOOD_DATA_REQUEST)
    assert 200 <= response.status_code < 300
    assert len(response.json()['errors']) == 0