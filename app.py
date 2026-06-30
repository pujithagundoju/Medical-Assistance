# # """
# # Explainable Cardiac Risk Assessment Assistant

# # Main Streamlit Application
# # """
# # import streamlit as st

# # # ==========================================================
# # # Configuration
# # # ==========================================================

# # from config import (
# #     APP_TITLE,
# #     APP_ICON,
# #     LAYOUT
# # )

# # # ==========================================================
# # # UI Components
# # # ==========================================================
# # from services.recommendation_service import generate_recommendations
# # from ui.ai_chat import render_ai_chat
# # from ui.sidebar import render_sidebar
# # from ui.patient_form import render_patient_form
# # from ui.prediction_cards import render_prediction_cards
# # from ui.shap_tab import render_shap_tab
# # from ui.lime_tab import render_lime_tab
# # from ui.recommendation_tab import render_recommendation_tab
# # from ui.counterfactual_tab import render_counterfactual_tab
# # from ui.about_tab import render_about_tab
# # from ui.report_tab import render_report_tab
# # # ==========================================================
# # # Backend
# # # ==========================================================

# # from preprocessing.preprocess_input import preprocess_input

# # from model.predictor import predict_risk

# # from visualizations.risk_gauge import create_gauge

# # from services.clinical_interpreter import interpret_patient

# # from services.explanation_service import explain_prediction

# # from explainability.shap_analysis import (
# #     get_shap_explanation,
# #     get_top_risk_drivers
# # )

# # # ==========================================================
# # # Streamlit Configuration
# # # ==========================================================

# # st.set_page_config(

# #     page_title=APP_TITLE,

# #     page_icon=APP_ICON,

# #     layout=LAYOUT

# # )

# # # ==========================================================
# # # Sidebar
# # # ==========================================================

# # render_sidebar()

# # # ==========================================================
# # # Header
# # # ==========================================================

# # st.title(APP_TITLE)

# # st.markdown(
# # """
# # AI-powered Clinical Decision Support System using

# # Machine Learning

# # Explainable AI

# # Clinical Decision Support

# # Counterfactual Analysis

# # Google Gemini AI
# # """
# # )

# # st.markdown("---")

# # # ==========================================================
# # # Patient Form
# # # ==========================================================

# # patient_data = render_patient_form()

# # st.markdown("---")

# # predict_button = st.button(

# #     "❤️ Predict Cardiac Risk",

# #     use_container_width=True

# # )

# # # ==========================================================
# # # Prediction
# # # ==========================================================

# # if predict_button:

# #     try:

# #         # --------------------------------------------------

# #         processed_data = preprocess_input(

# #             patient_data

# #         )

# #         # --------------------------------------------------

# #         prediction, probability, risk_level = predict_risk(

# #             processed_data

# #         )

# #         # --------------------------------------------------

# #         clinical_summary = interpret_patient(

# #             patient_data

# #         )
        
# #         # --------------------------------------------------
# #         # Compute SHAP ONLY ONCE
# #         # --------------------------------------------------

# #         shap_df = get_shap_explanation(

# #             processed_data

# #         )

# #         top_factors = get_top_risk_drivers(

# #             shap_df

# #         )
# # #========= added===========
# #         st.session_state["patient_context"] = {

# #             "patient": patient_data,

# #             "prediction": "High Risk" if prediction == 1 else "Low Risk",

# #             "probability": probability,

# #             "clinical_summary": clinical_summary,

# #             "risk_factors": top_factors[
# #                 ["Feature", "SHAP_Value"]
# #             ].to_dict("records")

# #         }
# #         #===========================
# #         # --------------------------------------------------
# #         # Prediction Dashboard
# #         # --------------------------------------------------

# #         render_prediction_cards(

# #             prediction,

# #             probability,

# #             risk_level,

# #             patient_data

# #         )

# #         st.markdown("---")

# #         st.header("❤️ Cardiac Risk Gauge")

# #         gauge = create_gauge(

# #             probability

# #         )

# #         st.plotly_chart(

# #             gauge,

# #             use_container_width=True

# #         )

# #         st.markdown("---")
# #         # ==========================================================
# #         # Dashboard Tabs
# #         # ==========================================================

# #         tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(

# #             [

# #                 "📊 Clinical Summary",

# #                 "🧠 SHAP",

# #                 "🔍 LIME",

# #                 "🤖 AI Explanation",

# #                 "🩺 Recommendations",

# #                 "🔄 What-If Analysis",

# #                 "💬 AI Assistant",

# #                 "Report"

# #             ]

# #         )

# #         # ==========================================================
# #         # TAB 1 : Clinical Summary
# #         # ==========================================================

# #         with tab1:

# #             st.subheader("Patient Clinical Summary")

# #             if isinstance(clinical_summary, dict):

# #                 for key, value in clinical_summary.items():

# #                     st.write(

# #                         f"**{key}:** {value}"

# #                     )

# #             else:

# #                 st.write(clinical_summary)

# #         # ==========================================================
# #         # TAB 2 : SHAP
# #         # ==========================================================

# #         with tab2:

# #             st.subheader("SHAP Explainability")

# #             render_shap_tab(

# #                 processed_data

# #             )

# #         # ==========================================================
# #         # TAB 3 : LIME
# #         # ==========================================================

# #         with tab3:

# #             st.subheader("LIME Explainability")

# #             render_lime_tab(

# #                 processed_data

# #             )

# #         # ==========================================================
# #         # TAB 4 : Gemini Explanation
# #         # ==========================================================

# #         with tab4:

# #             st.subheader(

# #                 "AI Clinical Explanation"

# #             )

# #             explanation = explain_prediction(

# #                 patient_data,

# #                 probability,

# #                 top_factors,

# #                 clinical_summary

# #             )

# #             st.write(

# #                 explanation

# #             )

# #         # ==========================================================
# #         # TAB 5 : Recommendations
# #         # ==========================================================

# #         with tab5:

# #             st.subheader(

# #                 "Personalized Recommendations"

# #             )

# #             render_recommendation_tab(

# #                 patient_data

# #             )

# #         # ==========================================================
# #         # TAB 6 : Counterfactual
# #         # ==========================================================

# #         with tab6:

# #             st.subheader(

# #                 "What-If Analysis"

# #             )

# #             render_counterfactual_tab(

# #                 patient_data,

# #                 probability

# #             )

# #         st.markdown("---")
# #         #========================================================
# #         #TAB 7: AI Health Assistant
# #         #========================================================
# #         with tab7:
# #             render_ai_chat()
        

# #         with tab8:

# #             render_report_tab(

# #                patient_data,

# #                "High Risk" if prediction == 1 else "Low Risk",

# #                 probability,

# #                clinical_summary,

# #                generate_recommendations(patient_data),

# #                explanation

# #             )
# #         # ==========================================================
# #         # ABOUT SECTION
# #         # ==========================================================

# #         st.markdown("---")

# #         with st.expander(
# #             "ℹ About This Application"
# #         ):

# #             render_about_tab()

# #     # ==========================================================
# #     # ERROR HANDLING
# #     # ==========================================================

# #     except Exception as e:

# #         st.error(
# #             "An unexpected error occurred while processing the prediction."
# #         )

# #         st.exception(e)

# # # ==========================================================
# # # FOOTER
# # # ==========================================================

# # st.markdown("---")

# # col1, col2, col3 = st.columns(3)

# # with col1:

# #     st.caption(
# #         "❤️ Explainable Cardiac Risk Assessment Assistant"
# #     )

# # with col2:

# #     st.caption(
# #         "Machine Learning + Explainable AI"
# #     )

# # with col3:

# #     st.caption(
# #         "Version 2.0"
# #     )
# """
# CardioAI
# Explainable Cardiac Risk Assessment Assistant

# Main Streamlit Application
# """

# import streamlit as st

# # ==========================================================
# # Configuration
# # ==========================================================

# from config import (
#     APP_TITLE,
#     APP_ICON,
#     LAYOUT
# )

# # ==========================================================
# # UI Components
# # ==========================================================

# from ui.sidebar import render_sidebar
# from ui.patient_form import render_patient_form
# from ui.prediction_cards import render_prediction_cards
# from ui.shap_tab import render_shap_tab
# from ui.lime_tab import render_lime_tab
# from ui.recommendation_tab import render_recommendation_tab
# from ui.counterfactual_tab import render_counterfactual_tab
# from ui.about_tab import render_about_tab
# from ui.ai_chat import render_ai_chat

# # Report tab (we'll integrate after PDF is finalized)
# # from ui.report_tab import render_report_tab

# # ==========================================================
# # Backend
# # ==========================================================

# from preprocessing.preprocess_input import preprocess_input

# from model.predictor import predict_risk

# from visualizations.risk_gauge import create_gauge

# from services.clinical_interpreter import interpret_patient

# from services.explanation_service import explain_prediction

# from services.recommendation_service import (
#     generate_recommendations
# )

# from explainability.shap_analysis import (
#     get_shap_explanation,
#     get_top_risk_drivers
# )

# # ==========================================================
# # Page Configuration
# # ==========================================================

# st.set_page_config(

#     page_title=APP_TITLE,

#     page_icon=APP_ICON,

#     layout=LAYOUT

# )

# # ==========================================================
# # Sidebar
# # ==========================================================

# render_sidebar()

# # ==========================================================
# # Header
# # ==========================================================

# st.title(APP_TITLE)

# st.markdown(
# """
# ### 

# This Clinical Decision Support System combines

# - Machine Learning
# - Explainable AI (SHAP + LIME)
# - AI Clinical Explanation
# - Counterfactual Analysis
# - AI Health Assistant

# to help understand cardiovascular risk.
# """
# )

# st.divider()

# # ==========================================================
# # Patient Form
# # ==========================================================

# patient_data = render_patient_form()

# st.divider()

# predict_button = st.button(

#     "❤️ Predict Cardiac Risk",

#     use_container_width=True

# )
        
# # ==========================================================
# # Prediction
# # ==========================================================

# if predict_button:

#     try:

#         # --------------------------------------------------
#         # Preprocess Input
#         # --------------------------------------------------

#         processed_data = preprocess_input(
#             patient_data
#         )

#         # --------------------------------------------------
#         # Prediction
#         # --------------------------------------------------

#         prediction, probability, risk_level = predict_risk(
#             processed_data
#         )

#         prediction_text = (
#             "High Cardiac Risk"
#             if prediction == 1
#             else "Low Cardiac Risk"
#         )

#         # --------------------------------------------------
#         # Clinical Summary
#         # --------------------------------------------------

#         clinical_summary = interpret_patient(
#             patient_data
#         )

#         # --------------------------------------------------
#         # SHAP Analysis
#         # --------------------------------------------------

#         shap_df = get_shap_explanation(
#             processed_data
#         )

#         top_factors = get_top_risk_drivers(
#             shap_df
#         )

#         # --------------------------------------------------
#         # Recommendations
#         # --------------------------------------------------

#         recommendations = generate_recommendations(
#             patient_data
#         )

#         # --------------------------------------------------
#         # AI Explanation
#         # --------------------------------------------------

#         with st.spinner(
#             "Generating AI clinical explanation..."
#         ):

#             ai_explanation = explain_prediction(

#                 patient_data,

#                 probability,

#                 top_factors,

#                 clinical_summary

#             )

#         # --------------------------------------------------
#         # Store Context for AI Assistant
#         # --------------------------------------------------

#         st.session_state["patient_context"] = {

#             "patient": patient_data,

#             "prediction": prediction_text,

#             "probability": probability,

#             "clinical_summary": clinical_summary,

#             "risk_factors": top_factors.to_dict(
#                 "records"
#             )

#         }

#         # --------------------------------------------------
#         # Prediction Cards
#         # --------------------------------------------------

#         render_prediction_cards(

#             prediction,

#             probability,

#             risk_level,

#             patient_data

#         )

#         # --------------------------------------------------
#         # Risk Gauge
#         # --------------------------------------------------

#         st.divider()

#         st.header("❤️ Cardiac Risk Gauge")

#         gauge = create_gauge(
#             probability
#         )

#         st.plotly_chart(

#             gauge,

#             use_container_width=True

#         )

#         st.divider()
#         # ==========================================================
#         # Dashboard Tabs
#         # ==========================================================

#         tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(

#             [

#                 "📋 Clinical Summary",

#                 "🧠 SHAP",

#                 "🔍 LIME",

#                 "🤖 AI Explanation",

#                 "🩺 Recommendations",

#                 "🔄 What-If Analysis",

#                 "💬 AI Health Assistant"

#             ]

#         )

#         # ==========================================================
#         # TAB 1 - Clinical Summary
#         # ==========================================================

#         with tab1:

#             st.subheader("📋 Patient Clinical Summary")

#             for key, value in clinical_summary.items():

#                 st.markdown(

#                     f"**{key} :** {value}"

#                 )

#         # ==========================================================
#         # TAB 2 - SHAP
#         # ==========================================================

#         with tab2:

#             # st.subheader(
#             #     "🧠 SHAP Explainability"
#             # )

#             render_shap_tab(

#                 processed_data

#             )

#         # ==========================================================
#         # TAB 3 - LIME
#         # ==========================================================

#         with tab3:

#             # st.subheader(
#             #     "🔍 LIME Explainability"
#             # )

#             render_lime_tab(

#                 processed_data

#             )

#         # ==========================================================
#         # TAB 4 - AI Explanation
#         # ==========================================================

#         with tab4:

#             # st.subheader(
#             #     "🤖 AI Clinical Explanation"
#             # )

#             st.markdown(ai_explanation)

#         # ==========================================================
#         # TAB 5 - Recommendations
#         # ==========================================================

#         with tab5:

#             # st.subheader(
#             #     "🩺 Personalized Recommendations"
#             # )

#             render_recommendation_tab(

#                 patient_data

#             )

#         # ==========================================================
#         # TAB 6 - Counterfactual
#         # ==========================================================

#         with tab6:

#             # st.subheader(
#             #     "🔄 What-If Analysis"
#             # )

#             render_counterfactual_tab(

#                 patient_data,

#                 probability

#             )

#         # ==========================================================
#         # TAB 7 - AI Assistant
#         # ==========================================================

#         with tab7:

#             render_ai_chat()

#         # ==========================================================
#         # About
#         # ==========================================================

#         st.divider()

#         with st.expander(
#             "ℹ About This Application"
#         ):

#             render_about_tab()
#     # ==========================================================
#     # Error Handling
#     # ==========================================================

#     except Exception as e:

#         st.error(
#             "⚠ An unexpected error occurred while processing the prediction."
#         )

#         with st.expander("View Error Details"):

#             st.exception(e)

# # ==========================================================
# # Footer
# # ==========================================================

# st.divider()

# col1, col2, col3 = st.columns(3)

# with col1:

#     st.caption(
#         "❤️ CardioAI"
#     )

# with col2:

#     st.caption(
#         "Explainable Clinical Decision Support System"
#     )

# with col3:

#     st.caption(
#         "Version 2.0 | Powered by ML + SHAP + LIME + Gemini"
#     )
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