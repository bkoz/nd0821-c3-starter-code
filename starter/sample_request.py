import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

baseurl = "https://bk-census.herokuapp.com"

logging.info("GET")
r = requests.get(baseurl)
logging.info(f"status code = {r.status_code}")
logging.info(r.json())

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
r = requests.post(f"{baseurl}/predict/", data=json.dumps(request_0))
logging.info(f"status code = {r.status_code}")
logging.info(r.json())

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
r = requests.post(f"{baseurl}/predict/", data=json.dumps(request_1))
logging.info(f"status code = {r.status_code}")
logging.info(r.json())
