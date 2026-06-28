# services/counterfactual_service.py

from preprocessing.preprocess_input import preprocess_input
from model.predictor import predict_risk


def generate_counterfactual(patient_data):

    improved_patient = patient_data.copy()

    # Smoking improvement

    if improved_patient["Smoking"] == "Yes":
        improved_patient["Smoking"] = "No"

    # Blood Pressure improvement

    if improved_patient["Blood Pressure"] > 130:
        improved_patient["Blood Pressure"] = 130

    # Cholesterol improvement

    if improved_patient["Cholesterol Level"] > 200:
        improved_patient["Cholesterol Level"] = 200

    # BMI improvement

    if improved_patient["BMI"] > 25:
        improved_patient["BMI"] = 25

    # Exercise improvement

    improved_patient["Exercise Habits"] = "High"

    processed = preprocess_input(
        improved_patient
    )

    prediction, probability = predict_risk(
        processed
    )

    return {
        "improved_profile": improved_patient,
        "improved_risk": probability
    }