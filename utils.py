"""
Utility Functions

Reusable helper functions
used throughout the project.
"""

from config import *


# ==========================================================
# Risk Category
# ==========================================================

def get_risk_category(probability):

    if probability < VERY_LOW:
        return "Very Low"

    elif probability < LOW:
        return "Low"

    elif probability < MODERATE:
        return "Moderate"

    elif probability < HIGH:
        return "High"

    return "Very High"


# ==========================================================
# Risk Color
# ==========================================================

def get_risk_color(probability):

    if probability < VERY_LOW:
        return LOW_COLOR

    elif probability < LOW:
        return LOW_COLOR

    elif probability < MODERATE:
        return MEDIUM_COLOR

    elif probability < HIGH:
        return HIGH_COLOR

    return VERY_HIGH_COLOR


# ==========================================================
# Confidence
# ==========================================================

def calculate_confidence(probability):

    return round(
        max(probability, 1 - probability) * 100,
        2
    )


# ==========================================================
# Probability to Percentage
# ==========================================================

def probability_to_percent(probability):

    return round(probability * 100, 2)


# ==========================================================
# Health Score
# ==========================================================

def calculate_health_score(patient):
    """
    Calculate a simple health score
    for the Kaggle cardiovascular dataset.
    """

    score = 100

    # ------------------------------------
    # BMI
    # ------------------------------------

    bmi = patient["Weight"] / (
        (patient["Height"] / 100) ** 2
    )

    if bmi >= 30:
        score -= 15

    elif bmi >= 25:
        score -= 8

    # ------------------------------------
    # Smoking
    # ------------------------------------

    if patient["Smoking"] == "Yes":
        score -= 20

    # ------------------------------------
    # Alcohol
    # ------------------------------------

    if patient["Alcohol"] == "Yes":
        score -= 10

    # ------------------------------------
    # Physical Activity
    # ------------------------------------

    if patient["Physical_Activity"] == "No":
        score -= 15

    # ------------------------------------
    # Blood Pressure
    # ------------------------------------

    if patient["Systolic_BP"] >= 140:
        score -= 15

    elif patient["Systolic_BP"] >= 120:
        score -= 8

    # ------------------------------------
    # Cholesterol
    # ------------------------------------

    if patient["Cholesterol"] == "Well Above Normal":
        score -= 12

    elif patient["Cholesterol"] == "Above Normal":
        score -= 6

    # ------------------------------------
    # Glucose
    # ------------------------------------

    if patient["Glucose"] == "Well Above Normal":
        score -= 12

    elif patient["Glucose"] == "Above Normal":
        score -= 6

    score = max(score, 0)

    return score


# ==========================================================
# Health Status
# ==========================================================

def health_status(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 60:
        return "Fair"

    elif score >= 40:
        return "Needs Improvement"

    return "High Attention Required"