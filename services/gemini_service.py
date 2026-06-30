"""
Gemini API Service

Centralized Gemini client
for the entire project.
"""

import os

from dotenv import load_dotenv
from google import genai

from config import GEMINI_MODEL


# ==========================================================
# Load Environment
# ==========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:

    raise ValueError(

        "GEMINI_API_KEY not found in .env"

    )

# ==========================================================
# Gemini Client
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

    # ------------------------------------------------------
    # Quota Exceeded
    # ------------------------------------------------------

    except Exception as e:

        error = str(e)

        if "429" in error or "RESOURCE_EXHAUSTED" in error:

            return """

## ⚠ AI Assistant Temporarily Unavailable

Google Gemini free API quota has been reached.

### What happened?

The daily or per-minute request limit for the
free Gemini API has been exceeded.

### Possible Solutions

• Wait a few minutes and try again.

• Create another Gemini API Key.

• Upgrade to a paid Gemini API plan.

### Meanwhile

You can still use

✅ Prediction

✅ SHAP

✅ LIME

✅ Recommendations

✅ Counterfactual Analysis

without any interruption.
"""

        # --------------------------------------------------
        # Invalid API Key
        # --------------------------------------------------

        if "API_KEY" in error or "401" in error:

            return """

## ❌ Invalid Gemini API Key

The configured API key is invalid.

Please verify your .env file.

"""

        # --------------------------------------------------
        # Internet Error
        # --------------------------------------------------

        if (

            "Connection" in error

            or

            "Timeout" in error

        ):

            return """

## 🌐 Network Error

Unable to connect to Gemini servers.

Please check your internet connection.

"""

        # --------------------------------------------------
        # Unknown Error
        # --------------------------------------------------

        return f"""

## ⚠ AI Assistant Error

An unexpected error occurred.

Reason

{error}

"""