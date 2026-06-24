import streamlit as st

st.title("SHAP Explainability")

st.write("""
SHAP explanations help identify which features
have the greatest impact on customer churn predictions.
""")

st.info("""
The SHAP backend implementation is available in:

src/shap_explainer.py

Future enhancement:
Display SHAP summary plots directly inside Streamlit.
""")