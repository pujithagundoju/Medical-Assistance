"""
Counterfactual Dashboard
"""

import streamlit as st

from services.counterfactual_service import (
    generate_counterfactual
)


def render_counterfactual_tab(
    patient,
    probability
):

    st.subheader(
        "🔄 What-If Analysis"
    )

    result = generate_counterfactual(
        patient
    )

    improved = result["improved_risk"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Risk",
            f"{probability*100:.1f}%"
        )

    with col2:

        st.metric(
            "Improved Risk",
            f"{improved*100:.1f}%"
        )

    st.info(
        """
Improving lifestyle
factors may reduce
future cardiovascular risk.
"""
    )