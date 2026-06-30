"""
Prediction Cards Component

Displays prediction results in
professional dashboard cards.
"""

import streamlit as st

from utils import (
    probability_to_percent,
    calculate_confidence,
    calculate_health_score
)


# ==========================================================
# Risk Badge
# ==========================================================

def risk_badge(risk_level):

    colors = {

        "Very Low": "🟢",

        "Low": "🟢",

        "Moderate": "🟡",

        "High": "🟠",

        "Very High": "🔴"

    }

    return f"{colors.get(risk_level, '⚪')} {risk_level}"


# ==========================================================
# Prediction Dashboard
# ==========================================================

def render_prediction_cards(
    prediction,
    probability,
    risk_level,
    patient
):
    """
    Display prediction dashboard.
    """

    probability_percent = probability_to_percent(probability)

    confidence = calculate_confidence(probability)

    health_score = calculate_health_score(patient)

    st.markdown("---")

    st.header("📊 Prediction Summary")

    col1, col2, col3, col4 = st.columns(4)

    # -----------------------------------------

    with col1:

        st.metric(

            "Risk Level",

            risk_badge(risk_level)

        )

    # -----------------------------------------

    with col2:

        st.metric(

            "Probability",

            f"{probability_percent:.2f}%"

        )

    # -----------------------------------------

    with col3:

        st.metric(

            "Model Confidence",

            f"{confidence:.2f}%"

        )

    # -----------------------------------------

    with col4:

        st.metric(

            "Health Score",

            f"{health_score}/100"

        )

    # =====================================================
    # Prediction Banner
    # =====================================================

    st.markdown("")

    if prediction == 1:

        st.error(

            f"""
### ❤️ High Cardiac Risk Detected

Estimated probability:

**{probability_percent:.2f}%**

Please consult a qualified healthcare professional.
"""

        )

    else:

        st.success(

            f"""
### 💚 Low Cardiac Risk

Estimated probability:

**{probability_percent:.2f}%**

Maintain healthy lifestyle habits.
"""

        )

    # =====================================================
    # Health Score Interpretation
    # =====================================================

    st.markdown("")

    if health_score >= 90:

        st.success("🌟 Excellent overall health profile.")

    elif health_score >= 75:

        st.info("✅ Good overall health profile.")

    elif health_score >= 60:

        st.warning(
            "⚠ Some lifestyle improvements are recommended."
        )

    else:

        st.error(
            "🚨 Multiple cardiovascular risk factors detected."
        )