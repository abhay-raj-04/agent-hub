from ..types.state import ResumeCoPilotState
from ..prompts.system_prompts import (
    get_greeting_response,
    get_missing_resume_message,
    get_missing_jd_message
)

def format_output_node(state: ResumeCoPilotState):
    """Formats agent outputs into user-friendly responses."""
    decision = state.get("router_decision", "")
    ai_response_content = "I'm processing your request..."
    
    if decision == "ANALYZE" and state.get("analysis_report"):
        ai_response_content = state["analysis_report"]
    elif decision == "QUIZ" and state.get("interview_quiz"):
        quiz_list = state["interview_quiz"]
        if quiz_list:
            ai_response_content = "\n".join(quiz_list)
    elif decision == "REWRITE" and state.get("rewritten_section"):
        ai_response_content = state["rewritten_section"]
    elif decision == "CLARIFY":
        missing_doc = []
        if not state.get("resume_text"): 
            missing_doc.append("resume")
        if "analyze" in state.get("user_query", "").lower() and not state.get("job_description_text"): 
            missing_doc.append("job description")
        
        if missing_doc:
            ai_response_content = get_missing_resume_message()
        else:
            ai_response_content = get_missing_jd_message()
    elif decision == "GREETING/INFO":
        ai_response_content = get_greeting_response()
    elif decision == "END_CONVERSATION":
        ai_response_content = "It was a pleasure assisting you! Goodbye."
    elif state.get("error_message"):
        ai_response_content = state["error_message"]
    
    state["formatted_response"] = ai_response_content
    return state 