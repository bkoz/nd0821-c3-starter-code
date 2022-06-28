# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
# BK
import pandas as pd
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics
import joblib
import sklearn
import logging
logging.basicConfig(level=logging.INFO)

# Add code to load in the data.
# BK
data = pd.read_csv('../data/census.csv') 

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Process the test data with the process_data function.
# BK
X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary", training=False,
    encoder=encoder, lb=lb
)
logging.info("Processed data.")

# Train and save a model.
model = train_model(X_train, y_train)
logging.info("Model trained.")
model_dir = "../model"
joblib.dump(model, f'{model_dir}/model.pkl')
joblib.dump(encoder, f'{model_dir}/encoder.pkl')
joblib.dump(lb, f'{model_dir}/lb.pkl')
logging.info("Saved model.")

# BK - Make test predictions and score the model.
y_predict = inference(model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, y_predict)
logging.info(f"precision: {precision: .2f}. recall: {recall: .2f}. fbeta: {fbeta: .2f}")

