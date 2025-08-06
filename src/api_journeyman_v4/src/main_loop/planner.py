# Planner functionality
from src.types.state import JourneymanState

def planner_node(state: JourneymanState):
    """Plans API calls based on user goals and service documentation."""
    print("--- [Main Loop] Planning API call ---")
    mock_plan = {
        "method": "POST",
        "endpoint": f"/{state['service_name'].lower()}/api/v1/create",
        "parameters": {"name": "Test User", "email": "test@example.com"}
    }
    state['plan'] = mock_plan
    return state
