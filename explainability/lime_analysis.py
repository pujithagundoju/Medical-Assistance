# import lime
# import lime.lime_tabular

# def build_lime_explainer(model, X_train, feature_names):
    
#     explainer = lime.lime_tabular.LimeTabularExplainer(
#         training_data=X_train,
#         feature_names=feature_names,
#         class_names=["Low Risk", "High Risk"],
#         mode="classification"
#     )

#     return explainer
"""
LIME Explainability Module

Provides local explanations for an individual prediction.
"""

import joblib
import pandas as pd
import streamlit as st

from lime.lime_tabular import LimeTabularExplainer

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ============================================================
# Load Model
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load("model/best_model.pkl")


# ============================================================
# Build LIME Explainer
# ============================================================

@st.cache_resource
def load_lime_explainer():

    df = load_data("data/heart_disease.csv")

    df, _ = clean_data(df)

    X = df.drop(
        columns=["Heart Disease Status"]
    )

    explainer = LimeTabularExplainer(

        training_data=X.values,

        feature_names=X.columns.tolist(),

        class_names=["Low Risk", "High Risk"],

        mode="classification",

        discretize_continuous=True

    )

    return explainer


# ============================================================
# Explain Prediction
# ============================================================

def get_lime_explanation(processed_data):

    model = load_model()

    explainer = load_lime_explainer()

    explanation = explainer.explain_instance(

        processed_data.iloc[0].values,

        model.predict_proba,

        num_features=10

    )

    explanation_df = pd.DataFrame(

        explanation.as_list(),

        columns=[

            "Feature",

            "Contribution"

        ]

    )

    explanation_df["Impact"] = (

        explanation_df["Contribution"]

        .abs()

    )

    explanation_df = explanation_df.sort_values(

        by="Impact",

        ascending=False

    )

    return explanation_df