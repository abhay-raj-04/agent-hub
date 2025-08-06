from ..types.state import ResumeCoPilotState
from ..config.llm_config import get_llm_flash, get_llm_pro
from ..prompts.quiz_prompts import get_quiz_prompt_standard, get_quiz_prompt_followup
from ..prompts.fallback_prompts import get_fallback_quiz_questions

def generate_quiz_node(state: ResumeCoPilotState):
    """Generates tailored interview questions based on resume and user query."""
    try:
        llm = get_llm_pro() if state.get("think_mode", False) else get_llm_flash()
            
        resume = state.get("resume_text", "")
        user_query = state.get("user_query", "")
        conversation_history = state.get("conversation_history", [])
        
        # Detect follow-up questions about previous interview questions
        is_follow_up = any(word in user_query.lower() for word in ["regarding", "about", "concerning", "question", "answer"])
        
        if is_follow_up and len(conversation_history) > 2:
            recent_history = conversation_history[-4:] if len(conversation_history) >= 4 else conversation_history
            quiz_prompt = get_quiz_prompt_followup(user_query, resume, recent_history)
        else:
            quiz_prompt = get_quiz_prompt_standard(resume, user_query)

        response = llm.invoke(quiz_prompt)
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
        # Parse questions from response
        questions = []
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('•') or line.startswith('-') or line.startswith('*')):
                clean_line = line.lstrip('0123456789.•-* ').strip()
                if clean_line:
                    questions.append(clean_line)
        
        if not questions:
            questions = get_fallback_quiz_questions()
        
        state["interview_quiz"] = questions
        
    except Exception as e:
        questions = get_fallback_quiz_questions()
        state["interview_quiz"] = questions
        state["error_message"] = f"LLM quiz generation failed, using fallback: {str(e)}"
    
    return state 