from typing import TypedDict, List, Optional

class ResumeCoPilotState(TypedDict):
    """
    Represents the state of the Resume AI Co-Pilot conversation.
    """
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
    think_mode: bool  # True for high-quality (Pro), False for fast (Flash) 