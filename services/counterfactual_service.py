# # services/counterfactual_service.py

# from preprocessing.preprocess_input import preprocess_input
# from model.predictor import predict_risk


# def generate_counterfactual(patient_data):

#     improved_patient = patient_data.copy()

#     # Smoking improvement

#     if improved_patient["Smoking"] == "Yes":
#         improved_patient["Smoking"] = "No"

#     # Blood Pressure improvement

#     if improved_patient["Blood Pressure"] > 130:
#         improved_patient["Blood Pressure"] = 130

#     # Cholesterol improvement

#     if improved_patient["Cholesterol Level"] > 200:
#         improved_patient["Cholesterol Level"] = 200

#     # BMI improvement

#     if improved_patient["BMI"] > 25:
#         improved_patient["BMI"] = 25

#     # Exercise improvement

#     improved_patient["Exercise Habits"] = "High"

#     processed = preprocess_input(
#         improved_patient
#     )

#     prediction, probability = predict_risk(
#         processed
#     )

#     return {
#         "improved_profile": improved_patient,
#         "improved_risk": probability
#     }
"""
Counterfactual Service

Creates an improved patient profile and predicts
how the cardiac risk changes.
"""

import copy

from preprocessing.preprocess_input import preprocess_input
from model.predictor import predict_risk


def improve_patient(patient):
    """
    Create an improved version of the patient
    by modifying only modifiable risk factors.
    """

    improved = copy.deepcopy(patient)

    # =====================================================
    # Smoking
    # =====================================================

    improved["Smoking"] = "No"

    # =====================================================
    # Exercise
    # =====================================================

    improved["Exercise Habits"] = "High"

    # =====================================================
    # Blood Pressure
    # =====================================================

    if improved["Blood Pressure"] > 120:
        improved["Blood Pressure"] = 120

    # =====================================================
    # BMI
    # =====================================================

    if improved["BMI"] > 24.9:
        improved["BMI"] = 24.5

    # =====================================================
    # LDL
    # =====================================================

    improved["High LDL Cholesterol"] = "No"

    # =====================================================
    # HDL
    # =====================================================

    improved["Low HDL Cholesterol"] = "No"

    # =====================================================
    # Alcohol
    # =====================================================

    improved["Alcohol Consumption"] = "Low"

    # =====================================================
    # Sugar
    # =====================================================

    improved["Sugar Consumption"] = "Low"

    # =====================================================
    # Stress
    # =====================================================

    improved["Stress Level"] = "Low"

    # =====================================================
    # Sleep
    # =====================================================

    if improved["Sleep Hours"] < 7:
        improved["Sleep Hours"] = 7

    # =====================================================
    # Triglycerides
    # =====================================================

    if improved["Triglyceride Level"] > 150:
        improved["Triglyceride Level"] = 140

    # =====================================================
    # Fasting Sugar
    # =====================================================

    if improved["Fasting Blood Sugar"] > 100:
        improved["Fasting Blood Sugar"] = 95

    # =====================================================
    # CRP
    # =====================================================

    if improved["CRP Level"] > 1:
        improved["CRP Level"] = 1

    # =====================================================
    # Homocysteine
    # =====================================================

    if improved["Homocysteine Level"] > 12:
        improved["Homocysteine Level"] = 10

    return improved


def generate_counterfactual(patient):
    """
    Predict improved cardiac risk using the
    trained Random Forest model.
    """

    improved_patient = improve_patient(patient)

    processed = preprocess_input(improved_patient)

    prediction, probability, risk_level = predict_risk(processed)

    return {

        "patient": improved_patient,

        "prediction": prediction,

        "risk_level": risk_level,

        "improved_risk": probability

    }