from langgraph.graph import StateGraph, END
from ..types.state import ResumeCoPilotState
from ..core import (
    ingest_documents_node,
    router_node,
    analyze_resume_node,
    generate_quiz_node,
    rewrite_section_node,
    format_output_node
)

# Initialize the workflow graph with the ResumeCoPilotState
def create_workflow():
    workflow = StateGraph(ResumeCoPilotState)

    # Add nodes
    workflow.add_node("ingest_documents", ingest_documents_node)
    workflow.add_node("router", router_node)
    workflow.add_node("analyze_resume", analyze_resume_node)
    workflow.add_node("generate_quiz", generate_quiz_node)
    workflow.add_node("rewrite_section", rewrite_section_node)
    workflow.add_node("format_output", format_output_node)

    # Set entry point
    workflow.set_entry_point("ingest_documents")

    # Define edges
    workflow.add_edge("ingest_documents", "router")

    # Conditional routing from the router node
    workflow.add_conditional_edges(
        "router",
        lambda state: state["router_decision"],
        {
            "ANALYZE": "analyze_resume",
            "QUIZ": "generate_quiz",
            "REWRITE": "rewrite_section",
            "CLARIFY": "format_output",
            "GREETING/INFO": "format_output",
            "END_CONVERSATION": END,
        },
    )

    # After each sub-agent, go to format_output
    workflow.add_edge("analyze_resume", "format_output")
    workflow.add_edge("generate_quiz", "format_output")
    workflow.add_edge("rewrite_section", "format_output")

    # After formatting output, end the workflow (don't loop back)
    workflow.add_edge("format_output", END)

    # Compile the graph
    app = workflow.compile()
    return app

# Create the compiled app instance
app = create_workflow() 