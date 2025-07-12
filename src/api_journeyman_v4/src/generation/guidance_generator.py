from src.types.state import JourneymanState
from src.config.llm_config import get_llm
from src.prompts.generation_prompts import get_guidance_prompt

def generate_guidance_node(state: JourneymanState):
    print("--- [Generation] Creating integration guide ---")
    llm = get_llm()
    prompt = get_guidance_prompt(state['project_analysis'], state['service_analysis'])
    response = llm.invoke(prompt)
    state['final_output'] = response.content
    return state
