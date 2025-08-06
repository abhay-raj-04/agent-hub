from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro
from ..prompts.rewrite_prompts import get_rewrite_prompt
from ..prompts.fallback_prompts import get_fallback_rewrite_response

def rewrite_section_node(state: ResumeCoPilotState):
    """Improves specific resume sections with enhanced clarity and impact."""
    try:
        llm = get_llm_pro() if state.get("think_mode", False) else get_llm_flash()
            
        user_query = state.get("user_query", "")
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        
        rewrite_prompt = get_rewrite_prompt(user_query, resume, jd)

        response = llm.invoke(rewrite_prompt)
        response_content = response.content
        if isinstance(response_content, list):
            response_content = " ".join([str(item) for item in response_content])
        state["rewritten_section"] = response_content
        
    except Exception as e:
        rewritten = get_fallback_rewrite_response()
        state["rewritten_section"] = rewritten
        state["error_message"] = f"LLM rewriting failed, using fallback: {str(e)}"
    
    return state 