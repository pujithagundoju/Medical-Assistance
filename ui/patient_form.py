"""
Patient Form UI

Collects patient information required
by the trained Random Forest model.
"""

import streamlit as st


def render_patient_form():

    st.header("👤 Patient Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age (Years)",
            min_value=18,
            max_value=100,
            value=45
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        height = st.number_input(
            "Height (cm)",
            min_value=120,
            max_value=230,
            value=170
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0
        )

        systolic = st.number_input(
            "Systolic Blood Pressure",
            min_value=70,
            max_value=250,
            value=120
        )

        diastolic = st.number_input(
            "Diastolic Blood Pressure",
            min_value=40,
            max_value=180,
            value=80
        )

    with col2:

        cholesterol = st.selectbox(
            "Cholesterol Level",
            [
                "Normal",
                "Above Normal",
                "Well Above Normal"
            ]
        )

        glucose = st.selectbox(
            "Glucose Level",
            [
                "Normal",
                "Above Normal",
                "Well Above Normal"
            ]
        )

        smoking = st.selectbox(
            "Smoking",
            ["No", "Yes"]
        )

        alcohol = st.selectbox(
            "Alcohol Consumption",
            ["No", "Yes"]
        )

        physical_activity = st.selectbox(
            "Physical Activity",
            ["Yes", "No"]
        )

    patient = {

        "Age": age,

        "Gender": gender,

        "Height": height,

        "Weight": weight,

        "Systolic_BP": systolic,

        "Diastolic_BP": diastolic,

        "Cholesterol": cholesterol,

        "Glucose": glucose,

        "Smoking": smoking,

        "Alcohol": alcohol,

        "Physical_Activity": physical_activity

    }

    return patient