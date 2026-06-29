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

Generates personalized recommendations
based on patient information.
"""


def generate_recommendations(patient):

    recommendations = []

    # =====================================================
    # Smoking
    # =====================================================

    if patient["Smoking"] == "Yes":

        recommendations.append({

            "Priority": "High",

            "Category": "Lifestyle",

            "Recommendation":
            "Quit smoking immediately. Smoking is one of the strongest risk factors for cardiovascular disease."

        })

    # =====================================================
    # Exercise
    # =====================================================

    if patient["Exercise Habits"] == "Low":

        recommendations.append({

            "Priority": "High",

            "Category": "Lifestyle",

            "Recommendation":
            "Aim for at least 150 minutes of moderate exercise each week."

        })

    elif patient["Exercise Habits"] == "Medium":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Lifestyle",

            "Recommendation":
            "Increase physical activity to improve cardiovascular fitness."

        })

    # =====================================================
    # BMI
    # =====================================================

    if patient["BMI"] >= 30:

        recommendations.append({

            "Priority": "High",

            "Category": "Weight",

            "Recommendation":
            "Work towards gradual weight reduction through healthy eating and regular exercise."

        })

    elif patient["BMI"] >= 25:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Weight",

            "Recommendation":
            "Maintain a healthy diet and increase activity to achieve a normal BMI."

        })

    # =====================================================
    # Blood Pressure
    # =====================================================

    if patient["Blood Pressure"] >= 140:

        recommendations.append({

            "Priority": "High",

            "Category": "Medical",

            "Recommendation":
            "Consult your physician for blood pressure management and monitor it regularly."

        })

    elif patient["Blood Pressure"] >= 120:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Medical",

            "Recommendation":
            "Monitor your blood pressure regularly and reduce salt intake."

        })

    # =====================================================
    # Diabetes
    # =====================================================

    if patient["Diabetes"] == "Yes":

        recommendations.append({

            "Priority": "High",

            "Category": "Medical",

            "Recommendation":
            "Maintain proper blood sugar control through medication, diet and exercise."

        })

    # =====================================================
    # High LDL
    # =====================================================

    if patient["High LDL Cholesterol"] == "Yes":

        recommendations.append({

            "Priority": "High",

            "Category": "Diet",

            "Recommendation":
            "Reduce saturated fats and increase dietary fiber to lower LDL cholesterol."

        })

    # =====================================================
    # Low HDL
    # =====================================================

    if patient["Low HDL Cholesterol"] == "Yes":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Diet",

            "Recommendation":
            "Increase HDL cholesterol by regular exercise, healthy fats, and maintaining a healthy weight."

        })

    # =====================================================
    # Sugar
    # =====================================================

    if patient["Sugar Consumption"] == "High":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Diet",

            "Recommendation":
            "Reduce added sugar and sugary beverages."

        })

    # =====================================================
    # Alcohol
    # =====================================================

    if patient["Alcohol Consumption"] == "High":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Lifestyle",

            "Recommendation":
            "Reduce alcohol intake to recommended limits."

        })

    # =====================================================
    # Stress
    # =====================================================

    if patient["Stress Level"] == "High":

        recommendations.append({

            "Priority": "Medium",

            "Category": "Lifestyle",

            "Recommendation":
            "Practice stress management techniques such as meditation, yoga, or deep breathing."

        })

    # =====================================================
    # Sleep
    # =====================================================

    if patient["Sleep Hours"] < 6:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Lifestyle",

            "Recommendation":
            "Aim for 7–9 hours of quality sleep every night."

        })

    # =====================================================
    # CRP
    # =====================================================

    if patient["CRP Level"] > 3:

        recommendations.append({

            "Priority": "Medium",

            "Category": "Medical",

            "Recommendation":
            "Discuss elevated inflammation markers with your physician."

        })

    # =====================================================
    # General Prevention
    # =====================================================

    recommendations.append({

        "Priority": "Low",

        "Category": "Monitoring",

        "Recommendation":
        "Schedule regular health check-ups and monitor blood pressure, blood sugar, and cholesterol."

    })

    # =====================================================
    # Remove duplicates
    # =====================================================

    unique = []

    seen = set()

    for item in recommendations:

        if item["Recommendation"] not in seen:

            unique.append(item)

            seen.add(item["Recommendation"])

    priority_order = {

        "High": 0,

        "Medium": 1,

        "Low": 2

    }

    unique.sort(

        key=lambda x: priority_order[x["Priority"]]

    )

    return unique