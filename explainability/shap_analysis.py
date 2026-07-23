"""
SHAP Explainability Module

Provides local feature importance for each prediction.
"""

import joblib
import shap
import pandas as pd
import streamlit as st


# ============================================================
# Load model only once
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load("model/random_forest.pkl")


# ============================================================
# Create SHAP Explainer only once
# ============================================================

@st.cache_resource
def load_explainer():

    model = load_model()

    return shap.TreeExplainer(model)


# ============================================================
# Calculate SHAP Values
# ============================================================

# def get_shap_explanation(processed_data):

#     explainer = load_explainer()

#     shap_values = explainer.shap_values(processed_data)

#     model = load_model()

#     feature_names = model.feature_names_in_

#     # Binary classification
#     if isinstance(shap_values, list):

#         values = shap_values[1][0]

#     else:

#         values = shap_values[0]

#     shap_df = pd.DataFrame({

#         "Feature": feature_names,

#         "SHAP_Value": values,

#         "Impact": abs(values)

#     })

#     shap_df = shap_df.sort_values(

#         by="Impact",

#         ascending=False

#     ).reset_index(drop=True)

#     return shap_df

def get_shap_explanation(processed_data):

    explainer = load_explainer()

    model = load_model()

    feature_names = model.feature_names_in_

    # Compute SHAP values
    shap_values = explainer(processed_data)

    # ========================================================
    # Compatible with SHAP 0.52+
    # ========================================================

    values = shap_values.values

    # Binary classification
    if values.ndim == 3:
        values = values[:, :, 1]

    # Single patient
    values = values[0]

    shap_df = pd.DataFrame({

        "Feature": feature_names,

        "SHAP_Value": values,

        "Impact": abs(values)

    })

    shap_df = shap_df.sort_values(

        by="Impact",

        ascending=False

    ).reset_index(drop=True)

    return shap_df
# ============================================================
# Top Risk Drivers
# ============================================================

def get_top_risk_drivers(

    shap_df,

    top_n=5

):

    return shap_df.head(top_n)


# ============================================================
# Positive Contributors
# ============================================================

def positive_contributors(

    shap_df,

    top_n=5

):

    positive = shap_df[

        shap_df["SHAP_Value"] > 0

    ]

    return positive.sort_values(

        by="SHAP_Value",

        ascending=False

    ).head(top_n)


# ============================================================
# Protective Contributors
# ============================================================

def protective_contributors(

    shap_df,

    top_n=5

):

    negative = shap_df[

        shap_df["SHAP_Value"] < 0

    ]

    return negative.sort_values(

        by="SHAP_Value"

    ).head(top_n)