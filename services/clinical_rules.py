"""
Clinical interpretation rules for patient measurements.
"""

def age_category(age):
    if age < 30:
        return "Young Adult"
    elif age < 45:
        return "Adult"
    elif age < 60:
        return "Middle-aged"
    else:
        return "Senior"


def blood_pressure_category(bp):
    if bp < 120:
        return "Normal"
    elif bp < 130:
        return "Elevated"
    elif bp < 140:
        return "Stage 1 Hypertension"
    else:
        return "Stage 2 Hypertension"


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def crp_category(crp):
    if crp < 1:
        return "Low Cardiovascular Inflammation"
    elif crp <= 3:
        return "Moderate Cardiovascular Inflammation"
    else:
        return "High Cardiovascular Inflammation"


def homocysteine_category(value):
    if value < 15:
        return "Normal"
    elif value < 30:
        return "Moderately Elevated"
    else:
        return "High"


def sleep_category(hours):
    if hours < 6:
        return "Poor"
    elif hours <= 9:
        return "Healthy"
    else:
        return "Excessive"


def cholesterol_category(total):
    if total < 200:
        return "Normal"
    elif total < 240:
        return "Borderline High"
    else:
        return "High"


def generate_clinical_summary(patient):
    """
    Converts patient measurements into
    clinician-friendly interpretations.
    """

    return {

        "Age Group":
            age_category(patient["Age"]),

        "Blood Pressure":
            blood_pressure_category(patient["Blood Pressure"]),

        "Cholesterol":
            cholesterol_category(patient["Cholesterol Level"]),

        "BMI":
            bmi_category(patient["BMI"]),

        "CRP":
            crp_category(patient["CRP Level"]),

        "Homocysteine":
            homocysteine_category(patient["Homocysteine Level"]),

        "Sleep":
            sleep_category(patient["Sleep Hours"])

    }