import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def tune_random_forest(
    X_train,
    y_train
):

    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [5, 10]
    }

    rf = RandomForestClassifier(
        random_state=42
    )

    grid_search = GridSearchCV(
        rf,
        param_grid,
        cv=3,
        scoring="accuracy",
        n_jobs=-1
    )

    grid_search.fit(
        X_train,
        y_train
    )

    best_rf = grid_search.best_estimator_

    joblib.dump(
        best_rf,
        "models/best_random_forest.pkl"
    )

    print(
        "Best Parameters:",
        grid_search.best_params_
    )

    print(
        "Best Score:",
        grid_search.best_score_
    )

    return best_rf