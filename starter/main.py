# Put the code for your API here.
# BK
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
from typing import Union, List
import joblib
import json
import numpy
from starter.starter.ml.data import process_data
import logging

logging.basicConfig(level=logging.INFO)
# logging.info("model_server: API is up.")

app = FastAPI()


class TaggedItem(BaseModel):
    name: str
    tags: Union[str, List[str]]
    item_id: int


class CensusRequest(BaseModel):
    """
    Define the Census request schema.
    """
    age: int = Field(default=1, gt=0)
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
    hours_per_week: int = Field(default=40, alias='hours-per-week')
    native_country: str = Field(None, alias='native-country')
    salary: str


logging.info(f"CensusRequest = {CensusRequest.schema_json(indent=2)}")

model_file = 'starter/model/model.pkl'
model = joblib.load(model_file)
encoder = joblib.load("starter/model/encoder.pkl")
lb = joblib.load("starter/model/lb.pkl")


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
async def predict3(body: CensusRequest) -> int:
    global model
    global encoder
    global lb
    columns = []
    row = []
    for feature, val in body._iter():
        columns.append(feature)
        row.append(val)

    data = []
    data.append(row)
    df_copy = pd.DataFrame(data, columns=columns)
    logging.info(f"model_server: body = {body}")
    logging.info(f"model_server: columns = {columns}")
    logging.info(f"model_server: data = {data}")

    cat_features = [
                    "workclass",
                    "education",
                    "marital_status",
                    "occupation",
                    "relationship",
                    "race",
                    "sex",
                    "native_country",
                    ]

    X_test, y_test, _, _ = process_data(
        df_copy, categorical_features=cat_features,
        label="salary", training=False,
        encoder=encoder, lb=lb
    )
    logging.info(f"model_server: X_test = {X_test}")
    r = model.predict(X_test)
    logging.info(f"model_server: prediction = {type(r)} = {r.tolist()}")
    return {"Prediction": r.tolist()}
