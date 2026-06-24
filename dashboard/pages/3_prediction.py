import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.predictor import predict_customer

st.title("Customer Churn Prediction")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure",
    min_value=0
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0
)

if st.button("Predict"):

    customer_data = {
        "customerID": "TEST001",
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "charge_category": "Medium",
        "tenure_group": "0-1 year"
    }

    try:
        prediction, probability = predict_customer(
            customer_data
        )

        if prediction[0] == 1:
            st.error(
                f"Customer likely to churn ({probability:.2%})"
            )
        else:
            st.success(
                f"Customer likely to stay ({1-probability:.2%})"
            )

    except Exception as e:
        st.error(f"Error: {e}")