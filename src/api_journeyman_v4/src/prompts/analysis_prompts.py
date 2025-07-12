from typing import Dict

def get_project_analysis_prompt(file_contents: Dict[str, str]) -> str:
    file_previews = "\n\n".join([f"### File: {path}\n```\n{content[:500]}\n```" for path, content in file_contents.items()])
    return f"""
You are an expert software architect. Analyze the following file previews from a user's project to determine its key characteristics.

{file_previews}

Based on these files, you must determine the following:
1.  `language`: The primary programming language (e.g., "Python", "JavaScript", "TypeScript").
2.  `framework`: The main framework, if any (e.g., "Flask", "React", "Express", "None").
3.  `style`: The coding style (e.g., "Object-Oriented with classes", "Functional with async/await", "Procedural").
4.  `relevant_files`: A list of 1-3 file paths that are the best places to add new API client code or configuration.

Respond with a single, valid JSON object containing these four keys.
"""

def get_service_analysis_prompt(docs_content: str, service_name: str) -> str:
    return f"""
You are a documentation analyst for '{service_name}'. Read the provided documentation and extract the essential setup information.

You must extract:
1.  `base_url`: The base URL for the API.
2.  `auth_method`: A clear description of the authentication method (e.g., "Bearer Token in Authorization header", "API Key in x-api-key header").

Documentation Content Snippet:
---
{docs_content}
---

Respond with a single, valid JSON object containing "base_url" and "auth_method".
"""
