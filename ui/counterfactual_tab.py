"""
Counterfactual Dashboard Component

Displays the estimated improvement in
cardiac risk after modifying lifestyle
risk factors.
"""

import streamlit as st

from services.counterfactual_service import (
    generate_counterfactual
)

from utils import (
    probability_to_percent
)


# ==========================================================
# Counterfactual Tab
# ==========================================================

def render_counterfactual_tab(patient, current_probability):
    """
    Display counterfactual analysis.
    """

    st.header("🔄 What-If Analysis")

    st.markdown(
        """
This analysis estimates how your cardiac
risk may change after improving
modifiable lifestyle factors.
"""
    )

    try:

        result = generate_counterfactual(patient)

        improved_probability = result["improved_risk"]

        reduction = current_probability - improved_probability

        current_percent = probability_to_percent(
            current_probability
        )

        improved_percent = probability_to_percent(
            improved_probability
        )

        reduction_percent = probability_to_percent(
            reduction
        )

        # =====================================================
        # Metrics
        # =====================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Current Risk",

                f"{current_percent:.2f}%"

            )

        with col2:

            st.metric(

                "Improved Risk",

                f"{improved_percent:.2f}%"

            )

        with col3:

            st.metric(

                "Potential Reduction",

                f"{reduction_percent:.2f}%"

            )

        # =====================================================
        # Lifestyle Improvements
        # =====================================================

        st.markdown("---")

        st.subheader("✅ Suggested Lifestyle Changes")

        improvements = [

            "🚭 Quit Smoking",

            "🏃 Exercise Regularly",

            "⚖ Maintain Healthy BMI",

            "🩺 Control Blood Pressure",

            "🥗 Improve Diet",

            "🍎 Reduce Sugar Intake",

            "😴 Sleep 7-8 Hours Daily",

            "🧘 Reduce Stress",

            "❤️ Improve Cholesterol Levels"

        ]

        for item in improvements:

            st.write(f"• {item}")

        # =====================================================
        # Interpretation
        # =====================================================

        st.markdown("---")

        if reduction > 0.20:

            st.success(
                "Excellent improvement is possible with lifestyle modification."
            )

        elif reduction > 0.10:

            st.info(
                "Moderate improvement is achievable by addressing key risk factors."
            )

        elif reduction > 0:

            st.warning(
                "Small improvement is expected. Continue healthy lifestyle practices."
            )

        else:

            st.error(
                "No significant reduction was estimated by the model."
            )

        # =====================================================
        # Disclaimer
        # =====================================================

        st.markdown("---")

        st.caption(
            """
This is a model-based simulation and does not
guarantee future clinical outcomes.

Always consult a qualified healthcare professional
before making medical decisions.
"""
        )

    except Exception as e:

        st.error(
            f"Unable to generate counterfactual analysis.\n\n{e}"
        )