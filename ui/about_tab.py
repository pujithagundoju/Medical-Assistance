"""
About Dashboard Component

Displays project information,
technologies used, and disclaimer.
"""

import streamlit as st


# ==========================================================
# About Tab
# ==========================================================

def render_about_tab():

    st.header("ℹ️ About This Project")

    st.markdown("---")

    st.markdown(
        """
## ❤️ Explainable Cardiac Risk Assessment Assistant

This application is an AI-powered Clinical Decision Support
System (CDSS) designed to estimate the likelihood of
cardiovascular disease using Machine Learning and
Explainable Artificial Intelligence (XAI).

The system combines predictive modeling with explainability
and personalized recommendations to improve transparency
and clinical interpretability.
"""
    )

    st.markdown("---")

    st.subheader("🚀 Key Features")

    features = [

        "Random Forest Classifier",

        "Hyperparameter Tuning",

        "Cross Validation",

        "SHAP Explainability",

        "LIME Explainability",

        "Counterfactual Analysis",

        "Clinical Rule Engine",

        "Gemini AI Clinical Explanation",

        "Personalized Recommendations",

        "Interactive Dashboard",

        "PDF Report Generation"

    ]

    for feature in features:

        st.write(f"✅ {feature}")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    technologies = [

        "Python",

        "Scikit-learn",

        "Streamlit",

        "Pandas",

        "NumPy",

        "SHAP",

        "LIME",

        "Plotly",

        "Google Gemini API"

    ]

    cols = st.columns(2)

    for index, tech in enumerate(technologies):

        if index % 2 == 0:

            cols[0].write(f"• {tech}")

        else:

            cols[1].write(f"• {tech}")

    st.markdown("---")

    st.subheader("🧠 Machine Learning Model")

    st.info(
        """
Model : Random Forest Classifier

Evaluation:

• Accuracy

• Precision

• Recall

• F1 Score

• ROC-AUC

The model was selected after
hyperparameter tuning and
cross-validation.
"""
    )

    st.markdown("---")

    st.subheader("⚠ Medical Disclaimer")

    st.warning(
        """
This application is intended for educational
and research purposes only.

It is NOT a substitute for professional
medical diagnosis or treatment.

Always consult a qualified healthcare
professional for medical advice.
"""
    )

    st.markdown("---")

    st.caption(
        "Version 2.0 | Explainable AI Clinical Decision Support System"
    )