import json
from src.types.state import LearningPathState
from src.config.llm_config import get_llm
from src.prompts.curator_prompts import get_deconstructor_prompt

def deconstruct_topic_node(state: LearningPathState):
    print("--- [Step 1] Deconstructing Learning Goal into Topics ---")
    llm = get_llm()
    prompt = get_deconstructor_prompt(state['learning_goal'], state['experience_level'])
    response = llm.invoke(prompt)
    try:
        cleaned = response.content.strip().replace("```json", "").replace("```", "")
        state['topics_graph'] = json.loads(cleaned)
    except Exception as e:
        state['error_message'] = f"Failed to deconstruct topic: {e}"
    return state
