import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm_flash():
    """Get Gemini Flash LLM for routing (fast)"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=api_key
    )

def get_llm_pro():
    """Get Gemini Pro LLM for complex tasks (high quality)"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.7,
        google_api_key=api_key
    )

def get_llm_pro_streaming():
    """Get Gemini Pro LLM with streaming enabled"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.7,
        google_api_key=api_key,
        streaming=True
    ) 