from langgraph.graph import StateGraph, END
from src.types.state import LearningPathState
from src.core.topic_deconstructor import deconstruct_topic_node
from src.core.web_discoverer import discover_resources_node
from src.core.resource_evaluator import evaluate_resources_node
from src.core.curriculum_sequencer import sequence_curriculum_node

def create_curator_graph():
    """
    Defines the graph structure for the Learning Path Curator agent.
    """
    workflow = StateGraph(LearningPathState)

    # Add the nodes for each step of the pipeline
    workflow.add_node("deconstructor", deconstruct_topic_node)
    workflow.add_node("discoverer", discover_resources_node)
    workflow.add_node("evaluator", evaluate_resources_node)
    workflow.add_node("sequencer", sequence_curriculum_node)

    # Define the linear flow of the pipeline
    workflow.set_entry_point("deconstructor")
    workflow.add_edge("deconstructor", "discoverer")
    workflow.add_edge("discoverer", "evaluator")
    workflow.add_edge("evaluator", "sequencer")
    workflow.add_edge("sequencer", END)

    # Compile the graph into a runnable application
    return workflow.compile()

curator_app = create_curator_graph()
