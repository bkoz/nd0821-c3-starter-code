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
    data = json.dumps({"value": 10})
    r = client.post("/42?query=5", data=data)
    print(r.json())
    assert r.json()["path"] == 42
    assert r.json()["query"] == 5
    assert r.json()["body"] == {"value": 10}