"""
Gemini API Service

Centralized Gemini client for the entire project.
"""

import os

from dotenv import load_dotenv
from google import genai

from config import GEMINI_MODEL

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

# ==========================================================
# Initialize Gemini Client
# ==========================================================

client = genai.Client(
    api_key=API_KEY
)

# ==========================================================
# Generate Text
# ==========================================================

def generate_text(prompt):
    """
    Generate AI response using Gemini.
    """

    try:

        response = client.models.generate_content(

            model=GEMINI_MODEL,

            contents=prompt

        )

        return response.text

    except Exception as e:

        return (
            "Unable to generate AI explanation.\n\n"
            f"Reason: {str(e)}"
        )