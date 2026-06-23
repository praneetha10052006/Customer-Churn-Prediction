import pandas as pd
import numpy as np

def clean_data(df):
    df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
    return df