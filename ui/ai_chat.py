"""
AI Health Assistant Chat UI
---------------------------------

Interactive AI assistant for
cardiovascular risk assessment.
"""

import streamlit as st

from services.doctor_ai import ask_doctor_ai


# ==========================================================
# Suggested Questions
# ==========================================================

def get_suggested_questions(patient):

    questions = []

    bmi = patient["Weight"] / (
        (patient["Height"] / 100) ** 2
    )

    if patient["Smoking"] == "Yes":
        questions.append("🚭 How does smoking affect my heart?")

    if patient["Systolic_BP"] >= 140:
        questions.append("❤️ How can I lower my blood pressure?")

    if bmi >= 30:
        questions.append("⚖️ How can I lose weight safely?")

    if patient["Cholesterol"] != "Normal":
        questions.append("🥗 What foods reduce cholesterol?")

    if patient["Glucose"] != "Normal":
        questions.append("🍬 How can I control my blood sugar?")

    if patient["Physical_Activity"] == "No":
        questions.append("🏃 Suggest a beginner exercise plan.")

    questions.extend([
        "📊 Explain my prediction.",
        "💊 Should I consult a doctor?"
    ])

    # Remove duplicates while preserving order
    unique = []
    for q in questions:
        if q not in unique:
            unique.append(q)

    return unique[:4]


# ==========================================================
# Main Chat UI
# ==========================================================

def render_ai_chat():

    st.subheader("💬 AI Health Assistant")

    if "patient_context" not in st.session_state:

        st.info(
            "Please generate a cardiac risk prediction first."
        )

        return

    context = st.session_state["patient_context"]

    patient = context["patient"]

    probability = context["probability"] * 100

    prediction = context["prediction"]

    # ------------------------------------------------------

    st.success(f"""
### 👨‍⚕️ Welcome!

I've already analyzed your cardiovascular assessment.

### Current Assessment

**Prediction:** {prediction}

**Estimated Risk:** {probability:.1f}%

Ask me anything about your heart health,
prediction, lifestyle or prevention.
""")

    # ------------------------------------------------------

    st.markdown("### 💡 Suggested Questions")

    questions = get_suggested_questions(patient)

    cols = st.columns(2)

    selected_question = None

    for i, question in enumerate(questions):

        with cols[i % 2]:

            if st.button(
                question,
                key=f"suggested_{i}",
                use_container_width=True
            ):

                selected_question = question

    st.divider()

    # ------------------------------------------------------
    # Chat History
    # ------------------------------------------------------

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # ------------------------------------------------------

    typed_question = st.chat_input(
        "Ask your question..."
    )

    if selected_question:

        user_question = selected_question

    else:

        user_question = typed_question

    # ------------------------------------------------------

    if user_question:

        st.session_state.chat_history.append({

            "role": "user",

            "content": user_question

        })

        with st.chat_message("user"):

            st.markdown(user_question)

        try:

            with st.spinner("Analyzing..."):
                context["chat_history"] = st.session_state.chat_history
                
                answer = ask_doctor_ai(

                    context,

                    user_question

                )

        except Exception as e:

            answer = (
                "Unable to generate a response.\n\n"
                f"{e}"
            )

        st.session_state.chat_history.append({

            "role": "assistant",

            "content": answer

        })

        with st.chat_message("assistant"):

            st.markdown(answer)

    # ------------------------------------------------------

    st.divider()

    st.caption(
        "⚠ This AI assistant provides educational information only and does not replace professional medical advice."
    )