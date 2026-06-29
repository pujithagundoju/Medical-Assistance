# import os
# import joblib
# import pandas as pd

# MODEL_PATH = "model/heart_model.pkl"

# if not os.path.exists(MODEL_PATH):
#     raise FileNotFoundError(
#         "heart_model.pkl not found. Run train_model.py first."
#     )

# model = joblib.load(MODEL_PATH)


# def predict_risk(patient_df):

#     probability = model.predict_proba(
#         patient_df
#     )[0][1]

#     prediction = model.predict(
#         patient_df
#     )[0]

#     return prediction, probability
import joblib
import pandas as pd


class CardiacRiskPredictor:

    def __init__(self):

        self.model = joblib.load("model/random_forest.pkl")

    def predict(self, patient_df: pd.DataFrame):

        prediction = self.model.predict(patient_df)[0]

        probability = self.model.predict_proba(patient_df)[0][1]

        return prediction, probability

    def predict_probability(self, patient_df):

        return self.model.predict_proba(patient_df)[0][1]