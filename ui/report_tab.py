"""
Report Tab

Generate and download CardioAI PDF report.
"""

import streamlit as st

from reports.pdf_generator import generate_pdf


def render_report_tab(
    patient,
    prediction,
    probability,
    clinical_summary,
    recommendations,
    ai_explanation
):
    """
    Render PDF Report Download section.
    """

    st.header("📄 CardioAI Report")

    st.markdown(
        """
Generate a professional PDF report containing

- Patient Information
- Prediction Summary
- Clinical Summary
- Personalized Recommendations
- AI Clinical Explanation
"""
    )

    st.divider()

    if st.button(
        "📄 Generate PDF Report",
        use_container_width=True
    ):

        with st.spinner(
            "Generating PDF..."
        ):

            pdf = generate_pdf(

                patient,

                prediction,

                probability,

                clinical_summary,

                recommendations,

                ai_explanation

            )

        st.success(
            "Report generated successfully!"
        )

        st.download_button(

            label="⬇ Download CardioAI Report",

            data=pdf,

            file_name="CardioAI_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    st.info(
        """
The report includes:

✔ Patient Details

✔ Cardiac Risk Prediction

✔ Risk Probability

✔ Clinical Summary

✔ Recommendations

✔ AI Explanation

✔ Timestamp
"""
    )