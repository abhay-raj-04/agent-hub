# The Personalized Learning Path Curator

An AI agent that transforms your ambitious learning goals into a structured, step-by-step curriculum. It finds the best resources on the web, evaluates them, and organizes them into a personalized weekly plan to guide your learning journey.

## How It Works

1.  **Goal Deconstruction:** You provide a high-level goal (e.g., "Learn web development") and your current experience level. The agent breaks this down into a graph of necessary skills.
2.  **Resource Discovery:** It scours the web for high-quality articles, videos, and tutorials for each skill.
3.  **Content Evaluation:** It analyzes the content of each resource to determine its quality and difficulty.
4.  **Curriculum Sequencing:** It selects the best resource for each topic and arranges them into a logical, week-by-week learning path tailored to you.
5.  **Plan Presentation:** It delivers a clean, actionable markdown file you can follow.

## Setup & Installation

1.  **Create and activate a virtual environment.**
2.  **Install dependencies:** `pip install -r requirements.txt`
3.  **Install Playwright browsers:** `playwright install`
4.  **Set up environment variables:** Copy `.env.example` to `.env` and fill in your `GOOGLE_API_KEY` and `TAVILY_API_KEY`.
5.  **Run the application:** `streamlit run main.py`
