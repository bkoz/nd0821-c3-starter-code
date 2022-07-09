# Put the code for your API here.
# BK
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
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


class CensusRequest(BaseModel):
    age: int = 1
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(None, alias='education-num')
    marital_status: str = Field(None, alias='marital-status')
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(None, alias='capital-gain')
    capital_loss: int = Field(None, alias='capital-loss')
    hours_per_week: int = Field(40, alias='hours-per-week')
    native_country: str = Field(None, alias='native-country')
    salary: str

logging.info(f"CensusRequest = {CensusRequest.schema_json(indent=2)}")

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

@app.post("/predict3/")
async def predict3(body: CensusRequest) -> dict:
    logging.info(f"model_server: body = {body}")
    # r = model.predict(body)
    return "PREDICT3"

