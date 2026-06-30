"""
Doctor AI Assistant

Provides intelligent cardiac health responses.
Uses Gemini when available.
Falls back to offline advice when Gemini is unavailable.
"""

from services.gemini_service import generate_text


# ==========================================================
# Offline Doctor
# ==========================================================

def offline_response(context, question):
    """
    Generate rule-based responses when Gemini
    is unavailable.
    """

    patient = context["patient"]

    prediction = context["prediction"]

    probability = context["probability"]

    summary = context["clinical_summary"]

    question = question.lower()

    # ------------------------------------------------------
    # Diet
    # ------------------------------------------------------

    if any(word in question for word in [
        "diet",
        "food",
        "eat",
        "sugar",
        "salt"
    ]):

        return f"""
## 🍎 Diet Advice

Based on your current assessment:

• Predicted Risk: **{prediction}**
• Risk Probability: **{probability*100:.2f}%**

### Recommendation

✔ Eat more fruits and vegetables.

✔ Choose whole grains.

✔ Reduce processed food.

✔ Limit sugary beverages.

✔ Reduce salt intake.

✔ Drink adequate water.

Maintain a healthy balanced diet and continue regular follow-up with your physician.
"""

    # ------------------------------------------------------
    # Exercise
    # ------------------------------------------------------

    if any(word in question for word in [
        "exercise",
        "walking",
        "gym",
        "run",
        "activity"
    ]):

        return """
## 🚶 Exercise Advice

✔ Aim for at least 150 minutes of moderate exercise every week.

✔ Walking for 30 minutes daily is beneficial.

✔ Avoid prolonged sitting.

✔ Include light strength training twice a week if medically appropriate.
"""

    # ------------------------------------------------------
    # Blood Pressure
    # ------------------------------------------------------

    if "blood pressure" in question or "bp" in question:

        return f"""
## ❤️ Blood Pressure

According to your clinical summary:

**{summary.get("Blood Pressure","Unavailable")}**

Recommendations:

✔ Reduce salt intake.

✔ Exercise regularly.

✔ Maintain healthy weight.

✔ Monitor BP regularly.

Consult your physician if blood pressure remains elevated.
"""

    # ------------------------------------------------------
    # Cholesterol
    # ------------------------------------------------------

    if "cholesterol" in question:

        return f"""
## 🩺 Cholesterol

Current Status

**{summary.get("Cholesterol","Unavailable")}**

Maintain:

✔ Healthy diet

✔ Exercise

✔ Avoid fried foods

✔ Regular lipid profile monitoring
"""

    # ------------------------------------------------------
    # BMI
    # ------------------------------------------------------

    if "bmi" in question or "weight" in question:

        return f"""
## ⚖ BMI

Current BMI Status

**{summary.get("BMI","Unavailable")}**

Maintain a healthy body weight through balanced nutrition and regular physical activity.
"""

    # ------------------------------------------------------
    # Generic Response
    # ------------------------------------------------------

    return f"""
## ❤️ General Cardiac Advice

Prediction

**{prediction}**

Risk Probability

**{probability*100:.2f}%**

Continue

✔ Healthy diet

✔ Regular exercise

✔ Blood pressure monitoring

✔ Annual health checkups

If symptoms develop, consult a cardiologist promptly.
"""


# ==========================================================
# Doctor AI
# ==========================================================

def ask_doctor_ai(context, question):
    """
    Main AI assistant.
    """

    patient = context["patient"]

    prediction = context["prediction"]

    probability = context["probability"]

    summary = context["clinical_summary"]

    factors = context["risk_factors"]

    prompt = f"""
You are an experienced cardiologist.

Patient

{patient}

Prediction

{prediction}

Risk Probability

{probability*100:.2f}%

Clinical Summary

{summary}

Top SHAP Factors

{factors}

Question

{question}

Rules

- Answer in simple language.
- Give practical advice.
- Never invent facts.
- Mention when doctor consultation is needed.
- Keep answer under 250 words.
"""

    answer = generate_text(prompt)

    # ------------------------------------------------------
    # Gemini unavailable?
    # ------------------------------------------------------

    if (

        "temporarily unavailable" in answer.lower()

        or

        "quota" in answer.lower()

        or

        "resource_exhausted" in answer.lower()

        or

        "assistant error" in answer.lower()

    ):

        return offline_response(

            context,

            question

        )

    return answer