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
    Improve only the modifiable risk factors.
    """

    improved = copy.deepcopy(patient)

    # ---------------------------------------
    # Smoking
    # ---------------------------------------

    improved["Smoking"] = "No"

    # ---------------------------------------
    # Alcohol
    # ---------------------------------------

    improved["Alcohol"] = "No"

    # ---------------------------------------
    # Physical Activity
    # ---------------------------------------

    improved["Physical_Activity"] = "Yes"

    # ---------------------------------------
    # Blood Pressure
    # ---------------------------------------

    if improved["Systolic_BP"] > 120:
        improved["Systolic_BP"] = 120

    if improved["Diastolic_BP"] > 80:
        improved["Diastolic_BP"] = 80

    # ---------------------------------------
    # Weight (reduce BMI)
    # ---------------------------------------

    bmi = improved["Weight"] / (
        (improved["Height"] / 100) ** 2
    )

    if bmi > 25:

        target_weight = 24.9 * (
            (improved["Height"] / 100) ** 2
        )

        improved["Weight"] = round(target_weight, 1)

    # ---------------------------------------
    # Cholesterol
    # ---------------------------------------

    if improved["Cholesterol"] != "Normal":
        improved["Cholesterol"] = "Normal"

    # ---------------------------------------
    # Glucose
    # ---------------------------------------

    if improved["Glucose"] != "Normal":
        improved["Glucose"] = "Normal"

    return improved


def generate_counterfactual(patient):
    """
    Predict improved cardiac risk.
    """

    improved_patient = improve_patient(patient)

    processed = preprocess_input(improved_patient)

    prediction, probability, risk_level = predict_risk(
        processed
    )

    return {

        "patient": improved_patient,

        "prediction": prediction,

        "risk_level": risk_level,

        "improved_risk": probability

    }