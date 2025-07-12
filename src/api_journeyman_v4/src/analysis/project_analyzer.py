import json
from pathlib import Path
from src.types.state import JourneymanState
from src.config.llm_config import get_llm
from src.prompts.analysis_prompts import get_project_analysis_prompt

def analyze_project_code_node(state: JourneymanState):
    print("--- [Analysis] Starting Project Code Analysis ---")
    project_path = Path(state['project_path'])
    file_contents = {}
    file_limit = 10 # Avoid scanning huge projects
    
    # Get excluded folders from state (if any)
    excluded_folders = state.get('excluded_folders', [])
    print(f"Excluded folders: {excluded_folders}")

    try:
        for p in project_path.rglob('*.*'): # Scan for any file with an extension
            # Check if any part of the path contains excluded folders
            path_parts = p.parts
            should_skip = False
            
            for part in path_parts:
                if part in excluded_folders or part.startswith('.') or part == '__pycache__':
                    should_skip = True
                    break
            
            if should_skip:
                continue
                
            if p.is_file():
                try:
                    with open(p, 'r', encoding='utf-8') as f:
                        file_contents[str(p.relative_to(project_path))] = f.read()
                    if len(file_contents) >= file_limit:
                        break
                except Exception:
                    continue # Skip binary files etc.

        if not file_contents:
            raise ValueError("No readable files found in the specified project path.")

        llm = get_llm()
        prompt = get_project_analysis_prompt(file_contents)
        response = llm.invoke(prompt)
        
        cleaned = response.content.strip().replace("```json", "").replace("```", "")
        state['project_analysis'] = json.loads(cleaned)

    except Exception as e:
        state['error_message'] = f"Error analyzing project: {str(e)}"
    return state
