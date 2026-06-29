"""
Gemini API Service

Centralized Gemini client for the entire project.
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )

client = genai.Client(
    api_key=API_KEY
)


def generate_text(prompt):
    """
    Generate response from Gemini.
    """

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return (
            "Unable to generate AI explanation.\n\n"
            f"Reason: {e}"
        )