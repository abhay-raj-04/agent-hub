def get_guidance_prompt(project_analysis: dict, service_analysis: dict) -> str:
    return f"""
You are an expert Integration Co-Pilot. Create a step-by-step markdown guide for a developer to integrate the '{service_analysis['service_name']}' API into their '{project_analysis['language']}' project.

### Project Context:
- Language: {project_analysis['language']}
- Framework: {project_analysis['framework']}
- Suggested Files: {project_analysis['relevant_files']}

### Service Context:
- Service Name: {service_analysis['service_name']}
- Authentication: {service_analysis['auth_method']}

Provide a clear, actionable guide including:
1.  How to securely store the API key (e.g., using environment variables).
2.  Where to create a new API client module (referencing the suggested files).
3.  A basic code skeleton for a function to make an API call, matching the project's language.
"""

def get_context_aware_code_prompt(project_analysis: dict, service_analysis: dict, api_plan: dict, user_goal: str) -> str:
    return f"""
You are an expert Integration Co-Pilot. Your task is to generate a code snippet to integrate an API, perfectly matching the user's existing project.

### Project Context:
- Language: {project_analysis['language']}
- Framework: {project_analysis['framework']}
- Coding Style: {project_analysis['style']}
- Suggested Files for Integration: {project_analysis['relevant_files']}

### Service & Task Context:
- Service Name: {service_analysis['service_name']}
- User's Goal: "{user_goal}"
- API Call Plan: {api_plan}

### Your Instructions:
1.  **Generate the code snippet** in `{project_analysis['language']}` that performs the requested action based on the API Call Plan.
2.  **Match the coding style.** If the project uses `async/await`, use it. If it uses classes, structure your code in a class.
3.  **Include clear instructions** in comments explaining where to place the code, referencing one of the suggested files.
4.  **Demonstrate safe secret handling.** Show how to load the API key from an environment variable (e.g., `os.getenv('{service_analysis['service_name'].upper()}_API_KEY')`), do not hardcode the key itself.
5.  **Provide a complete, ready-to-use block of code.**
"""
