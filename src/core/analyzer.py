from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro, get_llm_pro_streaming
from ..prompts.analysis_prompts import get_analysis_prompt
from ..prompts.fallback_prompts import get_fallback_analysis_report

def analyze_resume_node(state: ResumeCoPilotState):
    """
    Provide detailed feedback on resume against JD. Update analysis_report in state.
    Uses Gemini-2.5-pro for high-quality analysis or Gemini-2.5-flash based on think_mode.
    """
    try:
        # Choose LLM based on think_mode
        think_mode = state.get("think_mode", False)
        if think_mode:
            llm = get_llm_pro()  # High-quality for thinking mode
        else:
            llm = get_llm_flash()  # Fast for normal mode
            
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        
        analysis_prompt = get_analysis_prompt(resume, jd)

        response = llm.invoke(analysis_prompt)
        # Ensure response.content is a string
        response_content = response.content
        if isinstance(response_content, list):
            response_content = " ".join([str(item) for item in response_content])
        state["analysis_report"] = response_content
        
    except Exception as e:
        # Fallback to mock report if LLM fails
        report = get_fallback_analysis_report()
        state["analysis_report"] = report
        state["error_message"] = f"LLM analysis failed, using fallback: {str(e)}"
    
    return state

def analyze_resume_node_streaming(state: ResumeCoPilotState):
    """
    Provide detailed feedback on resume against JD with streaming support.
    Yields chunks of the response for real-time display.
    Uses Gemini-2.5-pro for high-quality analysis or Gemini-2.5-flash based on think_mode.
    """
    try:
        # Choose LLM based on think_mode
        think_mode = state.get("think_mode", False)
        if think_mode:
            llm = get_llm_pro_streaming()  # High-quality for thinking mode
        else:
            # For fast mode, we'll use the regular pro model but with streaming
            llm = get_llm_pro_streaming()  # Flash doesn't support streaming, so we use Pro streaming for both
            
        resume = state.get("resume_text", "")
        jd = state.get("job_description_text", "") or ""
        
        analysis_prompt = get_analysis_prompt(resume, jd)

        # Stream the response
        full_response = ""
        for chunk in llm.stream(analysis_prompt):
            if chunk.content:
                # Ensure chunk.content is a string
                chunk_content = chunk.content
                if isinstance(chunk_content, list):
                    chunk_content = " ".join([str(item) for item in chunk_content])
                full_response += chunk_content
                yield chunk_content
        
        state["analysis_report"] = full_response
        
    except Exception as e:
        # Fallback to mock report if LLM fails
        report = get_fallback_analysis_report()
        state["analysis_report"] = report
        state["error_message"] = f"LLM analysis failed, using fallback: {str(e)}"
        yield report 