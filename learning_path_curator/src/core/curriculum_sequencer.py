from src.types.state import LearningPathState
from src.config.llm_config import get_llm
from src.prompts.curator_prompts import get_sequencer_prompt

def sequence_curriculum_node(state: LearningPathState):
    print("--- [Step 4] Sequencing Final Curriculum ---")
    llm = get_llm()
    prompt = get_sequencer_prompt(
        state['evaluated_resources'],
        state['learning_goal'],
        state['experience_level']
    )
    
    response = llm.invoke(prompt)
    state['final_curriculum'] = response.content
    return state
