# FastAPI/Heroku MLOps Project

## Dataset: [US Census Income](https://archive.ics.uci.edu/ml/datasets/census+income)

### My Enviroment

- MacBook Pro (Intel x86_64)
- MacOS Monterey 12.4
- Python version 3.8.13 installed [mini-conda](https://github.com/conda-forge/miniforge)

### High Level File and Directory Overview
```
├── Procfile                         Heroku startup commands
├── notebooks                        EDA notebooks and example output
├── requirements.txt                 Python dependencies
├── runtime.txt                      Changes the default Heroku python version
├── starter
│   ├── data                         Data and sample payloads
│   ├── main.py                      FastAPI code
│   ├── model                        Saved model artifacts
│   ├── sample_heroku_requests.py    Heroku scripts for testing fastAPI
│   ├── screenshots                  Screen captures
│   ├── setup.py
│   └── starter                      Python scripts to process data and build/train models
├── test_main.py                     FastAPI unit tests
└── test_train_model.py              Model training unit tests
```
### How to test my work

```
cd nd0821-c3-starter-code
```

#### Unit Tests
```
pytest --log-file=logs.txt --log-level=INFO
```
Example output
```
================================================================================== test session starts ==================================================================================
platform darwin -- Python 3.8.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/bkozdemb/src/github/bkoz/nd0821-c3-starter-code
plugins: anyio-3.6.1
collected 7 items                                                                                                                                                                       
test_main.py ...
test_train_model.py ....

=================================================================================== 7 passed in 3.81s ===================================================================================
```

#### Formatting Tests
```
flake8
```

#### Model Training
```
python starter/starter/train_model.py
```
Example output
```
INFO:root:Processed data.
INFO:root:Model trained.
INFO:root:Saved model, encoder and lb.
INFO:root:Loaded saved model.
INFO:root:Model Score: precision:  0.636.  recall:  0.327. fbeta:  0.432
INFO:root:Confusion Matrix: [[4658  292]
 [1048  510]]
INFO:root:slice: {'education': 'Bachelors'}
INFO:root:Slice {'education': 'Bachelors'}, precision: 0.840, recall: 0.380, fbeta: 0.523
INFO:root:Confusion Matrix: [[599  31]
 [266 163]]
INFO:root:slice: {'education': 'Masters'}
INFO:root:Slice {'education': 'Masters'}, precision: 0.908, recall: 0.333, fbeta: 0.488
INFO:root:Confusion Matrix: [[151   6]
 [118  59]]
INFO:root:slice: {'education': 'HS-grad'}
INFO:root:Slice {'education': 'HS-grad'}, precision: 0.610, recall: 0.284, fbeta: 0.387
INFO:root:Confusion Matrix: [[1696   62]
 [ 245   97]]
INFO:root:slice: {'education': 'Doctorate'}
INFO:root:Slice {'education': 'Doctorate'}, precision: 0.900, recall: 0.443, fbeta: 0.593
INFO:root:Confusion Matrix: [[24  3]
 [34 27]]
```

#### API Testing on Heroku
```
python starter/sample_heroku_requests.py 
```
Example output
```
INFO:root:baseurl = https://bk-census.herokuapp.com
INFO:root:GET
INFO:root:status code = 200
INFO:root:{'greeting': 'Welcome to the census ML model server.'}
INFO:root:POST
INFO:root:status code = 200
INFO:root:{'Prediction': 0}
INFO:root:POST
INFO:root:status code = 200
INFO:root:{'Prediction': 1}
```

### Steps Detail

##### Data Cleaning
I used the following `vim` command to remove the spaces after a comma.
```
:1,$s/, /,/g
```

Using pandas to clean the data.
```
data = pd.read_csv('starter/data/census-raw.csv')
data.columns = data.columns.str.replace(' ', '')
data = data.drop_duplicates()

# Strip white space
for feature in cat_features:
    data[feature] = data[feature].str.strip()
```

##### Data Processing

It is necessary to one-hot encode the request before making a prediction. 

##### Unit testing
```
pytest --log-file=logs.txt --log-level=INFO
```

###### FastAPI

How to launch from the top-level directory.
```
uvicorn starter.main:app --reload
```
