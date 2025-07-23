import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    return ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.2, google_api_key=api_key)
