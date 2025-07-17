import streamlit as st
from dotenv import load_dotenv
from src.workflow import curator_app
from src.types.state import LearningPathState

# Load environment variables from .env file
load_dotenv()

def main():
    st.set_page_config(page_title="Personalized Learning Path Curator", layout="wide")
    st.title("Personalized Learning Path Curator 🧠✨")
    st.markdown("Turn your learning goal into a custom, step-by-step curriculum powered by AI.")

    with st.sidebar:
        st.header("Your Learning Goal")
        learning_goal = st.text_area("What do you want to learn?", "I want to learn web development to build interactive websites.", height=100)
        experience_level = st.selectbox(
            "What is your current experience level in this area?",
            ("Beginner", "Intermediate", "Advanced")
        )

    if st.sidebar.button("Generate My Learning Path", type="primary"):
        initial_state = LearningPathState(
            learning_goal=learning_goal,
            experience_level=experience_level
        )
        
        # This will be the main content area
        st.markdown("### Your Personalized Curriculum:")
        
        # A container for the progress updates and final result
        result_container = st.empty()
        
        with st.spinner("Agent at work... This may take a few minutes."):
            # We'll use a generator to get updates from the graph as it runs
            # This makes the UI feel much more responsive
            progress_text = ""
            
            # config={"recursion_limit": 50} is important for complex graphs
            for event in curator_app.stream(initial_state, config={"recursion_limit": 50}):
                for key, value in event.items():
                    # Check which node has just finished
                    if key == "deconstructor":
                        progress_text += "✅ **Step 1:** Goal deconstructed into topics.\n"
                    elif key == "discoverer":
                        progress_text += "✅ **Step 2:** Found potential learning resources online.\n"
                    elif key == "evaluator":
                        progress_text += "✅ **Step 3:** Evaluated and scored all resources.\n"
                    elif key == "sequencer":
                        progress_text += "✅ **Step 4:** Assembling your final curriculum.\n"
                    
                    # Update the UI with the latest progress
                    result_container.info(progress_text)

            # The final state is in the last event from the stream
            final_state = list(curator_app.stream(initial_state, config={"recursion_limit": 50}))[-1]
            
            if "sequencer" in final_state:
                final_curriculum = final_state["sequencer"].get("final_curriculum")
                if final_curriculum:
                    result_container.markdown(final_curriculum)
                else:
                    error = final_state["sequencer"].get("error_message", "An unknown error occurred.")
                    result_container.error(f"Failed to generate curriculum: {error}")
            else:
                 result_container.error("The agent could not complete the process. Please try again with a different goal.")

    else:
        st.info("Define your learning goal in the sidebar and click 'Generate' to begin.")
