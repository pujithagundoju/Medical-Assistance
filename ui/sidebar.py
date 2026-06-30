"""
Sidebar Component

Displays application information
and navigation.
"""

import streamlit as st

from config import APP_TITLE


def render_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/heart-with-pulse.png",
            width=90
        )

        st.title("Cardiac AI")

        st.markdown("---")

        st.markdown(
            """
### Navigation

🏠 Dashboard

🧠 Explainability

📄 Reports

ℹ About
"""
        )

        st.markdown("---")

        st.info(

            """
This Clinical Decision Support System uses

• Random Forest

• SHAP

• LIME

• Counterfactual Analysis

• Gemini AI

to provide explainable cardiac risk assessment.
"""

        )

        st.markdown("---")

        st.success(

            "Model Status : Ready"

        )

        st.caption(

            "Version 2.0"

        )