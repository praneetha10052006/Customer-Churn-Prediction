import streamlit as st

st.title("SHAP Explainability")

st.write(
    """
    SHAP (SHapley Additive exPlanations) helps explain
    which features contribute most to customer churn
    predictions.
    """
)

st.subheader("SHAP Summary Plot")

st.image(
    "reports/shap_summary.png",
    caption="Feature Importance using SHAP",
    use_container_width=True
)