from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro
from ..prompts.router_prompts import get_router_prompt

def router_node(state: ResumeCoPilotState):
    """
    Classify user intent and direct workflow. Update router_decision in state.
    Uses Gemini-2.5-flash for fast routing or Gemini-2.5-pro based on think_mode.
    """
    try:
        # Choose LLM based on think_mode
        think_mode = state.get("think_mode", False)
        if think_mode:
            llm = get_llm_pro()  # High-quality for thinking mode
        else:
            llm = get_llm_flash()  # Fast for normal mode
            
        user_query = state.get("user_query", "")
        resume_available = bool(state.get("resume_text"))
        jd_available = bool(state.get("job_description_text"))
        
        # Get recent conversation history for context
        conversation_history = state.get("conversation_history", [])
        recent_context = ""
        if len(conversation_history) > 2:
            # Get last 2 exchanges for context
            recent_exchanges = conversation_history[-4:]  # Last 4 messages (2 exchanges)
            recent_context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_exchanges])
        
        print(f"🔍 Router Debug - Query: '{user_query}'")
        print(f"🔍 Router Debug - Resume Available: {resume_available}")
        print(f"🔍 Router Debug - JD Available: {jd_available}")
        print(f"🔍 Router Debug - Think Mode: {think_mode}")
        print(f"🔍 Router Debug - Recent Context: {recent_context[:100]}...")
        
        # Check for follow-up questions
        follow_up_indicators = [
            "regarding", "about", "concerning", "related to", "from", "of", "the", "that", "this",
            "question", "answer", "response", "previous", "above", "before", "earlier"
        ]
        
        is_follow_up = any(indicator in user_query.lower() for indicator in follow_up_indicators)
        
        # Build the router prompt
        router_prompt = get_router_prompt(user_query, resume_available, jd_available, is_follow_up, recent_context)

        print(f"🔍 Router Debug - Sending prompt to LLM...")
        
        # Call the LLM
        response = llm.invoke(router_prompt)
        # Ensure response.content is a string
        response_content = response.content
        if isinstance(response_content, list):
            response_content = " ".join([str(item) for item in response_content])
        decision = response_content.strip().upper()
        
        print(f"🔍 Router Debug - LLM Response: '{response_content}'")
        print(f"🔍 Router Debug - Parsed Decision: '{decision}'")
        
        # Validate the decision
        valid_decisions = ["ANALYZE", "QUIZ", "REWRITE", "CLARIFY", "GREETING/INFO", "END_CONVERSATION"]
        if decision not in valid_decisions:
            decision = "GREETING/INFO"  # Default fallback
            print(f"🔍 Router Debug - Invalid decision, using fallback: '{decision}'")
            
        state["router_decision"] = decision
        print(f"🔍 Router Debug - Final Decision: '{decision}'")
        
    except Exception as e:
        print(f"🔍 Router Debug - Exception: {e}")
        # Fallback to mock logic if LLM fails
        user_query = state.get("user_query", "").lower()
        resume_available = bool(state.get("resume_text"))
        jd_available = bool(state.get("job_description_text"))
        decision = "GREETING/INFO"  # Default
        
        # Check for follow-up questions in fallback logic
        follow_up_indicators = ["regarding", "about", "concerning", "related to", "from", "of", "the", "that", "this"]
        is_follow_up = any(indicator in user_query for indicator in follow_up_indicators)
        
        if "analyze" in user_query and resume_available and jd_available:
            decision = "ANALYZE"
        elif ("quiz" in user_query or "question" in user_query or is_follow_up) and resume_available:
            decision = "QUIZ"
        elif "rewrite" in user_query and resume_available:
            decision = "REWRITE"
        elif not resume_available or ("analyze" in user_query and not jd_available):
            decision = "CLARIFY"
        elif any(x in user_query for x in ["hello", "hi", "what can you do"]):
            decision = "GREETING/INFO"
        elif any(x in user_query for x in ["bye", "thank you"]):
            decision = "END_CONVERSATION"
        state["router_decision"] = decision
        state["error_message"] = f"LLM routing failed, using fallback: {str(e)}"
        print(f"🔍 Router Debug - Using fallback decision: '{decision}'")
    
    return state 