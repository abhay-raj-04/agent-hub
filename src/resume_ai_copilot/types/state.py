from typing import TypedDict, List, Optional

class ResumeCoPilotState(TypedDict):
    """State management for Resume AI Co-Pilot conversations."""
    resume_text: str
    job_description_text: Optional[str]
    user_query: str
    router_decision: Optional[str]
    analysis_report: Optional[str]
    interview_quiz: Optional[List[str]]
    rewritten_section: Optional[str]
    conversation_history: List[dict]
    error_message: Optional[str]
    formatted_response: Optional[str]
    think_mode: bool  # Pro model for quality vs Flash for speed 