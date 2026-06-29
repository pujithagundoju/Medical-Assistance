# from sklearn.preprocessing import LabelEncoder

# def clean_data(df):

#     df = df.copy()

#     df.fillna(df.median(numeric_only=True), inplace=True)

#     categorical_cols = df.select_dtypes(include=["object"]).columns

#     encoders = {}

#     for col in categorical_cols:

#         encoder = LabelEncoder()

#         df[col] = encoder.fit_transform(df[col].astype(str))

#         encoders[col] = encoder

#     return df, encoders
import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame):
    """
    Clean the cardiovascular dataset.
    """

    df = df.copy()

    # ----------------------------------
    # Remove duplicate rows
    # ----------------------------------

    df.drop_duplicates(inplace=True)

    # ----------------------------------
    # Drop ID
    # ----------------------------------

    if "id" in df.columns:
        df.drop(columns=["id"], inplace=True)

    # ----------------------------------
    # Convert age from days to years
    # ----------------------------------

    df["age"] = (df["age"] / 365).astype(int)

    # ----------------------------------
    # Rename columns
    # ----------------------------------

    df.rename(columns={
        "age": "Age",
        "gender": "Gender",
        "height": "Height",
        "weight": "Weight",
        "ap_hi": "Systolic_BP",
        "ap_lo": "Diastolic_BP",
        "cholesterol": "Cholesterol",
        "gluc": "Glucose",
        "smoke": "Smoking",
        "alco": "Alcohol",
        "active": "Physical_Activity",
        "cardio": "Heart_Disease"
    }, inplace=True)

    # ----------------------------------
    # Encode gender
    # Female=0
    # Male=1
    # ----------------------------------

    df["Gender"] = df["Gender"].replace({
        1: 0,
        2: 1
    })

    # ----------------------------------
    # BMI
    # ----------------------------------

    df["BMI"] = (
        df["Weight"] /
        ((df["Height"] / 100) ** 2)
    )

    # ----------------------------------
    # Remove impossible BP
    # ----------------------------------

    df = df[
        (df["Systolic_BP"] > 60) &
        (df["Systolic_BP"] < 250)
    ]

    df = df[
        (df["Diastolic_BP"] > 40) &
        (df["Diastolic_BP"] < 180)
    ]

    # ----------------------------------
    # Remove impossible BMI
    # ----------------------------------

    df = df[
        (df["BMI"] > 10) &
        (df["BMI"] < 70)
    ]

    # ----------------------------------
    # Fill missing values
    # ----------------------------------

    for col in df.columns:

        if df[col].dtype in ["int64", "float64"]:

            df[col].fillna(df[col].median(), inplace=True)

        else:

            df[col].fillna(df[col].mode()[0], inplace=True)

    return df