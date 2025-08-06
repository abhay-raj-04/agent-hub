# Executor functionality
from src.types.state import JourneymanState

def executor_node(state: JourneymanState):
    """Executes planned API calls."""
    print("--- [Main Loop] Executing API call ---")
    mock_response = {
        "status": "success",
        "data": {"id": "12345", "message": "Operation completed successfully"}
    }
    state['api_response'] = mock_response
    return state
