import json
from src.types.state import LearningPathState
from src.tools.content_loader import get_webpage_content
from src.config.llm_config import get_llm
from src.prompts.curator_prompts import get_evaluator_prompt

def evaluate_resources_node(state: LearningPathState):
    print("--- [Step 3] Evaluating and Scoring Discovered Resources ---")
    discovered = state.get('discovered_resources', {})
    evaluated_resources = {}
    llm = get_llm()

    for topic, resources in discovered.items():
        print(f"  - Evaluating topic: {topic}")
        evaluated_list = []
        for resource in resources:
            content_snippet = get_webpage_content.invoke({"url": resource['url']})
            if not content_snippet:
                continue # Skip if content loading fails

            prompt = get_evaluator_prompt(topic, resource['title'], content_snippet)
            response = llm.invoke(prompt)
            try:
                cleaned = response.content.strip().replace("```json", "").replace("```", "")
                eval_data = json.loads(cleaned)
                
                # Combine original resource info with evaluation data
                resource.update(eval_data)
                evaluated_list.append(resource)
            except Exception as e:
                # print(f"    - Could not evaluate {resource['url']}: {e}")
                continue
        evaluated_resources[topic] = evaluated_list
    
    state['evaluated_resources'] = evaluated_resources
    return state
