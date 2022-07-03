# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
# BK
import pandas as pd
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics
import joblib
from sklearn.metrics import confusion_matrix
import logging
logging.basicConfig(level=logging.INFO)


def slice_performance(model, local_df, slice):
    """ Output the model performance on slices of just the categorical features.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    feature (dict): The feature:value to hold constant (["sex" : "female"]).

    Returns
    -------
    preds : dict
        Performance metrics based on slices.
    """

    feature = slice[0]
    value = slice[1]
    query = f'{feature} == "{value}"'
    df_copy = local_df.copy()
    df_copy = df_copy.query(query)
    logging.debug(f'slice: {query}: count(): {df_copy[feature].count()}')

    X_test, y_test, _, _ = process_data(
        df_copy, categorical_features=cat_features,
        label="salary", training=False,
        encoder=encoder, lb=lb
    )
    y_predict = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, y_predict)
    return precision, recall, fbeta


# Add code to load in the data.
# BK - Remove spaces and duplicate rows.
data = pd.read_csv('starter/data/census-raw.csv')
data.columns = data.columns.str.replace(' ', '')
data = data.drop_duplicates()

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

# Strip white space
for feature in cat_features:
    data[feature] = data[feature].str.strip()

# Optional enhancement, use K-fold cross validation
# instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

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
# BK
model = train_model(X_train, y_train)
logging.info("Model trained.")
model_dir = "starter/model"
joblib.dump(model, f'{model_dir}/model.pkl')
joblib.dump(encoder, f'{model_dir}/encoder.pkl')
logging.info("Saved model.")

#
# Make test predictions and score the model.
# BK
y_predict = inference(model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, y_predict)
logging.info(f'count(): {test.age.count()}')
logging.info(f"Model Score: precision: {precision: .3f}.\
  recall: {recall: .3f}. fbeta: {fbeta: .3f}")
c_matrix = confusion_matrix(y_test, y_predict, labels=[0, 1])
logging.info(f"Confusion Matrix: {c_matrix}")

#
# Slice performance
# BK
slices = {
            'sex': 'Male',
            'race': 'Black',
            'workclass': 'Private',
            'education': 'Bachelors'
            }
for slice in slices.items():
    logging.debug(f"slice: {slice}")
    precision, recall, fbeta = slice_performance(model, test, slice)
    logging.info(
                 f"Slice {slice}, "
                 f"precision: {precision:.3f}, "
                 f"recall: {recall:.3f}, "
                 f"fbeta: {fbeta:.3f}"
                )
