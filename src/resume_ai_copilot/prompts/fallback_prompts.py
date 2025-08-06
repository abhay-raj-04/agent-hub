def get_fallback_analysis_report() -> str:
    """Fallback analysis report when LLM is unavailable."""
    return (
        "# Resume Analysis Report (Fallback Output)\n"
        "## 1. Keyword Alignment\n"
        "- The resume uses some keywords from the job description, but could add more such as 'collaboration', 'agile', and 'cloud'.\n"
        "\n## 2. ATS Friendliness\n"
        "- The formatting is simple and clear. Bullet points are used appropriately.\n"
        "\n## 3. Impact & Quantifiable Achievements\n"
        "- Some achievements are quantified, but more metrics would strengthen the resume.\n"
        "\n## 4. Clarity & Conciseness\n"
        "- The language is mostly clear, but a few sentences could be more concise.\n"
        "\n## 5. Skill Gaps\n"
        "- The resume could better highlight skills in project management and cloud technologies.\n"
        "\n## 6. Overall Impression\n"
        "- Strong technical background, but could improve keyword alignment and add more quantifiable results.\n"
    )

def get_fallback_quiz_questions() -> list:
    """Fallback questions when LLM is unavailable."""
    return [
        "1. Tell me about a time when you led a project from start to finish. What challenges did you face and how did you overcome them?",
        "2. Describe a situation where you had to quickly learn a new technology or tool to complete a task.",
        "3. How have you contributed to improving team collaboration or communication in your previous roles?",
        "4. Can you give an example of how you handled a difficult stakeholder or client request?",
        "5. What is an achievement from your resume that you are most proud of, and why?",
        "6. Tell me about a time you made a mistake at work. How did you handle it and what did you learn?",
    ]

def get_fallback_rewrite_response() -> str:
    """Fallback rewrite response when LLM is unavailable."""
    return (
        "**Rewritten Version 1:**\n"
        "- Led cross-functional teams to deliver projects on time, resulting in a 20% increase in client satisfaction.\n"
        "\n**Rewritten Version 2:**\n"
        "- Managed multiple projects simultaneously, consistently meeting deadlines and improving team efficiency by 15%.\n"
        "\n**Why these are better:**\n"
        "- Use strong action verbs (Led, Managed)\n"
        "- Quantify impact (20% increase, 15% improvement)\n"
        "- More specific and results-oriented\n"
    ) 