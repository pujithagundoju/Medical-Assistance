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
import pandas as pd


def preprocess_input(input_data: dict) -> pd.DataFrame:
    """
    Convert Streamlit user input
    into model-ready dataframe.
    """

    age = input_data["Age"]

    gender = 1 if input_data["Gender"] == "Male" else 0

    height = input_data["Height"]

    weight = input_data["Weight"]

    bmi = weight / ((height / 100) ** 2)

    row = {

        "Age": age,

        "Gender": gender,

        "Height": height,

        "Weight": weight,

        "Systolic_BP": input_data["Systolic_BP"],

        "Diastolic_BP": input_data["Diastolic_BP"],

        "Cholesterol": input_data["Cholesterol"],

        "Glucose": input_data["Glucose"],

        "Smoking": input_data["Smoking"],

        "Alcohol": input_data["Alcohol"],

        "Physical_Activity": input_data["Physical_Activity"],

        "BMI": bmi

    }

    return pd.DataFrame([row])