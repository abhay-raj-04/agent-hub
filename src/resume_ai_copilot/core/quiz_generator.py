from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro
from ..prompts.quiz_prompts import get_quiz_prompt_standard, get_quiz_prompt_followup
from ..prompts.fallback_prompts import get_fallback_quiz_questions

def generate_quiz_node(state: ResumeCoPilotState):
    """
    Generate tailored interview questions. Update interview_quiz in state.
    Uses Gemini-2.5-pro for high-quality question generation or Gemini-2.5-flash based on think_mode.
    """
    try:
        # Choose LLM based on think_mode
        think_mode = state.get("think_mode", False)
        if think_mode:
            llm = get_llm_pro()  # High-quality for thinking mode
        else:
            llm = get_llm_flash()  # Fast for normal mode
            
        resume = state.get("resume_text", "")
        user_query = state.get("user_query", "")
        conversation_history = state.get("conversation_history", [])
        
        # Check if this is a follow-up question about previous questions
        is_follow_up = any(word in user_query.lower() for word in ["regarding", "about", "concerning", "question", "answer"])
        
        if is_follow_up and len(conversation_history) > 2:
            # This is a follow-up question, generate related questions
            quiz_prompt = get_quiz_prompt_followup(user_query, resume, conversation_history[-4:] if len(conversation_history) >= 4 else conversation_history)
        else:
            # Standard quiz generation - now includes user query
            quiz_prompt = get_quiz_prompt_standard(resume, user_query)

        response = llm.invoke(quiz_prompt)
        # Ensure response.content is a string
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
        questions = []
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('•') or line.startswith('-') or line.startswith('*')):
                # Remove numbering/bullets and clean up
                clean_line = line.lstrip('0123456789.•-* ').strip()
                if clean_line:
                    questions.append(clean_line)
        
        if not questions:
            # Fallback if parsing fails
            questions = get_fallback_quiz_questions()
        
        state["interview_quiz"] = questions
        
    except Exception as e:
        # Fallback to mock questions if LLM fails
        questions = get_fallback_quiz_questions()
        state["interview_quiz"] = questions
        state["error_message"] = f"LLM quiz generation failed, using fallback: {str(e)}"
    
    return state 