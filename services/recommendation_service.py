def generate_recommendations(patient):

    recommendations = []

    if patient["Smoking"] == "Yes":
        recommendations.append(
            "Quit smoking to significantly reduce cardiovascular risk."
        )

    if patient["Blood Pressure"] > 140:
        recommendations.append(
            "Monitor blood pressure regularly and discuss management options with a healthcare professional."
        )

    if patient["Cholesterol Level"] > 240:
        recommendations.append(
            "Reduce saturated fats and maintain a heart-healthy diet."
        )

    if patient["BMI"] >= 30:
        recommendations.append(
            "Consider weight reduction through nutrition and physical activity."
        )

    if patient["Exercise Habits"] == "Low":
        recommendations.append(
            "Aim for at least 150 minutes of moderate exercise per week."
        )

    if patient["Sleep Hours"] < 6:
        recommendations.append(
            "Improve sleep habits and aim for 7–9 hours of sleep."
        )

    if patient["Stress Level"] == "High":
        recommendations.append(
            "Use stress-management techniques such as meditation or relaxation exercises."
        )

    if patient["CRP Level"] > 3:
        recommendations.append(
            "Discuss elevated inflammatory markers with a healthcare provider."
        )

    if patient["Diabetes"] == "Yes":
        recommendations.append(
            "Maintain proper blood sugar control and regular monitoring."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Maintain current healthy lifestyle habits and continue regular health checkups."
        )

    return recommendations