import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEYAQ.Ab8RN6ICg3RIRwW51T-D8mKD-BzPrSa-zX4-2diLiz09Zi17og"))


def answer_question_with_gemini(question: str) -> str:
    """Answers a question using Gemini API."""
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {str(e)}"