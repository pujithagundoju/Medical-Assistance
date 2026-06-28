print("RUNNING APP FROM:", __file__)
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

from preprocessing.preprocess_input import preprocess_input
from model.predictor import predict_risk

from visualizations.risk_gauge import create_gauge

from services.explanation_service import explain_prediction
from services.recommendation_service import generate_recommendations
from services.clinical_interpreter import interpret_patient
from services.counterfactual_service import generate_counterfactual

from explainability.shap_analysis import (
    get_shap_explanation,
    get_top_risk_drivers
)

st.set_page_config(
    page_title="Cardiac Risk Assessment Assistant",
    layout="wide"
)

st.title("❤️ Explainable Cardiac Risk Assessment Assistant")

st.markdown("---")

st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        120,
        40
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        50,
        250,
        120
    )

    cholesterol = st.number_input(
        "Cholesterol Level",
        50,
        500,
        180
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        0,
        24,
        7
    )

with col2:

    exercise = st.selectbox(
        "Exercise Habits",
        ["Low", "Medium", "High"]
    )

    smoking = st.selectbox(
        "Smoking",
        ["Yes", "No"]
    )

    family_history = st.selectbox(
        "Family Heart Disease",
        ["Yes", "No"]
    )

    diabetes = st.selectbox(
        "Diabetes",
        ["Yes", "No"]
    )

    high_bp = st.selectbox(
        "High Blood Pressure",
        ["Yes", "No"]
    )

    low_hdl = st.selectbox(
        "Low HDL Cholesterol",
        ["Yes", "No"]
    )

    high_ldl = st.selectbox(
        "High LDL Cholesterol",
        ["Yes", "No"]
    )

    alcohol = st.selectbox(
        "Alcohol Consumption",
        ["Low", "Medium", "High"]
    )

    stress = st.selectbox(
        "Stress Level",
        ["Low", "Medium", "High"]
    )

    sugar = st.selectbox(
        "Sugar Consumption",
        ["Low", "Medium", "High"]
    )

st.markdown("---")

st.subheader("Lab Measurements")

triglycerides = st.number_input(
    "Triglyceride Level",
    0.0,
    1000.0,
    150.0
)

fasting_sugar = st.number_input(
    "Fasting Blood Sugar",
    0.0,
    500.0,
    100.0
)

crp = st.number_input(
    "CRP Level",
    0.0,
    100.0,
    2.0
)

homocysteine = st.number_input(
    "Homocysteine Level",
    0.0,
    100.0,
    10.0
)

if st.button("Predict Cardiac Risk"):

    patient_data = {

        "Age": age,
        "Gender": gender,
        "Blood Pressure": blood_pressure,
        "Cholesterol Level": cholesterol,
        "Exercise Habits": exercise,
        "Smoking": smoking,
        "Family Heart Disease": family_history,
        "Diabetes": diabetes,
        "BMI": bmi,
        "High Blood Pressure": high_bp,
        "Low HDL Cholesterol": low_hdl,
        "High LDL Cholesterol": high_ldl,
        "Alcohol Consumption": alcohol,
        "Stress Level": stress,
        "Sleep Hours": sleep_hours,
        "Sugar Consumption": sugar,
        "Triglyceride Level": triglycerides,
        "Fasting Blood Sugar": fasting_sugar,
        "CRP Level": crp,
        "Homocysteine Level": homocysteine
    }

    try:

        # ------------------------
        # Preprocessing
        # ------------------------

        processed_data = preprocess_input(
            patient_data
        )

        # ------------------------
        # Prediction
        # ------------------------

        prediction, probability = predict_risk(
            processed_data
        )

        # ------------------------
        # Clinical Interpretation
        # ------------------------

        clinical_summary = interpret_patient(
            patient_data
        )

        # ------------------------
        # SHAP Explainability
        # ------------------------

        shap_df = get_shap_explanation(
            processed_data
        )

        top_factors = get_top_risk_drivers(
            shap_df
        )

        st.markdown("---")

        # ------------------------
        # Prediction Result
        # ------------------------

        st.subheader(
            "Prediction Result"
        )

        if prediction == 1:

            st.error(
                f"High Cardiac Risk ({probability*100:.2f}%)"
            )

        else:

            st.success(
                f"Low Cardiac Risk ({probability*100:.2f}%)"
            )

        gauge_fig = create_gauge(
            probability
        )

        st.plotly_chart(
            gauge_fig,
            use_container_width=True
        )

        # ------------------------
        # Clinical Summary
        # ------------------------

        st.subheader(
            "Clinical Summary"
        )

        for key, value in clinical_summary.items():

            st.write(
                f"**{key}:** {value}"
            )

        # ------------------------
        # Top Risk Drivers
        # ------------------------

        st.subheader(
            "Top Risk Drivers"
        )

        risk_driver_df = top_factors[
            ["Feature", "SHAP_Value"]
        ].copy()

        st.dataframe(
            risk_driver_df,
            use_container_width=True
        )

        # ------------------------
        # AI Explanation
        # ------------------------

        st.subheader(
            "AI Explanation"
        )

        explanation = explain_prediction(
            patient_data,
            probability,
            top_factors,
            clinical_summary
        )

        st.write(
            explanation
        )

        # ------------------------
        # Recommendations
        # ------------------------

        st.subheader(
            "Personalized Recommendations"
        )

        recommendations = (
            generate_recommendations(
                patient_data
            )
        )

        for recommendation in recommendations:

            st.write(
                f"• {recommendation}"
            )

        # ------------------------
        # Counterfactual Analysis
        # ------------------------

        st.subheader(
            "What-If Analysis"
        )

        counterfactual = (
            generate_counterfactual(
                patient_data
            )
        )

        improved_risk = (
            counterfactual[
                "improved_risk"
            ]
        )

        reduction = (
            probability -
            improved_risk
        ) * 100

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Current Risk",
                f"{probability*100:.1f}%"
            )

        with col2:

            st.metric(
                "Improved Risk",
                f"{improved_risk*100:.1f}%"
            )

        with col3:

            st.metric(
                "Potential Reduction",
                f"{reduction:.1f}%"
            )

        st.info(
            """
            This analysis estimates how risk may change if
            modifiable risk factors such as smoking,
            blood pressure, cholesterol,
            BMI, and exercise habits improve.
            """
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )