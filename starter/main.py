# Put the code for your API here.
# BK
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
import joblib
from starter.starter.ml.data import process_data
import logging

logging.basicConfig(level=logging.INFO)
logging.info("model_server: is running.")

app = FastAPI()


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


logging.debug(f"model_server: CensusRequest =\
              {CensusRequest.schema_json(indent=2)}")

logging.info("model_server: loading model, encoder and label binarizer.")
model_dir = 'starter/model'
model = joblib.load(f"{model_dir}/model.pkl")
encoder = joblib.load(f"{model_dir}/encoder.pkl")
lb = joblib.load(f"{model_dir}/lb.pkl")


# Define a GET on the specified endpoint.
@app.get("/")
async def welcome():
    logging.info("model_server: get()")
    return {"greeting": "Welcome to the census ML model server."}


@app.post("/predict/")
async def predict(body: CensusRequest) -> int:
    """
    Description: Converts the REST request body to a pandas DF,
                 preprocesses the data and makes a prediction.
    Args:
                 body: The request body.
    Returns:
                 0 if salary is <= $50K
                 1 if salary is > $50K
    """
    global model
    global encoder
    global lb

    #
    # Build out the pandas dataframe from the REST body.
    #
    columns = []
    row = []
    for feature, val in body._iter():
        columns.append(feature)
        row.append(val)

    data = []
    data.append(row)
    df_copy = pd.DataFrame(data, columns=columns)
    logging.debug(f"model_server: body = {body}")
    logging.debug(f"model_server: data = {data}")

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

    #
    # Preprocessing.
    # Build a one-hot encoded numpy array.
    #
    X_test, y_test, _, _ = process_data(
        df_copy, categorical_features=cat_features,
        label="salary", training=False,
        encoder=encoder, lb=lb
    )

    #
    # Make a prediction.
    #
    logging.debug(f"model_server: X_test = {X_test}")
    r = model.predict(X_test)
    logging.info(f"model_server: prediction = {type(r)} = {r.tolist()}")
    return {"Prediction": r.tolist()[0]}
