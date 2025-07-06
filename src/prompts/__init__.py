# Prompts module for Resume AI Co-Pilot

from .router_prompts import get_router_prompt
from .analysis_prompts import get_analysis_prompt
from .quiz_prompts import get_quiz_prompt_standard, get_quiz_prompt_followup
from .rewrite_prompts import get_rewrite_prompt
from .fallback_prompts import (
    get_fallback_analysis_report,
    get_fallback_quiz_questions,
    get_fallback_rewrite_response
)
from .system_prompts import (
    get_greeting_response,
    get_missing_resume_message,
    get_missing_jd_message,
    get_error_message,
    get_welcome_message
)

__all__ = [
    'get_router_prompt',
    'get_analysis_prompt', 
    'get_quiz_prompt_standard',
    'get_quiz_prompt_followup',
    'get_rewrite_prompt',
    'get_fallback_analysis_report',
    'get_fallback_quiz_questions',
    'get_fallback_rewrite_response',
    'get_greeting_response',
    'get_missing_resume_message',
    'get_missing_jd_message',
    'get_error_message',
    'get_welcome_message'
] 