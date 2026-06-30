"""
Recommendation Dashboard Component

Displays personalized recommendations
for the patient.
"""

import streamlit as st
import pandas as pd

from services.recommendation_service import (
    generate_recommendations
)


# ==========================================================
# Recommendation Tab
# ==========================================================

def render_recommendation_tab(patient):
    """
    Display personalized recommendations.
    """

    st.header("🩺 Personalized Recommendations")

    recommendations = generate_recommendations(patient)

    if not recommendations:

        st.success(
            "🎉 Excellent! No additional recommendations were generated."
        )
        return

    # =====================================================
    # Categorize Recommendations
    # =====================================================

    high = []
    medium = []
    low = []

    for item in recommendations:

        priority = item["Priority"]

        if priority == "High":

            high.append(item)

        elif priority == "Medium":

            medium.append(item)

        else:

            low.append(item)

    # =====================================================
    # High Priority
    # =====================================================

    if high:

        st.error("## 🔴 High Priority")

        for item in high:

            st.write(
                f"**{item['Category']}**")
            st.write(
                f"• {item['Recommendation']}"
            )

    # =====================================================
    # Medium Priority
    # =====================================================

    if medium:

        st.warning("## 🟡 Medium Priority")

        for item in medium:

            st.write(
                f"**{item['Category']}**")
            st.write(
                f"• {item['Recommendation']}"
            )

    # =====================================================
    # Low Priority
    # =====================================================

    if low:

        st.success("## 🟢 General Prevention")

        for item in low:

            st.write(
                f"**{item['Category']}**")
            st.write(
                f"• {item['Recommendation']}"
            )

    # =====================================================
    # Summary Table
    # =====================================================

    st.markdown("---")

    st.subheader("📋 Recommendation Summary")

    df = pd.DataFrame(recommendations)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # Recommendation Count
    # =====================================================

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "High Priority",
            len(high)
        )

    with col2:

        st.metric(
            "Medium Priority",
            len(medium)
        )

    with col3:

        st.metric(
            "General",
            len(low)
        )