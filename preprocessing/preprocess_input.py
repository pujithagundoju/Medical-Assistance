# import pandas as pd
# import joblib


# ENCODERS_PATH = "model/encoders.pkl"


# def preprocess_input(user_data):
#     """
#     Convert user input into the same format used during training.
#     """

#     encoders = joblib.load(ENCODERS_PATH)

#     processed_data = user_data.copy()

#     categorical_columns = [
#         "Gender",
#         "Exercise Habits",
#         "Smoking",
#         "Family Heart Disease",
#         "Diabetes",
#         "High Blood Pressure",
#         "Low HDL Cholesterol",
#         "High LDL Cholesterol",
#         "Alcohol Consumption",
#         "Stress Level",
#         "Sugar Consumption"
#     ]

#     for column in categorical_columns:

#         if column in encoders:

#             try:
#                 processed_data[column] = encoders[column].transform(
#                     [processed_data[column]]
#                 )[0]

#             except ValueError:

#                 raise ValueError(
#                     f"Unknown category '{processed_data[column]}' "
#                     f"for column '{column}'"
#                 )

#     return pd.DataFrame([processed_data])
"""
Preprocess User Input

Converts Streamlit form data into the
same format used during model training.
"""

import pandas as pd


def preprocess_input(patient_data: dict) -> pd.DataFrame:
    """
    Convert user input into model-ready DataFrame.
    """

    row = {

        "Age": patient_data["Age"],

        "Gender": 1 if patient_data["Gender"] == "Male" else 0,

        "Blood Pressure": patient_data["Blood Pressure"],

        "Cholesterol Level": patient_data["Cholesterol Level"],

        "Exercise Habits": {
            "Low": 0,
            "Medium": 1,
            "High": 2
        }[patient_data["Exercise Habits"]],

        "Smoking": 1 if patient_data["Smoking"] == "Yes" else 0,

        "Family Heart Disease": 1 if patient_data["Family Heart Disease"] == "Yes" else 0,

        "Diabetes": 1 if patient_data["Diabetes"] == "Yes" else 0,

        "BMI": patient_data["BMI"],

        "High Blood Pressure": 1 if patient_data["High Blood Pressure"] == "Yes" else 0,

        "Low HDL Cholesterol": 1 if patient_data["Low HDL Cholesterol"] == "Yes" else 0,

        "High LDL Cholesterol": 1 if patient_data["High LDL Cholesterol"] == "Yes" else 0,

        "Alcohol Consumption": {
            "Low": 0,
            "Medium": 1,
            "High": 2
        }[patient_data["Alcohol Consumption"]],

        "Stress Level": {
            "Low": 0,
            "Medium": 1,
            "High": 2
        }[patient_data["Stress Level"]],

        "Sleep Hours": patient_data["Sleep Hours"],

        "Sugar Consumption": {
            "Low": 0,
            "Medium": 1,
            "High": 2
        }[patient_data["Sugar Consumption"]],

        "Triglyceride Level": patient_data["Triglyceride Level"],

        "Fasting Blood Sugar": patient_data["Fasting Blood Sugar"],

        "CRP Level": patient_data["CRP Level"],

        "Homocysteine Level": patient_data["Homocysteine Level"]

    }

    return pd.DataFrame([row])