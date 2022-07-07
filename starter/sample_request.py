import requests
import json
import numpy

an_int = {"name": "bobs_data", "tags": "my_tags", "item_id": 33}

a_value = [12, 13]

r = requests.get("http://127.0.0.1:8000/")
print(r.status_code)
print(r.json())

r = requests.post("http://127.0.0.1:8000/mypath/", data=json.dumps(an_int))
print(r.status_code)
print(r.json())

r = requests.post("http://127.0.0.1:8000/predict/", data=json.dumps(an_int))
print(r.status_code)
print(r.json())

json_data_file = "starter/data/payload.json"
f = open(json_data_file)
a = json.load(f)
req = numpy.asarray(a)
req = req.reshape(1, -1)

r = requests.post("http://127.0.0.1:8000/predict2/",
                  data=json.dumps(req.tolist()))
print(r.status_code)
print(r.json())
