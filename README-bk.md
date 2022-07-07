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
curl -v -X 'POST' 'http://127.0.0.1:8000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
[60,325971,9,7688,0,40,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
}'
```

```
https://frank-ceballos.medium.com/deploying-your-first-fastapi-application-in-openshift-857cee7277f9
```
