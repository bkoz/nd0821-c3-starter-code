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
- % of split

## Evaluation Data
- % of split

## Metrics
Make a table here.
```
precision:  1.000.  recall:  0.010. fbeta:  0.020
```
Confusion Matrix
```
[
    [4925    0]
    [1567   16]
]
 ```

 Performance of categorical slices.
 ```
('sex', 'Male'), precision: 1.000, recall: 0.012, fbeta: 0.023
('race', 'Black'), precision: 1.000, recall: 0.000, fbeta: 0.000
('workclass', 'Private'), precision: 1.000, recall: 0.007, fbeta: 0.014
('education', 'Bachelors'), precision: 1.000, recall: 0.010, fbeta: 0.020
```


## Ethical Considerations

## Caveats and Recommendations
