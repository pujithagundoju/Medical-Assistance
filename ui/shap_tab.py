"""
SHAP Dashboard Component
"""

import streamlit as st

from explainability.shap_analysis import (
    get_shap_explanation,
    get_top_risk_drivers
)


def render_shap_tab(processed_data):
    """
    Display SHAP explanation.
    """

    try:

        shap_df = get_shap_explanation(processed_data)

        top_features = get_top_risk_drivers(shap_df)

        st.subheader("🧠 SHAP Explainability")

        st.write(
            """
SHAP explains how each feature influenced
the prediction for the current patient.
"""
        )

        st.dataframe(
            top_features,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("📊 SHAP Contribution Chart")

        chart = top_features.copy()

        chart = chart.sort_values(
            by="SHAP_Value",
            ascending=False
        )

        st.bar_chart(
            chart.set_index("Feature")["SHAP_Value"]
        )

        st.markdown("---")

        positive = top_features[
            top_features["SHAP_Value"] > 0
        ]

        negative = top_features[
            top_features["SHAP_Value"] < 0
        ]

        col1, col2 = st.columns(2)

        with col1:

            st.success("Factors Increasing Risk")

            if len(positive):

                for _, row in positive.iterrows():

                    st.write(
                        f"• {row['Feature']}"
                    )

        with col2:

            st.info("Protective Factors")

            if len(negative):

                for _, row in negative.iterrows():

                    st.write(
                        f"• {row['Feature']}"
                    )

    except Exception as e:

        st.error(e)