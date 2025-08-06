#!/usr/bin/env python3
"""Debug script for router node testing"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from ..types.state import ResumeCoPilotState
from ..core.router import router_node
from ..config.llm_config import get_llm_flash

def test_router_with_sample_data():
    """Test router with sample resume and queries"""
    
    # Sample resume text
    sample_resume = """
    JOHN DOE
    Software Engineer
    
    EXPERIENCE
    Senior Software Engineer at TechCorp (2020-2023)
    - Led development of web applications using React and Node.js
    - Managed team of 5 developers and delivered 3 major projects on time
    - Improved application performance by 40% through optimization
    
    Software Engineer at StartupXYZ (2018-2020)
    - Developed REST APIs using Python and Django
    - Collaborated with cross-functional teams to deliver features
    - Reduced bug reports by 25% through improved testing practices
    
    SKILLS
    JavaScript, Python, React, Node.js, Django, Git, AWS
    """
    
    # Test queries
    test_queries = [
        "Analyze my resume for this software engineering role",
        "Generate interview questions based on my resume",
        "Rewrite this bullet point: 'Managed projects'",
        "Hello",
        "What can you do?",
        "Analyze my resume"
    ]
    
    print("🧪 Testing Router Node with Sample Data")
    print("=" * 50)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Test {i}: '{query}' ---")
        
        # Create test state
        state = ResumeCoPilotState(
            resume_text=sample_resume,
            job_description_text="Software Engineer role requiring React, Python, and team leadership",
            user_query=query,
            router_decision=None,
            analysis_report=None,
            interview_quiz=None,
            rewritten_section=None,
            conversation_history=[],
            error_message=None,
            formatted_response=None,
            think_mode=False
        )
        
        # Test router
        try:
            result_state = router_node(state)
            decision = result_state.get("router_decision", "UNKNOWN")
            error = result_state.get("error_message")
            
            print(f"Query: {query}")
            print(f"Decision: {decision}")
            if error:
                print(f"Error: {error}")
            print(f"Resume Available: {bool(result_state.get('resume_text'))}")
            print(f"JD Available: {bool(result_state.get('job_description_text'))}")
            
        except Exception as e:
            print(f"Exception: {e}")

def test_llm_directly():
    """Test LLM directly to verify connectivity"""
    print("\n🧪 Testing LLM Directly")
    print("=" * 30)
    
    try:
        llm = get_llm_flash()
        test_prompt = "You are a router. For the query 'Analyze my resume', output only ANALYZE or GREETING/INFO. Choose ANALYZE if the user wants analysis, otherwise GREETING/INFO."
        
        response = llm.invoke(test_prompt)
        print(f"LLM Response: {response.content}")
        
    except Exception as e:
        print(f"LLM Error: {e}")

def debug_router():
    """Main debug function"""
    print("🚀 Router Debug Script")
    print("=" * 30)
    
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY not set!")
    
    print("✅ API key found")
    
    # Test LLM directly
    test_llm_directly()
    
    # Test router with sample data
    test_router_with_sample_data()

if __name__ == "__main__":
    debug_router() 