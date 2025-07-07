import streamlit as st
from dotenv import load_dotenv
import os
import time
from PIL import Image
import pytesseract

# Load environment variables from .env file
load_dotenv()

from ..types.state import ResumeCoPilotState
from ..core.analyzer import analyze_resume_node_streaming
from ..prompts.system_prompts import (
    get_missing_resume_message,
    get_missing_jd_message,
    get_greeting_response,
    get_error_message
)
from langchain_core.messages import HumanMessage, AIMessage
from io import BytesIO
from docx import Document
from PyPDF2 import PdfReader

# --- Helper functions for document parsing ---
def extract_text_from_pdf(file_bytes):
    reader = PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_bytes):
    doc = Document(BytesIO(file_bytes))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_image(file_bytes):
    try:
        img = Image.open(BytesIO(file_bytes))
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"[Error extracting text from image: {e}]"

def main():
    """Main streaming Streamlit application"""
    # --- Streamlit UI Setup ---
    st.set_page_config(page_title="Resume AI Co-Pilot (Streaming)", layout="centered")
    st.title("Resume AI Co-Pilot 🚀 (Real-time Streaming)")

    # Initialize session state for LangGraph state and conversation history
    if "graph_state" not in st.session_state:
        st.session_state.graph_state = ResumeCoPilotState(
            resume_text="",
            job_description_text="",
            user_query="",
            router_decision=None,
            analysis_report=None,
            interview_quiz=None,
            rewritten_section=None,
            conversation_history=[],
            error_message=None,
            formatted_response=None,
            think_mode=False
        )
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append(AIMessage("Hello! Upload your resume and job description to get started. Then tell me what you need!"))

    # --- File Uploads ---
    with st.sidebar:
        # Think Mode Toggle
        st.markdown("---")
        st.subheader("🤔 AI Mode")
        think_mode = st.toggle(
            "Think Mode (High Quality)", 
            value=st.session_state.graph_state.get("think_mode", False),
            help="Enable for higher quality responses (slower) or disable for faster responses"
        )
        st.session_state.graph_state["think_mode"] = think_mode
        
        if think_mode:
            st.info("🧠 **Think Mode ON** - Using Gemini-2.5-Pro for high-quality responses")
        else:
            st.info("⚡ **Fast Mode ON** - Using Gemini-2.5-Flash for quick responses")
        
        st.markdown("---")
        st.subheader("📄 Documents")
        uploaded_resume = st.file_uploader("Upload Resume (.pdf, .docx, .png, .jpg, .jpeg)", type=["pdf", "docx", "png", "jpg", "jpeg"], key="resume_uploader")
        uploaded_jd = st.file_uploader("Upload Job Description (.pdf, .docx, .txt, .png, .jpg, .jpeg)", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"], key="jd_uploader")

        # Auto-process resume when uploaded
        if uploaded_resume is not None:
            if "last_resume" not in st.session_state or st.session_state.last_resume != uploaded_resume.name:
                with st.spinner("Processing resume..."):
                    if uploaded_resume.type == "application/pdf":
                        st.session_state.graph_state["resume_text"] = extract_text_from_pdf(uploaded_resume.read())
                    elif uploaded_resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        st.session_state.graph_state["resume_text"] = extract_text_from_docx(uploaded_resume.read())
                    elif uploaded_resume.type in ["image/png", "image/jpeg"]:
                        st.session_state.graph_state["resume_text"] = extract_text_from_image(uploaded_resume.read())
                    st.session_state.last_resume = uploaded_resume.name
                    st.success(f"✅ Resume processed: {uploaded_resume.name}")

        # Auto-process job description when uploaded
        if uploaded_jd is not None:
            if "last_jd" not in st.session_state or st.session_state.last_jd != uploaded_jd.name:
                with st.spinner("Processing job description..."):
                    if uploaded_jd.type == "application/pdf":
                        st.session_state.graph_state["job_description_text"] = extract_text_from_pdf(uploaded_jd.read())
                    elif uploaded_jd.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        st.session_state.graph_state["job_description_text"] = extract_text_from_docx(uploaded_jd.read())
                    elif uploaded_jd.type in ["image/png", "image/jpeg"]:
                        st.session_state.graph_state["job_description_text"] = extract_text_from_image(uploaded_jd.read())
                    else: # Assume text file
                        st.session_state.graph_state["job_description_text"] = uploaded_jd.read().decode("utf-8")
                    st.session_state.last_jd = uploaded_jd.name
                    st.success(f"✅ Job Description processed: {uploaded_jd.name}")

        # Show current upload status
        if st.session_state.graph_state.get("resume_text"):
            st.info("📄 Resume: Ready")
        else:
            st.info("📄 Resume: Not uploaded")
            
        if st.session_state.graph_state.get("job_description_text"):
            st.info("📋 Job Description: Ready")
        else:
            st.info("📋 Job Description: Not uploaded")
        
        # Clear conversation button
        st.markdown("---")
        if st.button("🗑️ Clear Conversation", type="secondary"):
            st.session_state.messages = []
            st.session_state.messages.append(AIMessage("Hello! Upload your resume and job description to get started. Then tell me what you need!"))
            st.rerun()

    # Display conversation history
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message("ai").write(msg.content)

    # Show upload prompt only when user first visits (no conversation history)
    if not st.session_state.graph_state.get("resume_text") and len(st.session_state.messages) <= 1:
        st.markdown("---")
        st.markdown("### 📄 Welcome to Resume AI Co-Pilot!")
        st.markdown("To get started, please upload your resume using the sidebar.")
        st.markdown("Once you upload your resume, I can help you with:")
        st.markdown("- 📊 **Resume Analysis** against job descriptions")
        st.markdown("- 🎯 **Interview Questions** based on your experience")
        st.markdown("- ✏️ **Resume Improvements** and rewriting")
        st.markdown("- 📋 **ATS Optimization** tips")
        st.markdown("---")

    # Chat input - Simple chat bot interface
    if user_query := st.chat_input("Ask me anything about your resume or job description..."):
        st.session_state.messages.append(HumanMessage(user_query))
        st.chat_message("user").write(user_query)

        # Update graph state with user query and history
        st.session_state.graph_state["user_query"] = user_query
        st.session_state.graph_state["conversation_history"].append({"role": "user", "content": user_query})

        # Create a placeholder for streaming response
        with st.chat_message("ai"):
            response_placeholder = st.empty()
            
            # Choose spinner text based on think mode
            think_mode = st.session_state.graph_state.get("think_mode", False)
            if think_mode:
                spinner_text = "🧠 Analyzing deeply..."
            else:
                spinner_text = "⚡ Generating..."
            
            with st.spinner(spinner_text):
                try:
                    # Check if user wants analysis and has both documents
                    if "analyze" in user_query.lower() and st.session_state.graph_state.get("resume_text") and st.session_state.graph_state.get("job_description_text"):
                        # Use streaming analysis
                        full_response = ""
                        response_placeholder.markdown("🔍 **Analyzing your resume...**\n\n")
                        
                        for chunk in analyze_resume_node_streaming(st.session_state.graph_state):
                            full_response += chunk
                            response_placeholder.markdown(full_response + "▌")
                            time.sleep(0.01)  # Small delay for smooth streaming
                        
                        # Final response without cursor
                        response_placeholder.markdown(full_response)
                        
                    else:
                        # For other queries, use simple response
                        if "quiz" in user_query.lower() and st.session_state.graph_state.get("resume_text"):
                            response = "Here are some interview questions based on your resume:\n\n1. Tell me about a time when you led a project from start to finish.\n2. Describe a situation where you had to quickly learn a new technology.\n3. How have you contributed to improving team collaboration?\n4. Can you give an example of how you handled a difficult stakeholder request?\n5. What is an achievement from your resume that you are most proud of?"
                        elif "rewrite" in user_query.lower() and st.session_state.graph_state.get("resume_text"):
                            response = "I can help you rewrite specific sections of your resume. Please provide the text you'd like me to improve, and I'll suggest better versions with stronger action verbs and quantifiable results."
                        elif not st.session_state.graph_state.get("resume_text"):
                            response = get_missing_resume_message()
                        elif "analyze" in user_query.lower() and not st.session_state.graph_state.get("job_description_text"):
                            response = get_missing_jd_message()
                        else:
                            response = get_greeting_response()
                        
                        # Stream the simple response
                        full_response = ""
                        for char in response:
                            full_response += char
                            response_placeholder.markdown(full_response + "▌")
                            time.sleep(0.01)
                        
                        response_placeholder.markdown(full_response)
                    
                    st.session_state.messages.append(AIMessage(full_response))
                    st.session_state.graph_state["conversation_history"].append({"role": "ai", "content": full_response})

                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    error_msg = get_error_message()
                    response_placeholder.write(error_msg)
                    st.session_state.messages.append(AIMessage(error_msg))
                    st.session_state.graph_state["conversation_history"].append({"role": "ai", "content": f"Error: {e}"})

if __name__ == "__main__":
    main() 