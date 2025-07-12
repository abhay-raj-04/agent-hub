from src.types.state import JourneymanState
from src.config.llm_config import get_llm
from src.prompts.generation_prompts import get_context_aware_code_prompt

def generate_code_node(state: JourneymanState):
    print("--- [Generation] Creating context-aware code ---")
    llm = get_llm()
    prompt = get_context_aware_code_prompt(
        project_analysis=state['project_analysis'],
        service_analysis=state['service_analysis'],
        api_plan=state['plan'],
        user_goal=state['user_goal']
    )
    # In a real streaming app, you'd use llm.stream() and yield chunks here.
    # For simplicity, we invoke once. The prompt is designed to be robust.
    response = llm.invoke(prompt)
    state['final_output'] = response.content
    return state
