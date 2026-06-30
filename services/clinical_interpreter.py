# # services/clinical_interpreter.py

# def interpret_patient(patient):

#     summary = {}

#     # Blood Pressure
#     bp = patient["Blood Pressure"]

#     if bp < 120:
#         summary["Blood Pressure"] = "Normal"

#     elif bp < 140:
#         summary["Blood Pressure"] = "Elevated"

#     elif bp < 160:
#         summary["Blood Pressure"] = "Stage 1 Hypertension"

#     else:
#         summary["Blood Pressure"] = "Stage 2 Hypertension"

#     # Cholesterol

#     chol = patient["Cholesterol Level"]

#     if chol < 200:
#         summary["Cholesterol"] = "Normal"

#     elif chol < 240:
#         summary["Cholesterol"] = "Borderline High"

#     else:
#         summary["Cholesterol"] = "High"

#     # BMI

#     bmi = patient["BMI"]

#     if bmi < 18.5:
#         summary["BMI"] = "Underweight"

#     elif bmi < 25:
#         summary["BMI"] = "Normal"

#     elif bmi < 30:
#         summary["BMI"] = "Overweight"

#     else:
#         summary["BMI"] = "Obese"

#     # CRP

#     crp = patient["CRP Level"]

#     if crp < 1:
#         summary["CRP"] = "Low Cardiovascular Inflammation"

#     elif crp < 3:
#         summary["CRP"] = "Moderate Cardiovascular Inflammation"

#     else:
#         summary["CRP"] = "High Cardiovascular Inflammation"

#     # Homocysteine

#     hcy = patient["Homocysteine Level"]

#     if hcy < 15:
#         summary["Homocysteine"] = "Normal"

#     else:
#         summary["Homocysteine"] = "Elevated"

#     # Sleep

#     sleep = patient["Sleep Hours"]

#     if sleep < 6:
#         summary["Sleep"] = "Insufficient"

#     elif sleep <= 9:
#         summary["Sleep"] = "Healthy"

#     else:
#         summary["Sleep"] = "Excessive"

#     return summary
# services/clinical_interpreter.py
"""
Clinical Interpreter

Generates a simple clinical summary
for the patient's cardiovascular profile.
"""


def interpret_patient(patient):
    """
    Generate clinical interpretation.
    """

    summary = {}

    # =====================================================
    # Blood Pressure
    # =====================================================

    systolic = patient["Systolic_BP"]
    diastolic = patient["Diastolic_BP"]

    if systolic < 120 and diastolic < 80:
        summary["Blood Pressure"] = "Normal"

    elif systolic < 130 and diastolic < 80:
        summary["Blood Pressure"] = "Elevated"

    elif systolic < 140 or diastolic < 90:
        summary["Blood Pressure"] = "Stage 1 Hypertension"

    else:
        summary["Blood Pressure"] = "Stage 2 Hypertension"

    # =====================================================
    # BMI
    # =====================================================

    bmi = patient["Weight"] / (
        (patient["Height"] / 100) ** 2
    )

    if bmi < 18.5:
        summary["BMI"] = "Underweight"

    elif bmi < 25:
        summary["BMI"] = "Normal"

    elif bmi < 30:
        summary["BMI"] = "Overweight"

    else:
        summary["BMI"] = "Obese"

    # =====================================================
    # Cholesterol
    # =====================================================

    chol = patient["Cholesterol"]

    if chol == "Normal":
        summary["Cholesterol"] = "Normal"

    elif chol == "Above Normal":
        summary["Cholesterol"] = "Above Normal"

    else:
        summary["Cholesterol"] = "Well Above Normal"

    # =====================================================
    # Glucose
    # =====================================================

    glucose = patient["Glucose"]

    if glucose == "Normal":
        summary["Glucose"] = "Normal"

    elif glucose == "Above Normal":
        summary["Glucose"] = "Above Normal"

    else:
        summary["Glucose"] = "Well Above Normal"

    # =====================================================
    # Smoking
    # =====================================================

    summary["Smoking"] = (
        "Smoker"
        if patient["Smoking"] == "Yes"
        else "Non-Smoker"
    )

    # =====================================================
    # Alcohol
    # =====================================================

    summary["Alcohol"] = (
        "Consumes Alcohol"
        if patient["Alcohol"] == "Yes"
        else "No Alcohol Consumption"
    )

    # =====================================================
    # Physical Activity
    # =====================================================

    summary["Physical Activity"] = (
        "Physically Active"
        if patient["Physical_Activity"] == "Yes"
        else "Physically Inactive"
    )

    return summary


# =====================================================
# Wrapper
# =====================================================

def generate_clinical_summary(patient):
    return interpret_patient(patient)