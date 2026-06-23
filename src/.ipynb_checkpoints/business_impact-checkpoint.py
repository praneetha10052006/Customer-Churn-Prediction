def calculate_revenue_loss(df):
    churned = df[df["Churn"] == "Yes"]
    return churned["MonthlyCharges"].sum()