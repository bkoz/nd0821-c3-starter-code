# Put the code for your API here.
# BK
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List
import joblib
import json
import numpy
import logging

logging.basicConfig(level=logging.INFO)
# logging.info("model_server: API is up.")

app = FastAPI()


class TaggedItem(BaseModel):
    name: str
    tags: Union[str, List[str]]
    item_id: int


model_file = 'starter/model/model.pkl'
model = joblib.load(model_file)


# Define a GET on the specified endpoint.
@app.get("/")
async def welcome():
    logging.info("model_server: get()")
    return {"greeting": "Welcome to the census ML model server."}


@app.post("/mypath/")
async def exercise_function():
    return "Hello"


@app.post("/predict/")
async def predict(body: TaggedItem) -> str:
    # logging.info(f"model_server: body = {body}")
    return body


@app.post("/predict2/")
async def predict2(body: List[List[int]]) -> str:
    logging.info(f"model_server: body = {body}")
    a = numpy.array(body)
    logging.info(f"model_server: a = {a.reshape(1, -1)}")
    a.reshape(1, -1)
    r = model.predict(a)
    logging.info(f"model_server: r = {r}")
    # return "PREDICT"
    return json.dumps(r.tolist())
