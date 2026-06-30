# print("RUNNING APP FROM:", __file__)
# from dotenv import load_dotenv

# load_dotenv()

# import streamlit as st

# from preprocessing.preprocess_input import preprocess_input
# from model.predictor import predict_risk

# from visualizations.risk_gauge import create_gauge

# from services.explanation_service import explain_prediction
# from services.recommendation_service import generate_recommendations
# from services.clinical_interpreter import interpret_patient
# from services.counterfactual_service import generate_counterfactual

# from explainability.shap_analysis import (
#     get_shap_explanation,
#     get_top_risk_drivers
# )

# st.set_page_config(
#     page_title="Cardiac Risk Assessment Assistant",
#     layout="wide"
# )

# st.title("❤️ Explainable Cardiac Risk Assessment Assistant")

# st.markdown("---")

# st.subheader("Patient Information")

# col1, col2 = st.columns(2)

# with col1:

#     age = st.number_input(
#         "Age",
#         18,
#         120,
#         40
#     )

#     gender = st.selectbox(
#         "Gender",
#         ["Male", "Female"]
#     )

#     blood_pressure = st.number_input(
#         "Blood Pressure",
#         50,
#         250,
#         120
#     )

#     cholesterol = st.number_input(
#         "Cholesterol Level",
#         50,
#         500,
#         180
#     )

#     bmi = st.number_input(
#         "BMI",
#         10.0,
#         60.0,
#         25.0
#     )

#     sleep_hours = st.number_input(
#         "Sleep Hours",
#         0,
#         24,
#         7
#     )

# with col2:

#     exercise = st.selectbox(
#         "Exercise Habits",
#         ["Low", "Medium", "High"]
#     )

#     smoking = st.selectbox(
#         "Smoking",
#         ["Yes", "No"]
#     )

#     family_history = st.selectbox(
#         "Family Heart Disease",
#         ["Yes", "No"]
#     )

#     diabetes = st.selectbox(
#         "Diabetes",
#         ["Yes", "No"]
#     )

#     high_bp = st.selectbox(
#         "High Blood Pressure",
#         ["Yes", "No"]
#     )

#     low_hdl = st.selectbox(
#         "Low HDL Cholesterol",
#         ["Yes", "No"]
#     )

#     high_ldl = st.selectbox(
#         "High LDL Cholesterol",
#         ["Yes", "No"]
#     )

#     alcohol = st.selectbox(
#         "Alcohol Consumption",
#         ["Low", "Medium", "High"]
#     )

#     stress = st.selectbox(
#         "Stress Level",
#         ["Low", "Medium", "High"]
#     )

#     sugar = st.selectbox(
#         "Sugar Consumption",
#         ["Low", "Medium", "High"]
#     )

# st.markdown("---")

# st.subheader("Lab Measurements")

# triglycerides = st.number_input(
#     "Triglyceride Level",
#     0.0,
#     1000.0,
#     150.0
# )

# fasting_sugar = st.number_input(
#     "Fasting Blood Sugar",
#     0.0,
#     500.0,
#     100.0
# )

# crp = st.number_input(
#     "CRP Level",
#     0.0,
#     100.0,
#     2.0
# )

# homocysteine = st.number_input(
#     "Homocysteine Level",
#     0.0,
#     100.0,
#     10.0
# )

# if st.button("Predict Cardiac Risk"):

#     patient_data = {

#         "Age": age,
#         "Gender": gender,
#         "Blood Pressure": blood_pressure,
#         "Cholesterol Level": cholesterol,
#         "Exercise Habits": exercise,
#         "Smoking": smoking,
#         "Family Heart Disease": family_history,
#         "Diabetes": diabetes,
#         "BMI": bmi,
#         "High Blood Pressure": high_bp,
#         "Low HDL Cholesterol": low_hdl,
#         "High LDL Cholesterol": high_ldl,
#         "Alcohol Consumption": alcohol,
#         "Stress Level": stress,
#         "Sleep Hours": sleep_hours,
#         "Sugar Consumption": sugar,
#         "Triglyceride Level": triglycerides,
#         "Fasting Blood Sugar": fasting_sugar,
#         "CRP Level": crp,
#         "Homocysteine Level": homocysteine
#     }

#     try:

#         # ------------------------
#         # Preprocessing
#         # ------------------------

#         processed_data = preprocess_input(
#             patient_data
#         )

#         # ------------------------
#         # Prediction
#         # ------------------------

#         prediction, probability = predict_risk(
#             processed_data
#         )

#         # ------------------------
#         # Clinical Interpretation
#         # ------------------------

#         clinical_summary = interpret_patient(
#             patient_data
#         )

#         # ------------------------
#         # SHAP Explainability
#         # ------------------------

#         shap_df = get_shap_explanation(
#             processed_data
#         )

#         top_factors = get_top_risk_drivers(
#             shap_df
#         )

#         st.markdown("---")

#         # ------------------------
#         # Prediction Result
#         # ------------------------

#         st.subheader(
#             "Prediction Result"
#         )

#         if prediction == 1:

#             st.error(
#                 f"High Cardiac Risk ({probability*100:.2f}%)"
#             )

#         else:

#             st.success(
#                 f"Low Cardiac Risk ({probability*100:.2f}%)"
#             )

#         gauge_fig = create_gauge(
#             probability
#         )

#         st.plotly_chart(
#             gauge_fig,
#             use_container_width=True
#         )

#         # ------------------------
#         # Clinical Summary
#         # ------------------------

#         st.subheader(
#             "Clinical Summary"
#         )

#         for key, value in clinical_summary.items():

#             st.write(
#                 f"**{key}:** {value}"
#             )

#         # ------------------------
#         # Top Risk Drivers
#         # ------------------------

#         st.subheader(
#             "Top Risk Drivers"
#         )

#         risk_driver_df = top_factors[
#             ["Feature", "SHAP_Value"]
#         ].copy()

#         st.dataframe(
#             risk_driver_df,
#             use_container_width=True
#         )

#         # ------------------------
#         # AI Explanation
#         # ------------------------

#         st.subheader(
#             "AI Explanation"
#         )

#         explanation = explain_prediction(
#             patient_data,
#             probability,
#             top_factors,
#             clinical_summary
#         )

#         st.write(
#             explanation
#         )

#         # ------------------------
#         # Recommendations
#         # ------------------------

#         st.subheader(
#             "Personalized Recommendations"
#         )

#         recommendations = (
#             generate_recommendations(
#                 patient_data
#             )
#         )

#         for recommendation in recommendations:

#             st.write(
#                 f"• {recommendation}"
#             )

#         # ------------------------
#         # Counterfactual Analysis
#         # ------------------------

#         st.subheader(
#             "What-If Analysis"
#         )

#         counterfactual = (
#             generate_counterfactual(
#                 patient_data
#             )
#         )

#         improved_risk = (
#             counterfactual[
#                 "improved_risk"
#             ]
#         )

#         reduction = (
#             probability -
#             improved_risk
#         ) * 100

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             st.metric(
#                 "Current Risk",
#                 f"{probability*100:.1f}%"
#             )

#         with col2:

#             st.metric(
#                 "Improved Risk",
#                 f"{improved_risk*100:.1f}%"
#             )

#         with col3:

#             st.metric(
#                 "Potential Reduction",
#                 f"{reduction:.1f}%"
#             )

#         st.info(
#             """
#             This analysis estimates how risk may change if
#             modifiable risk factors such as smoking,
#             blood pressure, cholesterol,
#             BMI, and exercise habits improve.
#             """
#         )

#     except Exception as e:

#         st.error(
#             f"Error: {str(e)}"
#         )
"""
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

from ui.sidebar import render_sidebar
from ui.patient_form import render_patient_form
from ui.prediction_cards import render_prediction_cards
from ui.shap_tab import render_shap_tab
from ui.lime_tab import render_lime_tab
from ui.recommendation_tab import render_recommendation_tab
from ui.counterfactual_tab import render_counterfactual_tab
from ui.about_tab import render_about_tab

# ==========================================================
# Backend
# ==========================================================

from preprocessing.preprocess_input import preprocess_input

from model.predictor import predict_risk

from visualizations.risk_gauge import create_gauge

from services.clinical_interpreter import interpret_patient

from services.explanation_service import explain_prediction

from explainability.shap_analysis import (
    get_shap_explanation,
    get_top_risk_drivers
)

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(

    page_title=APP_TITLE,

    page_icon=APP_ICON,

    layout=LAYOUT

)

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
AI-powered Clinical Decision Support System using

Machine Learning

Explainable AI

Clinical Decision Support

Counterfactual Analysis

Google Gemini AI
"""
)

st.markdown("---")

# ==========================================================
# Patient Form
# ==========================================================

patient_data = render_patient_form()

st.markdown("---")

predict_button = st.button(

    "❤️ Predict Cardiac Risk",

    use_container_width=True

)

# ==========================================================
# Prediction
# ==========================================================

if predict_button:

    try:

        # --------------------------------------------------

        processed_data = preprocess_input(

            patient_data

        )

        # --------------------------------------------------

        prediction, probability, risk_level = predict_risk(

            processed_data

        )

        # --------------------------------------------------

        clinical_summary = interpret_patient(

            patient_data

        )

        # --------------------------------------------------
        # Compute SHAP ONLY ONCE
        # --------------------------------------------------

        shap_df = get_shap_explanation(

            processed_data

        )

        top_factors = get_top_risk_drivers(

            shap_df

        )

        # --------------------------------------------------
        # Prediction Dashboard
        # --------------------------------------------------

        render_prediction_cards(

            prediction,

            probability,

            risk_level,

            patient_data

        )

        st.markdown("---")

        st.header("❤️ Cardiac Risk Gauge")

        gauge = create_gauge(

            probability

        )

        st.plotly_chart(

            gauge,

            use_container_width=True

        )

        st.markdown("---")
        # ==========================================================
        # Dashboard Tabs
        # ==========================================================

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(

            [

                "📊 Clinical Summary",

                "🧠 SHAP",

                "🔍 LIME",

                "🤖 AI Explanation",

                "🩺 Recommendations",

                "🔄 What-If Analysis"

            ]

        )

        # ==========================================================
        # TAB 1 : Clinical Summary
        # ==========================================================

        with tab1:

            st.subheader("Patient Clinical Summary")

            if isinstance(clinical_summary, dict):

                for key, value in clinical_summary.items():

                    st.write(

                        f"**{key}:** {value}"

                    )

            else:

                st.write(clinical_summary)

        # ==========================================================
        # TAB 2 : SHAP
        # ==========================================================

        with tab2:

            st.subheader("SHAP Explainability")

            render_shap_tab(

                processed_data

            )

        # ==========================================================
        # TAB 3 : LIME
        # ==========================================================

        with tab3:

            st.subheader("LIME Explainability")

            render_lime_tab(

                processed_data

            )

        # ==========================================================
        # TAB 4 : Gemini Explanation
        # ==========================================================

        with tab4:

            st.subheader(

                "AI Clinical Explanation"

            )

            explanation = explain_prediction(

                patient_data,

                probability,

                top_factors,

                clinical_summary

            )

            st.write(

                explanation

            )

        # ==========================================================
        # TAB 5 : Recommendations
        # ==========================================================

        with tab5:

            st.subheader(

                "Personalized Recommendations"

            )

            render_recommendation_tab(

                patient_data

            )

        # ==========================================================
        # TAB 6 : Counterfactual
        # ==========================================================

        with tab6:

            st.subheader(

                "What-If Analysis"

            )

            render_counterfactual_tab(

                patient_data,

                probability

            )

        st.markdown("---")    
        
