from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro, get_llm_pro_streaming
from ..prompts.analysis_prompts import get_analysis_prompt
from ..prompts.fallback_prompts import get_fallback_analysis_report

def analyze_resume_node(state: ResumeCoPilotState):
    """Analyzes resume against job description and provides detailed feedback."""
    try:
        # Use pro model for detailed analysis, flash for quick feedback
        llm = get_llm_pro() if state.get("think_mode", False) else get_llm_flash()
            
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        user_query = state.get("user_query", "")
        
        analysis_prompt = get_analysis_prompt(resume, jd, user_query)

        response = llm.invoke(analysis_prompt)
        # Handle both string and list responses
        response_content = response.content
        if isinstance(response_content, list):
            response_content = " ".join([str(item) for item in response_content])
        state["analysis_report"] = response_content
        
    except Exception as e:
        # Fallback when LLM is unavailable
        report = get_fallback_analysis_report()
        state["analysis_report"] = report
        state["error_message"] = f"LLM analysis failed, using fallback: {str(e)}"
    
    return state

def analyze_resume_node_streaming(state: ResumeCoPilotState):
    """Streams resume analysis in real-time for better user experience."""
    try:
        # Flash model doesn't support streaming, so use pro for both modes
        llm = get_llm_pro_streaming()
            
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        user_query = state.get("user_query", "")
        
        analysis_prompt = get_analysis_prompt(resume, jd, user_query)

        full_response = ""
        for chunk in llm.stream(analysis_prompt):
            if chunk.content:
                chunk_content = chunk.content
                if isinstance(chunk_content, list):
                    chunk_content = " ".join([str(item) for item in chunk_content])
                full_response += chunk_content
                yield chunk_content
        
        state["analysis_report"] = full_response
        
    except Exception as e:
        report = get_fallback_analysis_report()
        state["analysis_report"] = report
        state["error_message"] = f"LLM analysis failed, using fallback: {str(e)}"
        yield report 