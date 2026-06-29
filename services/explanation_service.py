# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv() 

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# def explain_prediction(
#     patient_data,
#     probability,
#     top_factors,
#     clinical_summary
# ):

#     factor_text = ""

#     for _, row in top_factors.iterrows():
#         factor_text += (
#             f"{row['Feature']} "
#             f"(Impact: {row['SHAP_Value']:.3f})\n"
#         )

#     prompt = f"""
# You are an Explainable AI Cardiac Risk Assistant.

# Patient Information:
# {patient_data}

# Clinical Summary:
# {clinical_summary}

# Predicted Cardiac Risk:
# {probability*100:.1f}%

# Top Risk Contributors:
# {factor_text}

# Generate:

# 1. Risk Overview
# 2. Why the model predicted this risk
# 3. Modifiable risk factors
# 4. Non-modifiable risk factors
# 5. Lifestyle improvement suggestions
# 6. Preventive measures
# 7. Disclaimer

# Use patient-friendly language.
# Do not diagnose disease.
# """

#     try:

#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=prompt
#         )

#         return response.text

#     except Exception as e:

#         return f"Gemini API Error:\n{e}"
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

    clinical_summary

):
    """
    Build structured prompt for Gemini.
    """

    prediction = (

        "High Cardiac Risk"

        if probability >= 0.50

        else "Low Cardiac Risk"

    )

    prompt = f"""

You are an experienced Cardiologist.

Explain the prediction using simple patient-friendly language.

Never invent information.

Always remain consistent with the prediction.

--------------------------------------------------

PATIENT INFORMATION

{patient_data}

--------------------------------------------------

CLINICAL SUMMARY

{clinical_summary}

--------------------------------------------------

PREDICTION

{prediction}

Risk Probability

{probability*100:.2f} %

--------------------------------------------------

TOP SHAP FEATURES

{shap_features.to_string(index=False)}

--------------------------------------------------

Create these sections.

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

    clinical_summary

):
    """
    Generate explanation using Gemini.
    """

    prompt = build_prompt(

        patient_data,

        probability,

        shap_features,

        clinical_summary

    )

    return generate_text(prompt)