def get_analysis_prompt(resume: str, jd: str = "", user_query: str = "") -> str:
    """Generates analysis prompt for resume review."""
    return f"""
You are an expert career coach and resume analyst. Your task is to provide a comprehensive, actionable analysis of the provided resume in the context of the job description. Focus on alignment, ATS-friendliness, impact, and clarity.

USER REQUEST: {user_query}

RESUME:
{resume}

JOB DESCRIPTION:
{jd}

ANALYSIS_AREAS:
1. Keyword Alignment: How well does the resume use keywords from the job description? Suggest missing/weak keywords.
2. ATS Friendliness: Is the formatting simple, clear, and easy for an Applicant Tracking System to parse? (e.g., bullet points, standard sections).
3. Impact & Quantifiable Achievements: Are achievements quantified with numbers/metrics? Are action verbs strong? Provide examples of how to improve specific points.
4. Clarity & Conciseness: Is the language clear and concise? Avoid jargon where possible.
5. Skill Gaps: Based on the JD, what key skills seem underrepresented or missing from the resume?
6. Overall Impression: A brief summary of the resume's strengths and weaknesses.

INSTRUCTIONS: 
- Address the user's specific request or concerns mentioned in their query
- If the user asks for specific focus areas, prioritize those in your analysis
- Keep your response concise and directly relevant to the user's needs
- If the user asks for a brief analysis, provide a summary; if they ask for detailed feedback, be comprehensive

FORMATTING: Provide your response in clear, concise markdown. Use headings for each section. Keep it professional and encouraging.
""" 