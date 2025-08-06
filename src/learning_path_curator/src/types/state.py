from typing import TypedDict, List, Optional, Dict

class LearningPathState(TypedDict):
    """State management for Learning Path Curator agent."""
    # User Inputs
    learning_goal: str
    experience_level: str

    # Pipeline State
    topics_graph: Optional[Dict[str, List[str]]]
    discovered_resources: Optional[Dict[str, List[Dict[str, str]]]]
    evaluated_resources: Optional[Dict[str, List[Dict[str, str]]]]
    final_curriculum: Optional[str]

    # General
    error_message: Optional[str]
