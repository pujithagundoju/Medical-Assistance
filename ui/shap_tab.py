"""
SHAP Dashboard Component

Displays SHAP explainability
for the current prediction.
"""

import streamlit as st
import pandas as pd

from explainability.shap_analysis import (
    get_shap_explanation,
    get_top_risk_drivers
)


# ==========================================================
# SHAP TAB
# ==========================================================

def render_shap_tab(processed_data):
    """
    Display SHAP explanation.
    """

    st.header("🧠 SHAP Explainability")

    st.markdown(
        """
SHAP (SHapley Additive exPlanations) explains
how each feature contributed to the prediction.
"""
    )

    try:

        # ---------------------------------------------

        shap_df = get_shap_explanation(
            processed_data
        )

        top_features = get_top_risk_drivers(
            shap_df
        )

        # ---------------------------------------------

        st.subheader("📈 Top Risk Drivers")

        st.dataframe(
            top_features,
            use_container_width=True
        )

        # ---------------------------------------------

        positive = top_features[
            top_features["SHAP_Value"] > 0
        ]

        negative = top_features[
            top_features["SHAP_Value"] < 0
        ]

        col1, col2 = st.columns(2)

        # ---------------------------------------------

        with col1:

            st.subheader("🔺 Increased Risk")

            if len(positive) > 0:

                for _, row in positive.iterrows():

                    st.write(

                        f"• **{row['Feature']}** "
                        f"({row['SHAP_Value']:.4f})"

                    )

            else:

                st.success(
                    "No strong positive contributors."
                )

        # ---------------------------------------------

        with col2:

            st.subheader("🟢 Protective Factors")

            if len(negative) > 0:

                for _, row in negative.iterrows():

                    st.write(

                        f"• **{row['Feature']}** "
                        f"({row['SHAP_Value']:.4f})"

                    )

            else:

                st.info(
                    "No strong protective factors."
                )

        # ---------------------------------------------

        st.markdown("---")

        st.subheader("📋 Complete SHAP Values")

        st.dataframe(

            shap_df,

            use_container_width=True

        )

        # ---------------------------------------------
        # Optional Bar Chart
        # ---------------------------------------------

        st.markdown("---")

        st.subheader("📊 SHAP Contribution Chart")

        chart_df = shap_df.copy()

        chart_df = chart_df.sort_values(

            by="SHAP_Value",

            ascending=False

        )

        st.bar_chart(

            chart_df.set_index("Feature")["SHAP_Value"]

        )

    except Exception as e:

        st.error(

            f"Unable to generate SHAP explanation.\n\n{e}"

        )