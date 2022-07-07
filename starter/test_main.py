# test_main.py
import json
from fastapi.testclient import TestClient
from main import app
import logging

logging.basicConfig(level=logging.INFO)


client = TestClient(app)


def test_get():
    r = client.get("/")
    logging.info(r)
    assert r.json() == {'greeting': 'Welcome to the census ML model server.'}


def test_post():
    logging.info("test: Loading payload.")
    payload_file = 'starter/data/payload.json'
    f = open(payload_file)
    payload_data = json.load(f)
    logging.info(f"test: Loaded payload data = {payload_data}.")
    response = client.post("/predict/", data=json.dumps(payload_data))
    logging.info(f"test: Prediction: {response.json()}")
    print(f"test: Prediction: {response.json()}")
    assert 200, response.status_code == 200
