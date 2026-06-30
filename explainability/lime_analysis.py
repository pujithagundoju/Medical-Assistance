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

Generates local explanations for an individual
cardiac risk prediction.
"""

import joblib
import pandas as pd
import streamlit as st

from lime.lime_tabular import LimeTabularExplainer

from config import MODEL_PATH
from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ==========================================================
# Load Model
# ==========================================================

@st.cache_resource
def load_model():
    """
    Load trained Random Forest model.
    """
    return joblib.load(MODEL_PATH)


# ==========================================================
# Build LIME Explainer
# ==========================================================

@st.cache_resource
def load_lime_explainer():
    """
    Build the LIME explainer using the
    cleaned training dataset.
    """

    df = load_data("data/cardio_train.csv")

    df = clean_data(df)

    X = df.drop(columns=["Heart_Disease"])

    explainer = LimeTabularExplainer(

        training_data=X.values,

        feature_names=X.columns.tolist(),

        class_names=[
            "Low Cardiac Risk",
            "High Cardiac Risk"
        ],

        mode="classification",

        discretize_continuous=True,

        random_state=42

    )

    return explainer


# ==========================================================
# Generate Explanation
# ==========================================================

def get_lime_explanation(processed_data):
    """
    Generate LIME explanation for a single patient.
    """

    model = load_model()

    explainer = load_lime_explainer()

    explanation = explainer.explain_instance(

        processed_data.iloc[0].values,

        model.predict_proba,

        num_features=len(processed_data.columns)

    )

    explanation_df = pd.DataFrame(

        explanation.as_list(),

        columns=[

            "Feature",

            "Contribution"

        ]

    )

    explanation_df["Impact"] = (

        explanation_df["Contribution"].abs()

    )

    explanation_df = explanation_df.sort_values(

        by="Impact",

        ascending=False

    ).drop(columns="Impact")

    explanation_df.reset_index(

        drop=True,

        inplace=True

    )

    return explanation_df