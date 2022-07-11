# Model Card

## Model Details
- Author: Bob Kozdemba
- Date: July 2022
- Version: v1.0.0
- Type: SciKitLearn Random Forest Classifier
- => Details on RFC hyper params go here.
- Based on [US Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/census+income)
- License: Open Source
- Feedback: bkozdemba@gmail.com

## Intended Use
- Predict whether salary exceeds $50K/yr given a set of numeric and categorical features.

## Data
- 15 features (numeric and categorical)
- 32561 rows
- Data is one-hot encoded into 108 features.
- Training/Test split was 80/20 respectively

## Metrics

### Model Performance

Confusion Matrix (see `starter/screenshots/c_matrix.png`)

Performance of *test* split.

|Slice |Precision  |Recall |FBeta
|--- | --- | ---| ---|
|test split|0.696|0.256|0.375|

 #### Model performance of categorical slices.

Slices of the education category were performed for various values.
Example *confusion matricies* can be found in the `starter/screenshots`
directory.

#### Performance of education slices:

|Slice|Precision  |Recall |FBeta
|--- | --- | ---| ---|
|HS-Grad|0.592|0.217|0.318|
|Bachelors|0.810|0.295|0.433|
|Masters|0.877|0.284|0.429|
|Doctorate|0.944|0.254|0.400|
