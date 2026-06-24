import streamlit as st
import pandas as pd

df = pd.read_csv("data/telco_featured.csv")

st.title("Business Overview")

st.metric("Total Customers", len(df))

if "Churn" in df.columns:
    churn_rate = (df["Churn"].value_counts(normalize=True).get("Yes",0))*100
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

st.write("Business insights generated from customer churn data.")