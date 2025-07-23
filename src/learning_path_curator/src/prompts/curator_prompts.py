def get_deconstructor_prompt(learning_goal: str, experience_level: str) -> str:
    return f"""
You are an expert curriculum designer. Your task is to deconstruct a high-level learning goal into a structured, hierarchical list of topics.
The user's goal is: **"{learning_goal}"**
Their experience level is: **{experience_level}**

Create a dependency graph of topics, starting from the most fundamental and moving to more advanced concepts.
Group topics into logical categories (e.g., "Foundations", "Core Concepts", "Advanced Topics", "Tools & Ecosystem").

Respond with a single, valid JSON object. The keys should be the categories, and the values should be a list of specific, searchable topic strings.
Example for "Learn Python for Data Science" as a "Beginner":
{{
  "1. Python Foundations": ["Python Syntax and Data Types", "Control Flow (if/else, loops)", "Functions and Modules"],
  "2. Core Data Science Libraries": ["NumPy for numerical data", "Pandas for data manipulation", "Matplotlib and Seaborn for data visualization"],
  "3. Introduction to Machine Learning": ["Scikit-Learn basics", "Supervised Learning Concepts (Regression, Classification)", "Model Training and Evaluation"],
  "4. Essential Tools": ["Jupyter Notebooks", "Git and GitHub for version control"]
}}

Now, create the JSON for the user's request.
"""

def get_evaluator_prompt(topic: str, resource_title: str, content_snippet: str) -> str:
    return f"""
You are a resource quality analyst. Evaluate the following learning resource based on a snippet of its content.

- Topic: **{topic}**
- Resource Title: **{resource_title}**

Content Snippet:
---
{content_snippet}
---

Your task is to provide a quality score and a difficulty level.
- `quality_score`: An integer from 1 (very low quality, spammy) to 10 (excellent, clear, authoritative).
- `difficulty_level`: A string, either "Beginner", "Intermediate", or "Advanced".
- `format`: A string, either "Video", "Article", "Interactive Tutorial", "Documentation", or "Other".

Respond with a single, valid JSON object containing these three keys.
"""

def get_sequencer_prompt(evaluated_resources: dict, learning_goal: str, experience_level: str) -> str:
    # We'll format the resources nicely for the prompt context
    resources_text = ""
    for topic, resources in evaluated_resources.items():
        resources_text += f"### Topic: {topic}\n"
        for res in resources:
            resources_text += f"- Title: {res['title']}, URL: {res['url']}, Quality: {res['quality_score']}/10, Level: {res['difficulty_level']}, Format: {res['format']}\n"
        resources_text += "\n"

    return f"""
You are an expert curriculum creator. Your task is to design a personalized, week-by-week learning path using a pre-vetted list of resources.

- User's Goal: **{learning_goal}**
- User's Experience Level: **{experience_level}**

Available Resources:
---
{resources_text}
---

### Instructions:
1.  Create a structured learning plan, broken down by weeks (e.g., "Week 1-2: Foundations").
2.  For each topic in your plan, select the **single best resource** from the provided list.
3.  Prioritize resources that match the user's experience level. For a beginner, choose resources marked "Beginner" for foundational topics.
4.  If multiple good resources exist for a topic, prefer higher quality scores. A mix of formats (e.g., a video followed by an article) is good.
5.  Organize the output in clean, readable Markdown. Provide the title of the resource as a clickable link.
6.  Start with a brief motivational introduction. End with a concluding remark about next steps.
"""
