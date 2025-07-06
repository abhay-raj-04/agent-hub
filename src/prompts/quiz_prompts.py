def get_quiz_prompt_standard(resume: str) -> str:
    """
    Generate standard quiz prompt for interview questions.
    """
    return f"""
You are a seasoned hiring manager creating interview questions. Your task is to generate 5-7 unique and insightful interview questions directly based on the user's resume. Focus on behavioral questions that require the user to elaborate on their experiences, skills, and achievements.

RESUME:
{resume}

INSTRUCTIONS:
- Generate questions that cannot be answered with a simple "yes/no".
- Focus on past experiences: "Tell me about a time when...", "Describe a situation where...", "How did you handle...".
- Use specific keywords or projects mentioned in the resume to make questions highly personalized.
- If the resume mentions team leadership, ask about challenges in leadership. If it mentions a specific project, ask about their role and outcome.
- Output the questions as a numbered list.

Generate 5-7 behavioral interview questions based on this resume:
"""

def get_quiz_prompt_followup(user_query: str, resume: str, conversation_history: list) -> str:
    """
    Generate follow-up quiz prompt for related questions.
    """
    return f"""
You are a seasoned hiring manager. The user is asking follow-up questions about previous interview questions. Generate 5-7 additional related questions that build upon or explore the same themes.

USER QUERY: {user_query}
RESUME: {resume}
RECENT CONVERSATION: {conversation_history[-4:] if len(conversation_history) >= 4 else conversation_history}

INSTRUCTIONS:
- Generate follow-up questions related to the user's request
- If they ask about "question 1", generate questions about the same topic
- If they ask for "10 questions", generate exactly 10 questions
- Focus on the same themes and skills mentioned in the resume
- Output the questions as a numbered list.

Generate follow-up interview questions based on this request:
""" 