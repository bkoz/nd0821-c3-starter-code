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
- Predict whether salary exceeds $50K/yr.

## Training Data
- 80 % of split

## Evaluation Data
- 20% of split

## Metrics

### Model Performance

|Slice |Precision  |Recall |FBeta
|--- | --- | ---| ---|
|All|1.0|0.01|0.02

Confusion Matrix
```
[
    [4925    0]
    [1567   16]
]
 ```

 #### Model performance of categorical slices.

|Slice |Precision  |Recall |FBeta
|--- | --- | ---| ---|
|sex = Male|1.0|0.012|0.023
|race = White|1.0|0.004|0.007
|workclass = Private|1.0|0.007|0.014
|education = Bachelors|1.0|0.010|0.020

```

Confusion Matricies

Slice ('sex', 'Male')

[
    [2946    0]
    [1331    0]
 ]

Slice ('race', 'White')

[
    [4177    0]
    [1458    0]
]

Slice ('workclass', 'Private')

[
    [3527    0]
    [1038    0]
]

Slice ('education', 'Bachelors')

[
    [607   0]
    [467   0]
]
 ```

## Ethical Considerations

## Caveats and Recommendations
