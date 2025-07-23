from src.types.state import LearningPathState
from src.tools.web_search import search_for_resources

def discover_resources_node(state: LearningPathState):
    print("--- [Step 2] Discovering Web Resources for Each Topic ---")
    topics_graph = state.get('topics_graph', {})
    all_topics = [topic for sublist in topics_graph.values() for topic in sublist]
    
    discovered_resources = {}
    for topic in all_topics:
        print(f"  - Searching for: {topic}")
        resources = search_for_resources.invoke({"topic": topic})
        discovered_resources[topic] = resources
        
    state['discovered_resources'] = discovered_resources
    return state
