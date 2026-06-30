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

        max(

            probability,

            1 - probability

        ) * 100,

        2

    )


# ==========================================================
# Percentage
# ==========================================================

def probability_to_percent(probability):

    return round(

        probability * 100,

        2

    )


# ==========================================================
# Health Score
# ==========================================================

def calculate_health_score(patient):

    score = 100

    # Smoking
    if patient["Smoking"] == "Yes":
        score -= 20

    # Exercise
    if patient["Exercise Habits"] == "Low":
        score -= 15
    elif patient["Exercise Habits"] == "Medium":
        score -= 5

    # BMI
    if patient["BMI"] >= 30:
        score -= 15
    elif patient["BMI"] >= 25:
        score -= 8

    # Blood Pressure
    if patient["Blood Pressure"] >= 140:
        score -= 15
    elif patient["Blood Pressure"] >= 120:
        score -= 8

    # Diabetes
    if patient["Diabetes"] == "Yes":
        score -= 10

    # CRP
    if patient["CRP Level"] > 3:
        score -= 8

    # Sleep
    if patient["Sleep Hours"] < 6:
        score -= 5

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

