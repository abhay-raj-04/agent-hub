from typing import TypedDict, List, Optional, Dict

class LearningPathState(TypedDict):
    """
    Defines the state for the Learning Path Curator agent.
    """
    # --- User Inputs ---
    learning_goal: str
    experience_level: str # e.g., "Beginner", "Intermediate"

    # --- Pipeline State ---
    # 1. Deconstruction
    topics_graph: Optional[Dict[str, List[str]]] # e.g., {"Core": ["HTML", "CSS"], "Advanced": ["React"]}

    # 2. Discovery
    discovered_resources: Optional[Dict[str, List[Dict[str, str]]]] # { "HTML": [{"url": "...", "title": "..."}, ...]}

    # 3. Evaluation
    evaluated_resources: Optional[Dict[str, List[Dict[str, str]]]] # { "HTML": [{"url": "...", "title": "...", "quality": 8, "level": "Beginner"}, ...]}
    
    # 4. Sequencing & Presentation
    final_curriculum: Optional[str]

    # --- General ---
    error_message: Optional[str]
