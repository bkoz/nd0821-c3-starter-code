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

###### TODO: Remove duplicate rows.

##### Data Processing

# If training=False the following error is reported.
```
Traceback (most recent call last):
  File "/Users/bkozdemb/src/github/bkoz/nd0821-c3-starter-code/starter/starter/train_model.py", line 32, in <module>
    X_test, y_test, encoder, lb = process_data(
  File "/Users/bkozdemb/src/github/bkoz/nd0821-c3-starter-code/starter/starter/ml/data.py", line 62, in process_data
    X_categorical = encoder.transform(X_categorical)
AttributeError: 'NoneType' object has no attribute 'transform'
(py38) bkozdemb@tango$ /Users/bkozdemb/.local/miniforge3/envs/py38/bin/python /Users/bkozdemb/src/github/bkoz/nd0821-c3-starter-code/starter/starter/train_model.py
```

