
# """
# Explanation Service

# Creates structured prompts
# and requests explanations
# from Gemini.
# """

# from services.gemini_service import generate_text


# def build_prompt(

#     patient_data,

#     probability,

#     shap_features,

#     clinical_summary

# ):
#     """
#     Build structured prompt for Gemini.
#     """

#     prediction = (

#         "High Cardiac Risk"

#         if probability >= 0.50

#         else "Low Cardiac Risk"

#     )

#     prompt = f"""

# You are an experienced Cardiologist.

# Explain the prediction using simple patient-friendly language.

# Never invent information.

# Always remain consistent with the prediction.

# --------------------------------------------------

# PATIENT INFORMATION

# {patient_data}

# --------------------------------------------------

# CLINICAL SUMMARY

# {clinical_summary}

# --------------------------------------------------

# PREDICTION

# {prediction}

# Risk Probability

# {probability*100:.2f} %

# --------------------------------------------------

# TOP SHAP FEATURES

# {shap_features.to_string(index=False)}

# --------------------------------------------------

# Create these sections.

# 1. Risk Overview

# 2. Why the AI predicted this risk

# 3. Modifiable Risk Factors

# 4. Non-Modifiable Risk Factors

# 5. Lifestyle Improvement Suggestions

# 6. Preventive Measures

# 7. Disclaimer

# """

#     return prompt


# def explain_prediction(

#     patient_data,

#     probability,

#     shap_features,

#     clinical_summary

# ):
#     """
#     Generate explanation using Gemini.
#     """

#     prompt = build_prompt(

#         patient_data,

#         probability,

#         shap_features,

#         clinical_summary

#     )

#     return generate_text(prompt)
"""
Explanation Service

Creates structured prompts
and requests explanations
from Gemini.
"""

from services.gemini_service import generate_text


def build_prompt(
    patient_data,
    probability,
    shap_features,
    clinical_summary,
):
    """
    Build structured prompt for Gemini.
    """

    prediction = (
        "High Cardiac Risk"
        if probability >= 0.50
        else "Low Cardiac Risk"
    )

    # Handle missing SHAP gracefully
    if shap_features is None:
        shap_text = "SHAP explanation was not available."
    else:
        try:
            shap_text = shap_features.to_string(index=False)
        except Exception:
            shap_text = str(shap_features)

    prompt = f"""
You are an experienced Cardiologist.

Explain the prediction using simple, patient-friendly language.

Only use the information provided below.

Do NOT invent any diagnoses or clinical findings.

Remain consistent with the prediction.

--------------------------------------------------

PATIENT INFORMATION

{patient_data}

--------------------------------------------------

CLINICAL SUMMARY

{clinical_summary}

--------------------------------------------------

PREDICTION

{prediction}

Estimated Risk Probability

{probability*100:.2f}%

--------------------------------------------------

IMPORTANT RISK FACTORS

{shap_text}

--------------------------------------------------

Provide the explanation using the following headings:

1. Risk Overview

2. Why the AI predicted this risk

3. Modifiable Risk Factors

4. Non-Modifiable Risk Factors

5. Lifestyle Improvement Suggestions

6. Preventive Measures

7. Disclaimer
"""

    return prompt


def explain_prediction(
    patient_data,
    probability,
    shap_features,
    clinical_summary,
):
    """
    Generate explanation using Gemini.
    """

    try:

        prompt = build_prompt(
            patient_data,
            probability,
            shap_features,
            clinical_summary,
        )

        response = generate_text(prompt)

        if response is None:
            return (
                "AI explanation is currently unavailable."
            )

        if isinstance(response, str):

            response = response.strip()

            if response:
                return response

        return (
            "AI explanation is currently unavailable."
        )

    except Exception as e:

        return (
            "⚠ AI explanation could not be generated.\n\n"
            f"Reason: {e}"
        )