"""
Recommendation Dashboard
"""

import streamlit as st

from services.recommendation_service import (
    generate_recommendations
)


def render_recommendation_tab(patient):

    recommendations = generate_recommendations(
        patient
    )

    st.subheader(
        "🩺 Personalized Recommendations"
    )

    if len(recommendations) == 0:

        st.success(
            "No recommendations generated."
        )

        return

    for rec in recommendations:

        st.write(
            f"• {rec}"
        )