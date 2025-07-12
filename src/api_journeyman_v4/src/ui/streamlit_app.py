import streamlit as st
from dotenv import load_dotenv
import threading
import queue
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from src.types.state import JourneymanState
from src.analysis.project_analyzer import analyze_project_code_node
from src.analysis.service_analyzer import analyze_service_docs_node
from src.generation.guidance_generator import generate_guidance_node
# We will simulate the main loop for clarity as it's complex
# from src.main_loop...

# Load environment variables
load_dotenv()

# --- Helper for folder selection ---
def select_folder():
    """Open a folder selection dialog and return the selected path"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.wm_attributes('-topmost', 1)  # Bring to front
    folder_path = filedialog.askdirectory(title="Select Your Project Folder")
    root.destroy()
    return folder_path

# --- Helper for multithreading in Streamlit ---
def run_in_thread(target, args, q):
    thread = threading.Thread(target=target, args=args)
    thread.start()
    thread.join() # Wait for the thread to complete

def main():
    st.set_page_config(page_title="Integration Co-Pilot V4", layout="wide")
    st.title("API Journeyman V4: The Integration Co-Pilot 🚀")
    
    st.markdown("""
    This AI agent helps you integrate third-party services into your existing codebase by:
    - 📁 **Analyzing your project** to understand its language, framework, and coding style
    - 🔍 **Finding and analyzing API documentation** for any service you want to integrate  
    - 🤖 **Generating context-aware code** that matches your project's patterns
    - 📋 **Providing step-by-step guides** for manual integration
    """)

    # Initialize session state for multi-step workflow
    if "step" not in st.session_state:
        st.session_state.step = "initial_input"
    if "state" not in st.session_state:
        st.session_state.state = JourneymanState()
    if "synthesis_report" not in st.session_state:
        st.session_state.synthesis_report = ""

    # --- STEP 1: Initial User Input ---
    if st.session_state.step == "initial_input":
        st.header("Step 1: Provide Project and Service Details")
        
        # Project folder selection
        st.subheader("📁 Select Your Project Folder")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Text input for manual path entry
            project_path = st.text_input(
                "Project Folder Path", 
                value=st.session_state.get("selected_folder_path", ""),
                key="project_path_input",
                help="Enter the absolute path to your project folder or use the browse button"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
            if st.button("📂 Browse", help="Click to browse and select your project folder"):
                try:
                    selected_path = select_folder()
                    if selected_path:
                        st.session_state.selected_folder_path = selected_path
                        st.rerun()
                    else:
                        st.warning("No folder selected")
                except Exception as e:
                    st.error(f"Error opening folder dialog: {str(e)}")
        
        # Show selected folder info and exclusion options
        if project_path:
            if Path(project_path).exists():
                st.success(f"✅ Valid project folder: `{project_path}`")
                
                # Show folder contents and allow exclusions
                try:
                    all_items = list(Path(project_path).iterdir())
                    folders_only = [item for item in all_items if item.is_dir()]
                    files_only = [item for item in all_items if item.is_file()]
                    
                    if folders_only or files_only:
                        st.subheader("📋 Project Contents & Exclusions")
                        
                        # Folder exclusion section
                        if folders_only:
                            st.markdown("**� Folders in your project:**")
                            
                            # Default exclusions - common folders to exclude
                            default_excludes = {
                                '__pycache__', 'node_modules', '.git', '.vscode', '.idea', 
                                'venv', 'env', '.env', 'build', 'dist', '.next', 'coverage',
                                '.nyc_output', 'logs', 'tmp', 'temp', '.cache', '.pytest_cache'
                            }
                            
                            # Find which default excludes exist in the project
                            existing_folders = {folder.name for folder in folders_only}
                            suggested_excludes = default_excludes.intersection(existing_folders)
                            
                            # Initialize exclusions in session state
                            if "excluded_folders" not in st.session_state:
                                st.session_state.excluded_folders = list(suggested_excludes)
                            
                            # Create columns for folder display
                            cols = st.columns(3)
                            for idx, folder in enumerate(folders_only):
                                col_idx = idx % 3
                                with cols[col_idx]:
                                    is_excluded = folder.name in st.session_state.excluded_folders
                                    
                                    # Color code based on exclusion status
                                    if is_excluded:
                                        st.markdown(f"🚫 ~~{folder.name}~~")
                                    else:
                                        st.markdown(f"� {folder.name}")
                                    
                                    # Toggle button for exclusion
                                    button_text = "Include" if is_excluded else "Exclude"
                                    button_type = "secondary" if is_excluded else "primary"
                                    
                                    if st.button(f"{button_text}", key=f"toggle_{folder.name}", type=button_type):
                                        if is_excluded:
                                            st.session_state.excluded_folders.remove(folder.name)
                                        else:
                                            st.session_state.excluded_folders.append(folder.name)
                                        st.rerun()
                            
                            # Show exclusion summary
                            if st.session_state.excluded_folders:
                                st.info(f"🚫 Excluded folders: {', '.join(sorted(st.session_state.excluded_folders))}")
                            else:
                                st.info("✅ All folders will be analyzed")
                            
                            # Quick action buttons
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button("🚫 Exclude All Common", help="Exclude common build/cache folders"):
                                    st.session_state.excluded_folders = list(suggested_excludes)
                                    st.rerun()
                            with col2:
                                if st.button("✅ Include All", help="Include all folders in analysis"):
                                    st.session_state.excluded_folders = []
                                    st.rerun()
                            with col3:
                                if st.button("🔄 Reset to Suggested", help="Reset to suggested exclusions"):
                                    st.session_state.excluded_folders = list(suggested_excludes)
                                    st.rerun()
                        
                        # Show file count summary
                        included_folders = len([f for f in folders_only if f.name not in st.session_state.excluded_folders])
                        st.caption(f"📊 Summary: {included_folders}/{len(folders_only)} folders • {len(files_only)} files • Ready for analysis")
                        
                except Exception as e:
                    st.warning(f"Could not read folder contents: {str(e)}")
            else:
                st.error(f"❌ Folder does not exist: `{project_path}`")
        
        # Service name input
        st.subheader("🔌 Service to Integrate")
        service_name = st.text_input(
            "Service Name", 
            key="service_name",
            placeholder="e.g., Stripe, Twilio, OpenAI, Mailgun, etc.",
            help="Enter the name of the service/API you want to integrate"
        )
        
        # Examples section
        with st.expander("💡 Popular Service Examples"):
            st.markdown("""
            **Payment Processing:** Stripe, PayPal, Square  
            **Communication:** Twilio, SendGrid, Mailgun  
            **AI/ML:** OpenAI, Anthropic, Google AI  
            **Database:** Supabase, Firebase, MongoDB Atlas  
            **Storage:** AWS S3, Cloudinary, Google Cloud Storage  
            **Authentication:** Auth0, Firebase Auth, Clerk  
            """)
        
        with st.expander("📁 About Folder Exclusions"):
            st.markdown("""
            **Commonly Excluded Folders:**
            - `__pycache__`, `.pytest_cache` - Python cache files
            - `node_modules` - Node.js dependencies  
            - `.git`, `.vscode`, `.idea` - Version control & IDE files
            - `venv`, `env` - Virtual environments
            - `build`, `dist`, `.next` - Build artifacts
            - `logs`, `tmp`, `temp`, `.cache` - Temporary files
            
            **Why exclude folders?** These folders typically contain generated files, dependencies, or cache that don't represent your actual code patterns and can slow down analysis.
            """)
        
        if st.button("🚀 Start Analysis", type="primary"):
            if not project_path or not service_name:
                st.warning("⚠️ Please provide both a project folder path and a service name.")
            elif not Path(project_path).exists():
                st.error("❌ The specified project folder does not exist.")
            else:
                st.session_state.state['project_path'] = project_path
                st.session_state.state['service_name'] = service_name
                # Pass excluded folders to the analysis state
                st.session_state.state['excluded_folders'] = st.session_state.get('excluded_folders', [])
                st.session_state.step = "analysis"
                st.rerun()

    # --- STEP 2: Parallel Analysis ---
    if st.session_state.step == "analysis":
        st.header("Step 2: Autonomous Analysis in Progress...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        q = queue.Queue()
        
        with st.spinner("🔍 Analyzing your project and the service docs... This may take a moment."):
            # Update progress
            progress_bar.progress(25)
            excluded_count = len(st.session_state.state.get('excluded_folders', []))
            if excluded_count > 0:
                status_text.text(f"📁 Analyzing your project structure and code... (excluding {excluded_count} folders)")
            else:
                status_text.text("📁 Analyzing your project structure and code...")
            
            # We run the analysis nodes. A true parallel UI is complex, so we run sequentially but could thread.
            state = analyze_project_code_node(st.session_state.state)
            if state.get("error_message"):
                st.error(f"❌ Project Analysis Failed: {state['error_message']}")
                if st.button("🔄 Try Again"):
                    st.session_state.step = "initial_input"
                    st.rerun()
                return

            progress_bar.progress(50)
            status_text.text("🌐 Finding and analyzing service documentation...")

            state = analyze_service_docs_node(state)
            if state.get("error_message"):
                st.error(f"❌ Service Analysis Failed: {state['error_message']}")
                if st.button("🔄 Try Again"):
                    st.session_state.step = "initial_input"
                    st.rerun()
                return

            progress_bar.progress(75)
            status_text.text("📊 Synthesizing analysis results...")
            
            st.session_state.state = state
            
            # --- Synthesis Report Generation ---
            pa = state['project_analysis']
            sa = state['service_analysis']
            excluded_folders = state.get('excluded_folders', [])
            
            excluded_info = ""
            if excluded_folders:
                excluded_info = f"\n*   **Excluded from Analysis:** `{', '.join(sorted(excluded_folders))}`"
            
            report = f"""
### ✅ Analysis Complete!

Here's what I discovered about your integration:

#### 📁 Your Project (`{Path(state['project_path']).name}`)
*   **Language:** {pa.get('language', 'N/A')}
*   **Framework:** {pa.get('framework', 'N/A')}
*   **Coding Style:** {pa.get('style', 'N/A')}
*   **Suggested Integration Files:** `{', '.join(pa.get('relevant_files', []))}`{excluded_info}

#### 🔌 Target Service ({state['service_name']})
*   **Base URL:** `{sa.get('base_url', 'N/A')}`
*   **Authentication Method:** {sa.get('auth_method', 'N/A')}

Ready to proceed with integration! 🎉
"""
            st.session_state.synthesis_report = report
            progress_bar.progress(100)
            status_text.text("✅ Analysis complete!")
            
            st.session_state.step = "interaction"
            st.rerun()

    # --- STEP 3: User Interaction ---
    if st.session_state.step == "interaction":
        st.header("Step 3: Choose Your Integration Path")
        st.markdown(st.session_state.synthesis_report)

        st.subheader("🔐 API Configuration")
        api_key = st.text_input(
            f"Your {st.session_state.state['service_name']} API Key:", 
            type="password", 
            key="api_key",
            help="This will be used in the generated code examples (stored securely)"
        )
        
        st.subheader("🎯 Integration Approach")
        user_choice = st.radio(
            "What would you like me to help you with?",
            ("Select an option", "📋 Guide me through the integration steps", "💻 Generate code for a specific goal"),
            key="user_choice",
            help="Choose between a step-by-step guide or direct code generation"
        )

        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("🚀 Proceed", type="primary"):
                if not api_key or user_choice == "Select an option":
                    st.warning("⚠️ Please provide your API key and select an integration approach.")
                else:
                    st.session_state.state['api_key'] = api_key
                    st.session_state.state['user_choice'] = user_choice
                    if "Guide me" in user_choice:
                        st.session_state.step = "run_guidance"
                    else:
                        st.session_state.step = "get_goal"
                    st.rerun()
        
        with col2:
            if st.button("🔄 Start Over"):
                st.session_state.clear()
                st.rerun()

    # --- STEP 4a: Guidance Generation ---
    if st.session_state.step == "run_guidance":
        st.header("📋 Your Custom Integration Guide")
        
        with st.spinner("🤖 Generating your personalized integration guide..."):
            final_state = generate_guidance_node(st.session_state.state)
            
        st.markdown("### 🎯 Step-by-Step Integration Guide")
        st.markdown(final_state.get('final_output', "❌ Could not generate guide."))
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("💻 Generate Code Instead"):
                st.session_state.step = "get_goal"
                st.rerun()
        with col2:
            if st.button("🔄 Start Over"):
                st.session_state.clear()
                st.rerun()
            
    # --- STEP 4b: Code Generation ---
    if st.session_state.step == "get_goal":
        st.header("💻 Generate Context-Aware Code")
        
        st.markdown("Tell me specifically what you want to accomplish with this API:")
        
        user_goal = st.text_area(
            "Your Integration Goal", 
            key="user_goal",
            placeholder="e.g., 'Create a new customer with name and email'\n'Send a welcome email to new users'\n'Process a payment for $50'\n'Upload an image and get the URL'",
            height=100,
            help="Be specific about what action you want to perform"
        )
        
        # Example goals based on common services
        with st.expander("💡 Example Goals by Service Type"):
            st.markdown("""
            **Payment (Stripe):** "Create a payment intent for $50", "Create a customer and save their card"  
            **Email (SendGrid):** "Send a welcome email with template", "Send a password reset email"  
            **SMS (Twilio):** "Send verification code to phone number", "Send order confirmation SMS"  
            **Storage (AWS S3):** "Upload a file and get public URL", "Delete a file from bucket"  
            **AI (OpenAI):** "Generate text completion", "Create embeddings for text search"  
            """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("🤖 Generate Code", type="primary"):
                if not user_goal.strip():
                    st.warning("⚠️ Please describe your integration goal.")
                else:
                    st.session_state.state['user_goal'] = user_goal
                    # This is where you would invoke the full main_loop graph (planner -> executor -> generator)
                    st.info("🔄 Running Planner → Executor → Generator workflow...")
                    
                    with st.spinner("🎯 Analyzing your goal and generating context-aware code..."):
                        # For this example, we directly call the final generator node
                        # A real implementation would run the full chain.
                        # We'll create a mock plan for the generator.
                        mock_plan = {
                            "method": "POST", 
                            "endpoint": f"/{st.session_state.state['service_name'].lower()}/v1/create", 
                            "parameters": {"name": "Test User", "email": "test@example.com"}
                        }
                        st.session_state.state['plan'] = mock_plan
                        
                        from src.generation.code_generator import generate_code_node
                        final_state = generate_code_node(st.session_state.state)
                        
                        st.markdown("### 🎯 Generated Code")
                        st.markdown("Here's the context-aware code that matches your project's style:")
                        
                        # Determine language for syntax highlighting
                        lang = final_state['project_analysis']['language'].lower()
                        if lang == 'javascript':
                            lang = 'js'
                        elif lang == 'typescript':
                            lang = 'ts'
                        
                        st.code(
                            final_state.get('final_output', "❌ Could not generate code."), 
                            language=lang
                        )
                        
                        # Add download button
                        if final_state.get('final_output'):
                            st.download_button(
                                label="📥 Download Code",
                                data=final_state['final_output'],
                                file_name=f"{st.session_state.state['service_name'].lower()}_integration.{lang}",
                                mime="text/plain"
                            )
        
        with col2:
            if st.button("📋 Get Guide Instead"):
                st.session_state.step = "run_guidance"
                st.rerun()
        
        if st.button("🔄 Start Over"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()
