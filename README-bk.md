# API project

## Census Data

### Steps

#### Data Cleaning

###### Backup the original dataset.
```
cp census.csv census-raw.csv
```

##### Data Cleaning
I used the following `vim` command to remove the spaces after a comma.
```
:1,$s/, /,/g
```
```
df.columns = df.columns.str.replace(' ', '')
```

###### TODO: Remove duplicate rows.
```
df.drop_duplicates()
```

##### Data Processing

Save test prediction as json.
```
import json
d = X_test[0].tolist()
with open("payload.json", "w") as outfile:
    json.dump(d, outfile, indent=2)
```

##### Unit testing
```
pytest --log-file=logs.txt --log-level=INFO
```

###### FastAPI

How to launch from the top-level directory.
```
uvicorn starter.main:app --reload
```

These messages seem to be related to logging within testing.
```
INFO:uvicorn.error:Started server process [72041]
INFO:     Waiting for application startup.
INFO:uvicorn.error:Waiting for application startup.
INFO:     Application startup complete.
```

Testing
```
age                               35
workclass                    Private
fnlgt                         185556
education                    Masters
education-num                     14
marital-status    Married-civ-spouse
occupation            Prof-specialty
relationship                 Husband
race                           White
sex                             Male
capital-gain                       0
capital-loss                    1887
hours-per-week                    40
native-country         United-States
salary                          >50K

curl -X 'POST' \
  'http://localhost:8000/predict3/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
```
```
{"Prediction":[1]}
```
```
curl -X 'POST' \
  'http://localhost:8000/predict3/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 46,
  "workclass": "Adm-clerical",
  "fnlgt": 18556,
  "education": "HS-grad",
  "education-num": 10,
  "marital-status": "Married-civ-spouse",
  "occupation": "Prof-speciality",
  "relationship": "Husband",
  "race": "Black",
  "sex": "Male",
  "capital-gain": 0,
  "capital-loss": 110,
  "hours-per-week": 20,
  "native-country": "United-States",
  "salary": "?"
}'
```
```
{"Prediction":[0]}
```
```
https://frank-ceballos.medium.com/deploying-your-first-fastapi-application-in-openshift-857cee7277f9
```
