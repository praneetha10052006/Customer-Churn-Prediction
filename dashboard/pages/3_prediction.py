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

# Basic Information
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

# Service Information
phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

# Contract Information
contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# Charges
tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=600.0
)

if st.button("Predict Churn"):

    # Auto-generate charge_category
    if monthly < 35:
        charge_category = "Low"
    elif monthly < 70:
        charge_category = "Medium"
    else:
        charge_category = "High"

    # Auto-generate tenure_group
    if tenure <= 12:
        tenure_group = "0-1 year"
    elif tenure <= 24:
        tenure_group = "1-2 years"
    elif tenure <= 48:
        tenure_group = "2-4 years"
    else:
        tenure_group = "4+ years"

    customer_data = {
        "customerID": "TEST001",
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "charge_category": charge_category,
        "tenure_group": tenure_group
    }

    try:
        prediction, probability = predict_customer(customer_data)

        st.subheader("Prediction Result")

        ipred = prediction[0]

        if pred == "Yes":
            st.error(
                f"⚠️ Customer is likely to churn\n\nProbability: {probability:.2%}"
        )
        else:
            st.success(
                f"✅ Customer is likely to stay\n\nConfidence: {(1 - probability):.2%}"
        )

    except Exception as e:
        st.error(f"Error: {e}")