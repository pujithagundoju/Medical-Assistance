"""
Patient Form Component

Collects all patient information
from the Streamlit interface.
"""

import streamlit as st


def render_patient_form():
    """
    Display patient input form.

    Returns
    -------
    dict
        Dictionary containing all patient inputs.
    """

    st.header("👤 Patient Information")

    st.markdown("---")

    col1, col2 = st.columns(2)

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=120,
            value=45,
            step=1
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        blood_pressure = st.number_input(
            "Blood Pressure (mmHg)",
            min_value=50,
            max_value=250,
            value=120
        )

        cholesterol = st.number_input(
            "Cholesterol Level (mg/dL)",
            min_value=50,
            max_value=500,
            value=180
        )

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=24.5,
            step=0.1
        )

        sleep = st.number_input(
            "Sleep Hours",
            min_value=0,
            max_value=24,
            value=7
        )

    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with col2:

        exercise = st.selectbox(
            "Exercise Habits",
            ["Low", "Medium", "High"]
        )

        smoking = st.selectbox(
            "Smoking",
            ["No", "Yes"]
        )

        family = st.selectbox(
            "Family Heart Disease",
            ["No", "Yes"]
        )

        diabetes = st.selectbox(
            "Diabetes",
            ["No", "Yes"]
        )

        high_bp = st.selectbox(
            "High Blood Pressure",
            ["No", "Yes"]
        )

        low_hdl = st.selectbox(
            "Low HDL Cholesterol",
            ["No", "Yes"]
        )

        high_ldl = st.selectbox(
            "High LDL Cholesterol",
            ["No", "Yes"]
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

    # =====================================================
    # LAB MEASUREMENTS
    # =====================================================

    st.markdown("---")

    st.header("🧪 Laboratory Measurements")

    col3, col4 = st.columns(2)

    with col3:

        triglycerides = st.number_input(
            "Triglyceride Level",
            min_value=0.0,
            max_value=1000.0,
            value=150.0
        )

        fasting_sugar = st.number_input(
            "Fasting Blood Sugar",
            min_value=0.0,
            max_value=500.0,
            value=100.0
        )

    with col4:

        crp = st.number_input(
            "CRP Level",
            min_value=0.0,
            max_value=100.0,
            value=2.0
        )

        homocysteine = st.number_input(
            "Homocysteine Level",
            min_value=0.0,
            max_value=100.0,
            value=10.0
        )

    patient = {

        "Age": age,

        "Gender": gender,

        "Blood Pressure": blood_pressure,

        "Cholesterol Level": cholesterol,

        "Exercise Habits": exercise,

        "Smoking": smoking,

        "Family Heart Disease": family,

        "Diabetes": diabetes,

        "BMI": bmi,

        "High Blood Pressure": high_bp,

        "Low HDL Cholesterol": low_hdl,

        "High LDL Cholesterol": high_ldl,

        "Alcohol Consumption": alcohol,

        "Stress Level": stress,

        "Sleep Hours": sleep,

        "Sugar Consumption": sugar,

        "Triglyceride Level": triglycerides,

        "Fasting Blood Sugar": fasting_sugar,

        "CRP Level": crp,

        "Homocysteine Level": homocysteine

    }

    return patient