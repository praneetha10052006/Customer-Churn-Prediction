import pandas as pd

def create_features(df):

    df["charge_category"] = pd.cut(
        df["MonthlyCharges"],
        bins=[0, 40, 70, 120],
        labels=["Low", "Medium", "High"]
    )

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=[
            "0-1 year",
            "1-2 years",
            "2-4 years",
            "4-6 years"
        ]
    )

    return df