import pandas as pd
import joblib
from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Model paths
PREPROCESSOR_PATH = PROJECT_ROOT / "models" / "preprocessor.pkl"
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_regression.pkl"


# Load model and preprocessor once
try:
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(
        f"Failed to load model files.\n"
        f"Preprocessor: {PREPROCESSOR_PATH}\n"
        f"Model: {MODEL_PATH}\n"
        f"Error: {e}"
    )


def predict_customer(customer_data):
    """
    Predict customer churn.
    """

    try:
        customer_df = pd.DataFrame([customer_data])

        processed_data = preprocessor.transform(
            customer_df
        )

        prediction = model.predict(
            processed_data
        )

        probability = float(
            model.predict_proba(
                processed_data
            )[0][1]
        )

        return prediction, probability

    except Exception as e:
        raise RuntimeError(
            f"Prediction failed: {e}"
        )


# -------------------------
# TEST SECTION
# -------------------------
if __name__ == "__main__":

    sample_customer = {
        "customerID": "TEST001",
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 50.0,
        "TotalCharges": 600.0,
        "charge_category": "Medium",
        "tenure_group": "0-1 year"
    }

    print("\nRunning test prediction...\n")

    prediction, probability = predict_customer(
        sample_customer
    )

    print("Prediction:", prediction)
    print("Churn Probability:", probability)