import streamlit as st

st.title("Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "80%")
    st.metric("Precision", "65%")

with col2:
    st.metric("Recall", "52%")
    st.metric("F1 Score", "58%")

st.metric("ROC-AUC", "84.24%")

st.subheader("Classification Report")

st.text("""
              precision    recall    f1-score

No               0.84      0.90      0.87
Yes              0.65      0.52      0.58

Accuracy                             0.80
Macro Avg         0.74      0.71      0.72
Weighted Avg      0.79      0.80      0.79
""")

st.subheader("Confusion Matrix")

st.image(
    "reports/confusion_matrix.png",
    caption="Confusion Matrix",
    use_container_width=True
)