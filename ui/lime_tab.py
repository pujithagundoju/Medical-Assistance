"""
LIME Dashboard Component
"""

import streamlit as st

from explainability.lime_analysis import (
    get_lime_explanation
)


def render_lime_tab(processed_data):

    st.subheader("🔍 LIME Explainability")

    try:

        lime_df = get_lime_explanation(
            processed_data
        )

        st.dataframe(
            lime_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.bar_chart(
            lime_df.set_index("Feature")[
                "Contribution"
            ]
        )

        st.info(
            """
LIME explains why this
individual patient received
the current prediction.
"""
        )

    except Exception as e:

        st.error(e)