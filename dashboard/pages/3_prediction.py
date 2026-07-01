import streamlit as st
import sys
import os

# =====================================================
# Add Project Root
# =====================================================

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.predictor import predict_customer

# =====================================================
# Page Configuration
# =====================================================

st.title("📊 Customer Churn Prediction")

st.markdown("""
Predict whether a telecom customer is likely to churn based on
their demographic, service and billing information.
""")

# =====================================================
# Basic Information
# =====================================================

st.header("👤 Basic Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

with col2:

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

# =====================================================
# Service Information
# =====================================================

st.header("📡 Service Information")

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    [
        "Yes",
        "No",
        "No phone service"
    ]
)

internet_service = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

online_security = st.selectbox(
    "Online Security",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

online_backup = st.selectbox(
    "Online Backup",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

device_protection = st.selectbox(
    "Device Protection",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

tech_support = st.selectbox(
    "Tech Support",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

# =====================================================
# Contract Information
# =====================================================

st.header("📄 Contract Information")

contract = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

paperless = st.selectbox(
    "Paperless Billing",
    [
        "Yes",
        "No"
    ]
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

# =====================================================
# Billing Information
# =====================================================

st.header("💳 Billing Information")

col1, col2 = st.columns(2)

with col1:

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

with col2:

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=600.0
    )
    
# =====================================================
# Prediction Display Format
# =====================================================

display_format = st.selectbox(
    "Prediction Display Format",
    [
        "Original",
        "Yes / No",
        "1 / 0"
    ]
)

st.divider()

# =====================================================
# Prediction Button
# =====================================================

if st.button("🔍 Predict Churn", width="stretch"):

    # Auto Generate Charge Category

    if monthly < 35:
        charge_category = "Low"
    elif monthly < 70:
        charge_category = "Medium"
    else:
        charge_category = "High"

    # Auto Generate Tenure Group

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
        # =====================================================
        # Prediction Result
        # =====================================================

        st.divider()
        st.subheader("📊 Prediction Result")

        pred = prediction[0]

        # =====================================================
        # DISPLAY FORMAT
        # =====================================================

        if display_format == "Original":

            prediction_value = pred

        elif display_format == "Yes / No":

            if pred in [1, "1", True]:
                prediction_value = "Yes"

            elif pred in [0, "0", False]:
                prediction_value = "No"

            else:
                prediction_value = pred

        elif display_format == "1 / 0":

            if pred in ["Yes", 1, "1", True]:
                prediction_value = 1

            elif pred in ["No", 0, "0", False]:
                prediction_value = 0

            else:
                prediction_value = pred
        elif display_format == "Churn / No Churn":

            if pred in [1, "1", "Yes", True]:
                display_prediction = "Churn"
            else:
                display_prediction = "No Churn"

        # =====================================================
        # Model Prediction
        # =====================================================

        st.markdown("## Model Prediction")

        st.code(str(prediction_value))

        # =====================================================
        # CHURN
        # =====================================================

        if pred in [1, "1", "Yes", True]:

            st.error("⚠️ Customer is Likely to Churn")

            st.metric(
                "Churn Probability",
                f"{probability:.2%}"
            )

            st.progress(float(probability))

            st.markdown("## 📌 Recommendation")

            st.info("""
• Contact the customer proactively.

• Offer a discount or promotional plan.

• Recommend a long-term contract.

• Improve customer support.

• Resolve customer complaints quickly.

• Provide loyalty rewards.
""")

        # =====================================================
        # NO CHURN
        # =====================================================

        elif pred in [0, "0", "No", False]:

            stay_probability = 1 - probability

            st.success("✅ Customer is Likely to Stay")

            st.metric(
                "Stay Probability",
                f"{stay_probability:.2%}"
            )

            st.progress(float(stay_probability))

            st.markdown("## 📌 Recommendation")

            st.success("""
• Continue providing excellent service.

• Reward loyal customers.

• Promote premium subscription plans.

• Offer family or bundled plans.

• Send personalized offers.

• Encourage customer referrals.
""")

        # =====================================================
        # Unexpected Output
        # =====================================================

        else:

            st.warning(
                f"Unexpected prediction returned by model: {pred}"
            )

            st.write(
                "Probability:",
                probability
            )

        # =====================================================
        # Model Details
        # =====================================================

        st.divider()

        with st.expander("📈 Model Details"):

            st.write(
                f"Raw Prediction : {pred}"
            )

            st.write(
                f"Prediction Type : {type(pred)}"
            )

            st.write(
                f"Probability : {probability:.4f}"
            )

            st.write(
                f"Charge Category : {charge_category}"
            )

            st.write(
                f"Tenure Group : {tenure_group}"
            )
            
        # =====================================================
        # Customer Summary
        # =====================================================

        st.divider()

        st.subheader("📋 Customer Summary")

        summary = {
            "Gender": gender,
            "Senior Citizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "Phone Service": phone_service,
            "Multiple Lines": multiple_lines,
            "Internet Service": internet_service,
            "Contract": contract,
            "Payment Method": payment_method,
            "Tenure (Months)": tenure,
            "Monthly Charges": f"₹{monthly:.2f}",
            "Total Charges": f"₹{total:.2f}",
            "Charge Category": charge_category,
            "Tenure Group": tenure_group,
        }

        st.table(summary)

    except Exception as e:

        st.error("❌ Prediction Failed")

        st.exception(e)