import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("""
Welcome to the **Customer Churn Prediction System**.

This dashboard predicts whether a telecom customer is likely to churn using Machine Learning.
It also provides business insights, model explainability and performance evaluation.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Project Objective")

    st.write("""
- Predict customer churn using Machine Learning
- Help telecom companies identify high-risk customers
- Improve customer retention strategies
- Reduce revenue loss
""")

with col2:
    st.subheader("🛠 Technologies Used")

    st.write("""
- Python
- Streamlit
- Scikit-Learn
- XGBoost
- SHAP Explainability
- Pandas
- NumPy
- Matplotlib
""")

st.divider()

st.header("📁 Dashboard Modules")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
### 📈 Business Overview

Explore customer demographics,
service usage,
and churn distribution.
""")

with c2:
    st.success("""
### 📊 EDA Dashboard

Visualize important charts,
correlation heatmaps,
and customer trends.
""")

with c3:
    st.warning("""
### 🔍 Prediction

Predict whether a customer
will churn using
our trained ML model.
""")

c4, c5 = st.columns(2)

with c4:
    st.info("""
### 🧠 SHAP Explainability

Understand which features
influence customer churn
using SHAP values.
""")

with c5:
    st.success("""
### 📉 Model Performance

View Accuracy,
Precision,
Recall,
F1 Score,
ROC-AUC,
Confusion Matrix
and Classification Report.
""")

st.divider()

st.header("🚀 Workflow")

st.markdown("""
1️⃣ Load Customer Data

⬇️

2️⃣ Preprocess Features

⬇️

3️⃣ Train Machine Learning Model

⬇️

4️⃣ Predict Customer Churn

⬇️

5️⃣ Explain Prediction using SHAP

⬇️

6️⃣ Evaluate Model Performance
""")

st.divider()

st.success("✅ Developed as part of the Customer Churn Prediction Project.")

st.caption("Team M3 • Dashboard & Deployment")