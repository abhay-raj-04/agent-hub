from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro
from ..prompts.rewrite_prompts import get_rewrite_prompt
from ..prompts.fallback_prompts import get_fallback_rewrite_response

def rewrite_section_node(state: ResumeCoPilotState):
    """
    Improve specific resume sections/bullets. Update rewritten_section in state.
    Uses Gemini-2.5-pro for high-quality rewriting or Gemini-2.5-flash based on think_mode.
    """
    try:
        # Choose LLM based on think_mode
        think_mode = state.get("think_mode", False)
        if think_mode:
            llm = get_llm_pro()  # High-quality for thinking mode
        else:
            llm = get_llm_flash()  # Fast for normal mode
            
        user_query = state.get("user_query", "")
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        
        rewrite_prompt = get_rewrite_prompt(user_query, resume, jd)

        response = llm.invoke(rewrite_prompt)
        # Ensure response.content is a string
        response_content = response.content
        if isinstance(response_content, list):
            response_content = " ".join([str(item) for item in response_content])
        state["rewritten_section"] = response_content
        
    except Exception as e:
        # Fallback to mock rewriting if LLM fails
        rewritten = get_fallback_rewrite_response()
        state["rewritten_section"] = rewritten
        state["error_message"] = f"LLM rewriting failed, using fallback: {str(e)}"
    
    return state 