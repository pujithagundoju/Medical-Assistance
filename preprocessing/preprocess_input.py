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
Input Preprocessing
"""

import pandas as pd


def preprocess_input(input_data):

    bmi = input_data["Weight"] / (
        (input_data["Height"] / 100) ** 2
    )

    cholesterol = {
        "Normal": 1,
        "Above Normal": 2,
        "Well Above Normal": 3
    }

    glucose = {
        "Normal": 1,
        "Above Normal": 2,
        "Well Above Normal": 3
    }

    row = {

        "Age": input_data["Age"],

        "Gender": 1 if input_data["Gender"] == "Male" else 0,

        "Height": input_data["Height"],

        "Weight": input_data["Weight"],

        "Systolic_BP": input_data["Systolic_BP"],

        "Diastolic_BP": input_data["Diastolic_BP"],

        "Cholesterol": cholesterol[
            input_data["Cholesterol"]
        ],

        "Glucose": glucose[
            input_data["Glucose"]
        ],

        "Smoking": 1 if input_data["Smoking"] == "Yes" else 0,

        "Alcohol": 1 if input_data["Alcohol"] == "Yes" else 0,

        "Physical_Activity":
            1 if input_data["Physical_Activity"] == "Yes" else 0,

        "BMI": round(bmi, 2)

    }

    columns = [

        "Age",

        "Gender",

        "Height",

        "Weight",

        "Systolic_BP",

        "Diastolic_BP",

        "Cholesterol",

        "Glucose",

        "Smoking",

        "Alcohol",

        "Physical_Activity",

        "BMI"

    ]

    return pd.DataFrame(
        [row],
        columns=columns
    )