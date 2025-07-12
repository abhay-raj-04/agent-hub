from typing import TypedDict, List, Optional, Dict, Any

class JourneymanState(TypedDict):
    """
    Defines the memory or state for the Integration Co-Pilot agent.
    """
    # --- User Inputs ---
    project_path: str
    service_name: str
    api_key: Optional[str]
    user_choice: Optional[str]      # "guide" or "generate"
    user_goal: Optional[str]        # e.g., "Create a new customer"
    excluded_folders: Optional[List[str]]  # Folders to exclude from analysis

    # --- Analysis Phase (Populated in parallel) ---
    project_analysis: Optional[Dict[str, Any]] # {language, framework, style, files}
    service_analysis: Optional[Dict[str, Any]] # {docs_url, base_url, auth_method}

    # --- Synthesis & Main Loop ---
    synthesis_report: Optional[str]
    api_headers: Optional[Dict[str, str]]
    plan: Optional[Dict[str, Any]]
    api_response: Optional[Dict[str, Any]]

    # --- Final Output ---
    final_output: Optional[str] # Can be a guide or generated code
    error_message: Optional[str]
