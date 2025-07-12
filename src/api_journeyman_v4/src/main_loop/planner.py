# Placeholder for planner functionality
from src.types.state import JourneymanState

def planner_node(state: JourneymanState):
    """
    Plans an API call based on user goal and service documentation.
    This is a simplified implementation for the demo.
    """
    print("--- [Main Loop] Planning API call ---")
    # In a real implementation, this would use LLM to analyze docs and create a plan
    # For now, we'll create a mock plan
    mock_plan = {
        "method": "POST",
        "endpoint": f"/{state['service_name'].lower()}/api/v1/create",
        "parameters": {"name": "Test User", "email": "test@example.com"}
    }
    state['plan'] = mock_plan
    return state
