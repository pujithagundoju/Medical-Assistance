import pandas as pd
import joblib


ENCODERS_PATH = "model/encoders.pkl"


def preprocess_input(user_data):
    """
    Convert user input into the same format used during training.
    """

    encoders = joblib.load(ENCODERS_PATH)

    processed_data = user_data.copy()

    categorical_columns = [
        "Gender",
        "Exercise Habits",
        "Smoking",
        "Family Heart Disease",
        "Diabetes",
        "High Blood Pressure",
        "Low HDL Cholesterol",
        "High LDL Cholesterol",
        "Alcohol Consumption",
        "Stress Level",
        "Sugar Consumption"
    ]

    for column in categorical_columns:

        if column in encoders:

            try:
                processed_data[column] = encoders[column].transform(
                    [processed_data[column]]
                )[0]

            except ValueError:

                raise ValueError(
                    f"Unknown category '{processed_data[column]}' "
                    f"for column '{column}'"
                )

    return pd.DataFrame([processed_data])