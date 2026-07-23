# # # import shap
# # # import joblib
# # # import pandas as pd
# # # import numpy as np

# # # # Load trained model
# # # model = joblib.load("model/heart_model.pkl")


# # # def get_shap_explanation(input_df):
# # #     """
# # #     Generate SHAP values for a single patient record.
# # #     Compatible with different SHAP versions.
# # #     """

# # #     explainer = shap.TreeExplainer(model)

# # #     shap_values = explainer.shap_values(input_df)

# # #     # -----------------------------
# # #     # Handle different SHAP outputs
# # #     # -----------------------------

# # #     if isinstance(shap_values, list):
# # #         # Older SHAP versions
# # #         shap_values = shap_values[1]

# # #     elif isinstance(shap_values, np.ndarray):

# # #         if len(shap_values.shape) == 3:
# # #             # Shape:
# # #             # (samples, features, classes)
# # #             shap_values = shap_values[:, :, 1]

# # #     # -----------------------------
# # #     # Safety check
# # #     # -----------------------------

# # #     feature_values = shap_values[0]

# # #     if len(feature_values.shape) > 1:
# # #         feature_values = feature_values.flatten()

# # #     # -----------------------------
# # #     # Build feature importance table
# # #     # -----------------------------

# # #     feature_impacts = pd.DataFrame({
# # #         "Feature": input_df.columns.tolist(),
# # #         "SHAP_Value": feature_values
# # #     })

# # #     feature_impacts["Absolute"] = (
# # #         feature_impacts["SHAP_Value"].abs()
# # #     )

# # #     feature_impacts = feature_impacts.sort_values(
# # #         by="Absolute",
# # #         ascending=False
# # #     )

# # #     return feature_impacts


# # # def get_top_risk_drivers(
# # #     shap_df,
# # #     top_n=5
# # # ):
# # #     """
# # #     Return top positive contributors to risk.
# # #     """

# # #     positive = shap_df[
# # #         shap_df["SHAP_Value"] > 0
# # #     ]

# # #     if len(positive) == 0:
# # #         return shap_df.head(top_n)

# # #     return positive.head(top_n)
# # """
# # SHAP Explainability Module

# # Provides local feature importance for each prediction.
# # """

# # import joblib
# # import shap
# # import pandas as pd
# # import streamlit as st


# # # ============================================================
# # # Load model only once
# # # ============================================================

# # @st.cache_resource
# # def load_model():

# #     return joblib.load("model/random_forest.pkl")


# # # ============================================================
# # # Create SHAP Explainer only once
# # # ============================================================

# # @st.cache_resource
# # def load_explainer():

# #     model = load_model()

# #     return shap.TreeExplainer(model)


# # # ============================================================
# # # Calculate SHAP Values
# # # ============================================================

# # # def get_shap_explanation(processed_data):

# # #     explainer = load_explainer()

# # #     shap_values = explainer.shap_values(processed_data)

# # #     model = load_model()

# # #     feature_names = model.feature_names_in_

# # #     # Binary classification
# # #     if isinstance(shap_values, list):

# # #         values = shap_values[1][0]

# # #     else:

# # #         values = shap_values[0]

# # #     shap_df = pd.DataFrame({

# # #         "Feature": feature_names,

# # #         "SHAP_Value": values,

# # #         "Impact": abs(values)

# # #     })

# # #     shap_df = shap_df.sort_values(

# # #         by="Impact",

# # #         ascending=False

# # #     ).reset_index(drop=True)

# # #     return shap_df

# # def get_shap_explanation(processed_data):

# #     explainer = load_explainer()

# #     model = load_model()

# #     feature_names = model.feature_names_in_

# #     # Compute SHAP values
# #     shap_values = explainer(processed_data)

# #     # ========================================================
# #     # Compatible with SHAP 0.52+
# #     # ========================================================

# #     values = shap_values.values

# #     # Binary classification
# #     if values.ndim == 3:
# #         values = values[:, :, 1]

# #     # Single patient
# #     values = values[0]

# #     shap_df = pd.DataFrame({

# #         "Feature": feature_names,

# #         "SHAP_Value": values,

# #         "Impact": abs(values)

# #     })

# #     shap_df = shap_df.sort_values(

# #         by="Impact",

# #         ascending=False

# #     ).reset_index(drop=True)

# #     return shap_df
# # # ============================================================
# # # Top Risk Drivers
# # # ============================================================

# # def get_top_risk_drivers(

# #     shap_df,

# #     top_n=5

# # ):

# #     return shap_df.head(top_n)


# # # ============================================================
# # # Positive Contributors
# # # ============================================================

# # def positive_contributors(

# #     shap_df,

# #     top_n=5

# # ):

# #     positive = shap_df[

# #         shap_df["SHAP_Value"] > 0

# #     ]

# #     return positive.sort_values(

# #         by="SHAP_Value",

# #         ascending=False

# #     ).head(top_n)


# # # ============================================================
# # # Protective Contributors
# # # ============================================================

# # def protective_contributors(

# #     shap_df,

# #     top_n=5

# # ):

# #     negative = shap_df[

# #         shap_df["SHAP_Value"] < 0

# #     ]

# #     return negative.sort_values(

# #         by="SHAP_Value"

# #     ).head(top_n)
# """
# SHAP Explainability Module

# Provides local feature importance for each prediction.
# """

# import joblib
# import shap
# import pandas as pd
# import streamlit as st


# # ============================================================
# # Load model only once
# # ============================================================

# @st.cache_resource
# def load_model():
#     return joblib.load("model/random_forest.pkl")


# # ============================================================
# # Create SHAP Explainer only once
# # ============================================================

# @st.cache_resource
# def load_explainer():
#     model = load_model()
#     return shap.TreeExplainer(model)


# # ============================================================
# # Calculate SHAP Values
# # ============================================================

# def get_shap_explanation(processed_data):
#     """
#     Returns SHAP feature importance dataframe.

#     If SHAP fails, returns a dataframe with zero impacts
#     so the application can continue running.
#     """

#     model = load_model()
#     feature_names = list(model.feature_names_in_)

#     try:
#         explainer = load_explainer()

#         shap_values = explainer(processed_data)

#         values = shap_values.values

#         # Binary classifier
#         if values.ndim == 3:
#             values = values[:, :, 1]

#         values = values[0]

#         shap_df = pd.DataFrame({
#             "Feature": feature_names,
#             "SHAP_Value": values,
#             "Impact": abs(values)
#         })

#         shap_df = shap_df.sort_values(
#             by="Impact",
#             ascending=False
#         ).reset_index(drop=True)

#         return shap_df

#     except Exception as e:

#         st.warning(f"SHAP could not be generated: {e}")

#         return pd.DataFrame({
#             "Feature": feature_names,
#             "SHAP_Value": [0.0] * len(feature_names),
#             "Impact": [0.0] * len(feature_names)
#         })


# # ============================================================
# # Top Risk Drivers
# # ============================================================

# def get_top_risk_drivers(shap_df, top_n=5):
#     if shap_df is None or shap_df.empty:
#         return pd.DataFrame(columns=["Feature", "SHAP_Value", "Impact"])

#     return shap_df.head(top_n)


# # ============================================================
# # Positive Contributors
# # ============================================================

# def positive_contributors(shap_df, top_n=5):
#     if shap_df is None or shap_df.empty:
#         return pd.DataFrame(columns=["Feature", "SHAP_Value", "Impact"])

#     positive = shap_df[
#         shap_df["SHAP_Value"] > 0
#     ]

#     return positive.sort_values(
#         by="SHAP_Value",
#         ascending=False
#     ).head(top_n)


# # ============================================================
# # Protective Contributors
# # ============================================================

# def protective_contributors(shap_df, top_n=5):
#     if shap_df is None or shap_df.empty:
#         return pd.DataFrame(columns=["Feature", "SHAP_Value", "Impact"])

#     negative = shap_df[
#         shap_df["SHAP_Value"] < 0
#     ]

#     return negative.sort_values(
#         by="SHAP_Value"
#     ).head(top_n)
"""
SHAP Explainability Module

Provides local feature importance for each prediction.
"""

import gc
import joblib
import pandas as pd
import shap
import streamlit as st


# ============================================================
# Cached Model
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("model/random_forest.pkl")


# ============================================================
# Cached Explainer
# ============================================================

@st.cache_resource
def load_explainer():

    model = load_model()

    return shap.TreeExplainer(
        model,
        feature_perturbation="tree_path_dependent"
    )


# ============================================================
# SHAP Explanation
# ============================================================

def get_shap_explanation(processed_data):

    model = load_model()

    feature_names = list(model.feature_names_in_)

    try:

        explainer = load_explainer()

        explanation = explainer(processed_data)

        values = explanation.values

        del explanation

        if values.ndim == 3:
            values = values[:, :, 1]

        values = values[0]

        shap_df = pd.DataFrame({

            "Feature": feature_names,

            "SHAP_Value": values,

            "Impact": abs(values)

        })

        shap_df = (
            shap_df
            .sort_values(
                "Impact",
                ascending=False
            )
            .reset_index(drop=True)
        )

        del values

        gc.collect()

        return shap_df

    except Exception as e:

        st.warning(
            f"SHAP could not be generated: {e}"
        )

        return pd.DataFrame({

            "Feature": feature_names,

            "SHAP_Value": [0.0] * len(feature_names),

            "Impact": [0.0] * len(feature_names)

        })


# ============================================================
# Top Drivers
# ============================================================

def get_top_risk_drivers(
    shap_df,
    top_n=5
):

    if shap_df is None or shap_df.empty:

        return pd.DataFrame(
            columns=[
                "Feature",
                "SHAP_Value",
                "Impact"
            ]
        )

    return shap_df.head(top_n)


# ============================================================
# Positive Contributors
# ============================================================

def positive_contributors(
    shap_df,
    top_n=5
):

    if shap_df is None or shap_df.empty:

        return pd.DataFrame(
            columns=[
                "Feature",
                "SHAP_Value",
                "Impact"
            ]
        )

    return (
        shap_df[
            shap_df["SHAP_Value"] > 0
        ]
        .sort_values(
            "SHAP_Value",
            ascending=False
        )
        .head(top_n)
    )


# ============================================================
# Protective Contributors
# ============================================================

def protective_contributors(
    shap_df,
    top_n=5
):

    if shap_df is None or shap_df.empty:

        return pd.DataFrame(
            columns=[
                "Feature",
                "SHAP_Value",
                "Impact"
            ]
        )

    return (
        shap_df[
            shap_df["SHAP_Value"] < 0
        ]
        .sort_values(
            "SHAP_Value"
        )
        .head(top_n)
    )