import streamlit as st

st.title("Model Performance")

st.metric("Accuracy", "Available")
st.metric("Precision", "Available")
st.metric("Recall", "Available")
st.metric("F1 Score", "Available")

st.info(
    "Connect real metrics from model evaluation."
)