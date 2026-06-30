# def generate_recommendations(patient):

#     recommendations = []

#     if patient["Smoking"] == "Yes":
#         recommendations.append(
#             "Quit smoking to significantly reduce cardiovascular risk."
#         )

#     if patient["Blood Pressure"] > 140:
#         recommendations.append(
#             "Monitor blood pressure regularly and discuss management options with a healthcare professional."
#         )

#     if patient["Cholesterol Level"] > 240:
#         recommendations.append(
#             "Reduce saturated fats and maintain a heart-healthy diet."
#         )

#     if patient["BMI"] >= 30:
#         recommendations.append(
#             "Consider weight reduction through nutrition and physical activity."
#         )

#     if patient["Exercise Habits"] == "Low":
#         recommendations.append(
#             "Aim for at least 150 minutes of moderate exercise per week."
#         )

#     if patient["Sleep Hours"] < 6:
#         recommendations.append(
#             "Improve sleep habits and aim for 7–9 hours of sleep."
#         )

#     if patient["Stress Level"] == "High":
#         recommendations.append(
#             "Use stress-management techniques such as meditation or relaxation exercises."
#         )

#     if patient["CRP Level"] > 3:
#         recommendations.append(
#             "Discuss elevated inflammatory markers with a healthcare provider."
#         )

#     if patient["Diabetes"] == "Yes":
#         recommendations.append(
#             "Maintain proper blood sugar control and regular monitoring."
#         )

#     if len(recommendations) == 0:
#         recommendations.append(
#             "Maintain current healthy lifestyle habits and continue regular health checkups."
#         )

#     return recommendations
"""
Recommendation Service

Generate personalized recommendations
for the Kaggle Cardiovascular Dataset.
"""


def generate_recommendations(patient):

    recommendations = []

    # ==========================================
    # BMI
    # ==========================================

    bmi = patient["Weight"] / (
        (patient["Height"] / 100) ** 2
    )

    if bmi >= 30:

        recommendations.append({

            "Priority": "High",

            "Category": "Weight",

            "Recommendation":
            "Reduce body weight through a balanced diet and regular physical activity."

        })

    elif bmi >= 25:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Weight",

            "Recommendation":
            "Maintain a healthy diet and increase physical activity to reach a normal BMI."

        })

    # ==========================================
    # Blood Pressure
    # ==========================================

    if patient["Systolic_BP"] >= 140:

        recommendations.append({

            "Priority": "High",

            "Category": "Blood Pressure",

            "Recommendation":
            "Consult your physician regarding blood pressure control and monitor it regularly."

        })

    elif patient["Systolic_BP"] >= 120:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Blood Pressure",

            "Recommendation":
            "Reduce salt intake and monitor blood pressure regularly."

        })

    # ==========================================
    # Cholesterol
    # ==========================================

    if patient["Cholesterol"] == "Well Above Normal":

        recommendations.append({

            "Priority": "High",

            "Category": "Diet",

            "Recommendation":
            "Reduce saturated fats and increase fruits, vegetables and whole grains."

        })

    elif patient["Cholesterol"] == "Above Normal":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Diet",

            "Recommendation":
            "Follow a heart-healthy diet to improve cholesterol levels."

        })

    # ==========================================
    # Glucose
    # ==========================================

    if patient["Glucose"] == "Well Above Normal":

        recommendations.append({

            "Priority": "High",

            "Category": "Medical",

            "Recommendation":
            "Consult your physician for blood glucose evaluation."

        })

    elif patient["Glucose"] == "Above Normal":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Medical",

            "Recommendation":
            "Limit sugar intake and monitor blood glucose levels."

        })

    # ==========================================
    # Smoking
    # ==========================================

    if patient["Smoking"] == "Yes":

        recommendations.append({

            "Priority": "High",

            "Category": "Lifestyle",

            "Recommendation":
            "Quit smoking. Smoking significantly increases cardiovascular risk."

        })

    # ==========================================
    # Alcohol
    # ==========================================

    if patient["Alcohol"] == "Yes":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Lifestyle",

            "Recommendation":
            "Reduce alcohol consumption to recommended limits."

        })

    # ==========================================
    # Physical Activity
    # ==========================================

    if patient["Physical_Activity"] == "No":

        recommendations.append({

            "Priority": "High",

            "Category": "Exercise",

            "Recommendation":
            "Aim for at least 150 minutes of moderate exercise every week."

        })

    # ==========================================
    # General Recommendation
    # ==========================================

    recommendations.append({

        "Priority": "Low",

        "Category": "Monitoring",

        "Recommendation":
        "Schedule regular cardiovascular health check-ups."

    })

    # ==========================================
    # Remove duplicates
    # ==========================================

    unique = []

    seen = set()

    for item in recommendations:

        if item["Recommendation"] not in seen:

            unique.append(item)

            seen.add(item["Recommendation"])

    priority = {

        "High": 0,

        "Medium": 1,

        "Low": 2

    }

    unique.sort(

        key=lambda x: priority[x["Priority"]]

    )

    return unique