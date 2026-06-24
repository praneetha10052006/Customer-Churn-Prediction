from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions
    )

    roc_auc = roc_auc_score(
        y_test,
        model.predict_proba(X_test)[:, 1]
    )

    print("Accuracy:", accuracy)
    print("\nClassification Report:")
    print(report)

    print("\nConfusion Matrix:")
    print(matrix)

    print("\nROC-AUC:", roc_auc)

    return accuracy