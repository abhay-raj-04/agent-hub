def get_welcome_message() -> str:
    """
    Get the welcome message for new users.
    """
    return (
        "👋 **Welcome to Resume AI Co-Pilot!**\n\n"
        "I'm here to help you optimize your resume and prepare for interviews. Here's what I can do:\n\n"
        "📊 **Resume Analysis** - Compare your resume against job descriptions\n"
        "🎯 **Interview Questions** - Generate personalized questions based on your experience\n"
        "✏️ **Resume Improvements** - Rewrite and enhance specific sections\n"
        "📋 **ATS Optimization** - Ensure your resume passes Applicant Tracking Systems\n\n"
        "To get started, please upload your resume using the sidebar. You can also upload a job description for targeted analysis.\n\n"
        "What would you like to work on today?"
    )

def get_greeting_response() -> str:
    """
    Get greeting response for general queries.
    """
    return (
        "Hello! I'm your Resume AI Co-Pilot. I can help you:\n\n"
        "• Analyze your resume against job descriptions\n"
        "• Generate interview questions based on your experience\n"
        "• Improve and rewrite resume sections\n"
        "• Optimize for ATS systems\n\n"
        "Please upload your resume to get started!"
    )

def get_missing_resume_message() -> str:
    """
    Get message when resume is missing.
    """
    return (
        "📄 **Resume Required**\n\n"
        "I need your resume to help you effectively. Please upload your resume (.pdf or .docx) using the sidebar.\n\n"
        "Once uploaded, I can:\n"
        "• Analyze it against job descriptions\n"
        "• Generate interview questions\n"
        "• Suggest improvements\n"
        "• Help with ATS optimization"
    )

def get_missing_jd_message() -> str:
    """
    Get message when job description is missing for analysis.
    """
    return (
        "📋 **Job Description Required**\n\n"
        "To provide a targeted analysis, I need both your resume and the job description. Please upload the job description (.pdf, .docx, or .txt) using the sidebar.\n\n"
        "This will help me:\n"
        "• Compare your skills with job requirements\n"
        "• Identify keyword gaps\n"
        "• Suggest specific improvements\n"
        "• Ensure ATS compatibility"
    )

def get_error_message() -> str:
    """
    Get generic error message.
    """
    return (
        "❌ **Something went wrong**\n\n"
        "I encountered an error processing your request. Please try again, or if the problem persists, check that:\n\n"
        "• Your resume is properly uploaded\n"
        "• Your internet connection is stable\n"
        "• The file formats are supported (.pdf, .docx, .txt)\n\n"
        "Feel free to ask me anything else!"
    ) 