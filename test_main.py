#
# test_main.py
#
# Local testing of the fastAPI endpoints.
#
import json
from fastapi.testclient import TestClient
from starter.main import app
import logging

logging.basicConfig(level=logging.INFO)


client = TestClient(app)


def test_get():
    response = client.get("/")
    logging.info(response)
    assert 200, response.status_code == 200
    assert response.json() == {'greeting':
                               'Welcome to the census ML model server.'}


def test_post_0():
    #
    # This request should return a 0.
    #
    request_0 = {
                    "age": 21,
                    "workclass": "Private",
                    "fnlgt": 4128,
                    "education": "HS-Grad",
                    "education-num": 12,
                    "marital-status": "Single",
                    "occupation": "Prof-speciality",
                    "relationship": "Husband",
                    "race": "White",
                    "sex": "Male",
                    "capital-gain": 0,
                    "capital-loss": 17,
                    "hours-per-week": 40,
                    "native-country": "United-States",
                    "salary": ">50K"
                    }

    logging.info("POST")
    response = client.post("/predict/", data=json.dumps(request_0))
    assert 200, response.status_code == 200
    logging.info(f"status code = {response.status_code}")
    assert response.json() == {'Prediction': 0}
    logging.info(f"response = {response.json()}")


def test_post_1():
    #
    # This request should return a 0.
    #
    request_1 = {
                 "age": 35,
                 "workclass": "Private",
                 "fnlgt": 185556,
                 "education": "Masters",
                 "education-num": 14,
                 "marital-status": "Married-civ-spouse",
                 "occupation": "Prof-speciality",
                 "relationship": "Husband",
                 "race": "White",
                 "sex": "Male",
                 "capital-gain": 0,
                 "capital-loss": 1887,
                 "hours-per-week": 40,
                 "native-country": "United-States",
                 "salary": ">50K"
                 }

    logging.info("POST")
    response = client.post("/predict/", data=json.dumps(request_1))
    assert 200, response.status_code == 200
    logging.info(f"status code = {response.status_code}")
    assert response.json() == {'Prediction': 1}
    logging.info(f"response = {response.json()}")
