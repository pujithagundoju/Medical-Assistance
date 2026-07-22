
"""
CardioAI
Explainable Cardiac Risk Assessment Assistant

Main Streamlit Application
"""

import streamlit as st

# ==========================================================
# Configuration
# ==========================================================

from config import (
    APP_TITLE,
    APP_ICON,
    LAYOUT
)

# ==========================================================
# UI Components
# ==========================================================
from ui.report_tab import render_report_tab
from ui.sidebar import render_sidebar
from ui.patient_form import render_patient_form
from ui.prediction_cards import render_prediction_cards
from ui.shap_tab import render_shap_tab
from ui.lime_tab import render_lime_tab
from ui.recommendation_tab import render_recommendation_tab
from ui.counterfactual_tab import render_counterfactual_tab
from ui.about_tab import render_about_tab
from ui.ai_chat import render_ai_chat

# PDF (we'll enable later)
# from ui.report_tab import render_report_tab

# ==========================================================
# Backend
# ==========================================================

from preprocessing.preprocess_input import preprocess_input
from model.predictor import predict_risk

from visualizations.risk_gauge import create_gauge

from services.clinical_interpreter import (
    interpret_patient
)

from services.explanation_service import (
    explain_prediction
)

from services.recommendation_service import (
    generate_recommendations
)

from explainability.shap_analysis import (
    get_shap_explanation,
    get_top_risk_drivers
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title=APP_TITLE,

    page_icon=APP_ICON,

    layout=LAYOUT

)

# ==========================================================
# Session State
# ==========================================================

if "prediction_done" not in st.session_state:

    st.session_state.prediction_done = False

if "results" not in st.session_state:

    st.session_state.results = {}

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# ==========================================================
# Sidebar
# ==========================================================

render_sidebar()

# ==========================================================
# Header
# ==========================================================

st.title(APP_TITLE)

st.markdown(
"""
### AI Powered Clinical Decision Support System

This application combines

- ❤️ Machine Learning
- 🧠 SHAP Explainability
- 🔍 LIME Explainability
- 🤖 Google Gemini AI
- 🔄 Counterfactual Analysis
- 💬 AI Health Assistant

to help explain cardiovascular risk predictions.
"""
)

st.divider()

# ==========================================================
# Patient Form
# ==========================================================

patient_data = render_patient_form()

st.divider()

predict_button = st.button(

    "❤️ Predict Cardiac Risk",

    use_container_width=True

)

# ==========================================================
# Prediction Pipeline
# ==========================================================

if predict_button:

    try:

        processed_data = preprocess_input(
            patient_data
        )

        prediction, probability, risk_level = predict_risk(
            processed_data
        )

        prediction_text = (

            "High Cardiac Risk"

            if prediction == 1

            else "Low Cardiac Risk"

        )

        clinical_summary = interpret_patient(
            patient_data
        )

        shap_df = get_shap_explanation(
            processed_data
        )

#         prediction, probability, risk_level = predict_risk(processed_data)

#         prediction_text = (
#             "High Cardiac Risk"
#             if prediction == 1
#             else "Low Cardiac Risk"
#         )
# # Show prediction immediately
#         render_prediction_cards(
#             prediction_text,
#             probability,
#             risk_level
#         )

#         clinical_summary = interpret_patient(patient_data)

# # SHAP should not stop the whole application
#         try:
#             shap_df = get_shap_explanation(processed_data)
#             top_factors = get_top_risk_drivers(shap_df)
#         except Exception as e:
#             st.warning(f"SHAP explanation unavailable: {e}")
#             shap_df = None
#             top_factors = None

        top_factors = get_top_risk_drivers(
            shap_df
        )

        recommendations = generate_recommendations(
            patient_data
        )

        with st.spinner(
            "Generating AI Clinical Explanation..."
        ):

            ai_explanation = explain_prediction(

                patient_data,

                probability,

                top_factors,

                clinical_summary

            )
        # ==========================================================
        # Save Results
        # ==========================================================

        st.session_state.results = {

            "processed_data": processed_data,

            "patient_data": patient_data,

            "prediction": prediction,

            "prediction_text": prediction_text,

            "probability": probability,

            "risk_level": risk_level,

            "clinical_summary": clinical_summary,

            "shap_df": shap_df,

            "top_factors": top_factors,

            "recommendations": recommendations,

            "ai_explanation": ai_explanation

        }

        # ----------------------------------------------

        st.session_state["patient_context"] = {

            "patient": patient_data,

            "prediction": prediction_text,

            "probability": probability,

            "clinical_summary": clinical_summary,

            "risk_factors": top_factors.to_dict(
                "records"
            )

        }

        # ----------------------------------------------

        st.session_state.prediction_done = True

    except Exception as e:

        st.error(
            "⚠ Unable to generate prediction."
        )

        st.exception(e)

# ==========================================================
# Dashboard
# ==========================================================

if st.session_state.prediction_done:

    results = st.session_state.results

    processed_data = results["processed_data"]

    patient_data = results["patient_data"]

    prediction = results["prediction"]

    prediction_text = results["prediction_text"]

    probability = results["probability"]

    risk_level = results["risk_level"]

    clinical_summary = results["clinical_summary"]

    shap_df = results["shap_df"]

    top_factors = results["top_factors"]

    recommendations = results["recommendations"]

    ai_explanation = results["ai_explanation"]

    # ======================================================
    # Prediction Cards
    # ======================================================

    render_prediction_cards(

        prediction,

        probability,

        risk_level,

        patient_data

    )

    st.divider()

    # ======================================================
    # Risk Gauge
    # ======================================================

    st.header("❤️ Cardiac Risk Gauge")

    gauge = create_gauge(

        probability

    )

    st.plotly_chart(

        gauge,

        use_container_width=True

    )

    st.divider()
    # ==========================================================
    # Dashboard Tabs
    # ==========================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(

        [

            "📋 Clinical Summary",

            "🧠 SHAP",

            "🔍 LIME",

            "🤖 AI Explanation",

            "🩺 Recommendations",

            "🔄 What-If Analysis",

            "💬 AI Assistant",

            "📄 Report"

        ]

    )

    # ==========================================================
    # TAB 1
    # ==========================================================

    with tab1:

        st.subheader(
            "📋 Patient Clinical Summary"
        )

        if isinstance(clinical_summary, dict):

            for key, value in clinical_summary.items():

                st.markdown(

                    f"**{key}:** {value}"

                )

        else:

            st.write(clinical_summary)

    # ==========================================================
    # TAB 2
    # ==========================================================

    with tab2:

        render_shap_tab(

            processed_data

        )

    # ==========================================================
    # TAB 3
    # ==========================================================

    with tab3:

        render_lime_tab(

            processed_data

        )

    # ==========================================================
    # TAB 4
    # ==========================================================

    with tab4:

        st.subheader(
            "🤖 AI Clinical Explanation"
        )

        st.markdown(

            ai_explanation

        )

    # ==========================================================
    # TAB 5
    # ==========================================================

    with tab5:

        render_recommendation_tab(

            patient_data

        )

    # ==========================================================
    # TAB 6
    # ==========================================================

    with tab6:

        render_counterfactual_tab(

            patient_data,

            probability

        )

    # ==========================================================
    # TAB 7
    # ==========================================================

    with tab7:

        render_ai_chat()
    
    with tab8:

        render_report_tab(

          patient_data,

          prediction_text,

          probability,

          clinical_summary,

          recommendations,

          ai_explanation

     )
    # ==========================================================
    # About
    # ==========================================================

    st.divider()

    with st.expander(

        "ℹ About This Application"

    ):

        render_about_tab()
# ==========================================================
# Footer
# ==========================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.caption(
        "❤️ CardioAI"
    )

with col2:

    st.caption(
        "Explainable AI Clinical Decision Support"
    )

with col3:

    st.caption(
        "Version 2.0"
    )