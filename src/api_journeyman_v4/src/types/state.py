from typing import TypedDict, List, Optional, Dict, Any

class JourneymanState(TypedDict):
    """State management for Integration Co-Pilot agent."""
    # User Inputs
    project_path: str
    service_name: str
    api_key: Optional[str]
    user_choice: Optional[str]
    user_goal: Optional[str]
    excluded_folders: Optional[List[str]]

    # Analysis Phase
    project_analysis: Optional[Dict[str, Any]]
    service_analysis: Optional[Dict[str, Any]]

    # Synthesis & Main Loop
    synthesis_report: Optional[str]
    api_headers: Optional[Dict[str, str]]
    plan: Optional[Dict[str, Any]]
    api_response: Optional[Dict[str, Any]]

    # Final Output
    final_output: Optional[str]
    error_message: Optional[str]
