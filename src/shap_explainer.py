import shap
import matplotlib.pyplot as plt


def explain_model(
    model,
    X_sample
):

    explainer = shap.Explainer(
        model,
        X_sample
    )

    shap_values = explainer(
        X_sample
    )

    shap.summary_plot(
        shap_values,
        X_sample
    )

    plt.show()