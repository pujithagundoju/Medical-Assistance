"""
LIME Dashboard Component

Displays LIME explanation
for the current prediction.
"""

import streamlit as st
import pandas as pd

from explainability.lime_analysis import get_lime_explanation


# ==========================================================
# LIME TAB
# ==========================================================

def render_lime_tab(processed_data):
    """
    Display LIME explanation.
    """

    st.header("🔍 LIME Explainability")

    st.markdown(
        """
LIME (Local Interpretable Model-agnostic Explanations)
explains why the model made this prediction
for this specific patient.
"""
    )

    try:

        # ------------------------------------------------

        lime_df = get_lime_explanation(processed_data)

        # ------------------------------------------------

        st.subheader("📋 Feature Contributions")

        st.dataframe(

            lime_df,

            use_container_width=True

        )

        # ------------------------------------------------

        positive = lime_df[
            lime_df["Contribution"] > 0
        ]

        negative = lime_df[
            lime_df["Contribution"] < 0
        ]

        col1, col2 = st.columns(2)

        # ------------------------------------------------

        with col1:

            st.subheader("🔺 Increased Risk")

            if len(positive) > 0:

                for _, row in positive.iterrows():

                    st.write(

                        f"• **{row['Feature']}** "
                        f"({row['Contribution']:.4f})"

                    )

            else:

                st.success(
                    "No significant positive contributors."
                )

        # ------------------------------------------------

        with col2:

            st.subheader("🟢 Protective Factors")

            if len(negative) > 0:

                for _, row in negative.iterrows():

                    st.write(

                        f"• **{row['Feature']}** "
                        f"({row['Contribution']:.4f})"

                    )

            else:

                st.info(
                    "No significant protective factors."
                )

        # ------------------------------------------------

        st.markdown("---")

        st.subheader("📊 LIME Contribution Chart")

        chart_df = lime_df.copy()

        chart_df = chart_df.sort_values(

            by="Contribution",

            ascending=False

        )

        st.bar_chart(

            chart_df.set_index("Feature")["Contribution"]

        )

        # ------------------------------------------------

        st.markdown("---")

        st.info(
            """
LIME explains **only this prediction**.

Unlike SHAP, which measures global feature
importance, LIME focuses on the local behavior
around the current patient.
"""
        )

    except Exception as e:

        st.error(

            f"Unable to generate LIME explanation.\n\n{e}"

        )