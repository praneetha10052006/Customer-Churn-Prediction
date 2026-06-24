import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def train_models(X_train, y_train):

    logistic_model = LogisticRegression(max_iter=1000)

    random_forest = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    xgb_model = XGBClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )

    logistic_model.fit(X_train, y_train)
    random_forest.fit(X_train, y_train)
    xgb_model.fit(X_train, y_train)

    joblib.dump(
        logistic_model,
        "models/logistic_regression.pkl"
    )

    joblib.dump(
        random_forest,
        "models/random_forest.pkl"
    )

    joblib.dump(
        xgb_model,
        "models/xgboost_tuned.pkl"
    )

    return logistic_model, random_forest, xgb_model