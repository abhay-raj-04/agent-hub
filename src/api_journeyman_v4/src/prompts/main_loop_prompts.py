def get_planner_prompt(docs_content: str, user_goal: str) -> str:
    return f"""
You are an expert API planner. Your job is to analyze API documentation and a user's goal to create a plan for an API call.
You must respond with a single, valid JSON object containing `method`, `endpoint`, and a dictionary of `parameters`.

User's Goal: "{user_goal}"

Relevant API Documentation Snippet:
---
{docs_content}
---

Based on the goal and the documentation, determine the correct HTTP method, endpoint path, and extract any parameters from the user's goal.
Your output must be only the JSON object.
"""
