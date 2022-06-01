#usr/bin/bash
curl --location --request POST '127.0.0.1:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
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
}'