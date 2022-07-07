# Put the code for your API here.
# BK
from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()


class Value(BaseModel):
    value: int


logging.basicConfig(level=logging.INFO)
logging.info("model_server: API is up.")


# Define a GET on the specified endpoint.
@app.get("/")
async def welcome():
    logging.info("model_server: get()")
    return {"greeting": "Welcome to the census ML model server."}


@app.post("/{path}")
async def predict(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}
