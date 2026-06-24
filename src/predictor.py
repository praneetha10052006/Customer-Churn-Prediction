import pandas as pd
import joblib


def predict_customer(customer_data):

    preprocessor = joblib.load(
        "models/preprocessor.pkl"
    )

    model = joblib.load(
        "models/logistic_regression.pkl"
    )

    customer_df = pd.DataFrame(
        [customer_data]
    )

    processed_data = preprocessor.transform(
        customer_df
    )

    prediction = model.predict(
        processed_data
    )

    probability = model.predict_proba(
        processed_data
    )[0][1]

    return prediction, probability