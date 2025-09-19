import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")  # or GEMINI_API_KEY, whichever you set

if not API_KEY:
    raise ValueError("Google API key not found. Make sure .env has GOOGLE_API_KEY set.")

import google.generativeai as genai
genai.configure(api_key=API_KEY)


def aiProcess(command: str):
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Instead of system role, prepend context to user’s prompt
    prompt = (
        "You are a virtual assistant named Jarvis. "
        "Give short, precise answers like Alexa or Google Assistant.\n\n"
        f"User: {command}"
    )

    response = model.generate_content(
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )

    # Safely extract response
    if response and response.candidates:
        return response.candidates[0].content.parts[0].text
    else:
        return "Sorry, I couldn't generate a response."
