#!/usr/bin/env python3
"""
Test script for Gemini LLM integration
Run this to verify your API key and LLM setup is working
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

def test_gemini_integration():
    """Test both Gemini Flash and Pro models"""
    
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY environment variable not set!")
        print("Please set your API key:")
        print("Windows: set GOOGLE_API_KEY=your_api_key_here")
        print("macOS/Linux: export GOOGLE_API_KEY=your_api_key_here")
        return False
    
    print("✅ API key found")
    
    try:
        # Test Gemini Flash
        print("\n🧪 Testing Gemini Flash (for routing)...")
        llm_flash = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2,
            google_api_key=api_key
        )
        
        flash_response = llm_flash.invoke("Say 'Hello' in one word.")
        print(f"Flash Response: {flash_response.content}")
        
        # Test Gemini Pro
        print("\n🧪 Testing Gemini Pro (for analysis)...")
        llm_pro = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=0.7,
            google_api_key=api_key
        )
        
        pro_response = llm_pro.invoke("What is 2+2? Answer in one sentence.")
        print(f"Pro Response: {pro_response.content}")
        
        print("\n✅ Gemini integration successful!")
        print("You can now run the Resume AI Co-Pilot with real LLM responses.")
        return True
        
    except Exception as e:
        print(f"❌ Gemini integration failed: {e}")
        print("Please check your API key and internet connection.")
        return False

def test_gemini():
    """Main test function"""
    print("🚀 Testing Gemini LLM Integration for Resume AI Co-Pilot")
    print("=" * 60)
    
    success = test_gemini_integration()
    
    if success:
        print("\n🎉 Ready to run: streamlit run streamlit_app.py")
    else:
        print("\n⚠️  Please fix the issues above before running the main app")

if __name__ == "__main__":
    test_gemini() 