# # import os
# # import joblib
# # import pandas as pd

# # MODEL_PATH = "model/heart_model.pkl"

# # if not os.path.exists(MODEL_PATH):
# #     raise FileNotFoundError(
# #         "heart_model.pkl not found. Run train_model.py first."
# #     )

# # model = joblib.load(MODEL_PATH)


# # def predict_risk(patient_df):

# #     probability = model.predict_proba(
# #         patient_df
# #     )[0][1]

# #     prediction = model.predict(
# #         patient_df
# #     )[0]

# #     return prediction, probability
# import joblib
# import pandas as pd


# class CardiacRiskPredictor:

#     def __init__(self):

#         self.model = joblib.load("model/random_forest.pkl")

#     def predict(self, patient_df: pd.DataFrame):

#         prediction = self.model.predict(patient_df)[0]

#         probability = self.model.predict_proba(patient_df)[0][1]

#         return prediction, probability

#     def predict_probability(self, patient_df):

#         return self.model.predict_proba(patient_df)[0][1]
"""
Prediction Module

Loads the trained model once and provides
prediction utilities.
"""

import joblib
import pandas as pd
import streamlit as st


# =====================================================
# Load Model (Cached)
# =====================================================

@st.cache_resource
def load_model():
    """
    Load trained model only once.
    """
    model = joblib.load("model/best_model.pkl")
    return model


# =====================================================
# Predict Class
# =====================================================

def predict(processed_data):
    """
    Returns predicted class.
    """

    model = load_model()

    prediction = model.predict(processed_data)

    return int(prediction[0])


# =====================================================
# Predict Probability
# =====================================================

def predict_probability(processed_data):
    """
    Returns probability of Heart Disease.
    """

    model = load_model()

    probability = model.predict_proba(processed_data)

    return float(probability[0][1])


# =====================================================
# Complete Prediction
# =====================================================

def predict_risk(processed_data):
    """
    Returns

    prediction

    probability

    risk level

    """

    prediction = predict(processed_data)

    probability = predict_probability(processed_data)

    if probability < 0.20:

        risk_level = "Very Low"

    elif probability < 0.40:

        risk_level = "Low"

    elif probability < 0.60:

        risk_level = "Moderate"

    elif probability < 0.80:

        risk_level = "High"

    else:

        risk_level = "Very High"

    return prediction, probability, risk_level


# =====================================================
# Batch Prediction
# =====================================================

def batch_predict(df):
    """
    Predict multiple patients.
    """

    model = load_model()

    prediction = model.predict(df)

    probability = model.predict_proba(df)[:, 1]

    results = pd.DataFrame({

        "Prediction": prediction,

        "Probability": probability

    })

    return results