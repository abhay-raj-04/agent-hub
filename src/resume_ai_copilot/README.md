# Resume AI Copilot

A powerful AI agent for resume analysis, job description matching, interview question generation, and resume rewriting. Supports PDF, DOCX, TXT, and image (PNG, JPG, JPEG) uploads with OCR.

## Features
- Resume analysis against job descriptions
- Personalized interview question generation
- Resume rewriting and improvement suggestions
- ATS optimization tips
- Supports PDF, DOCX, TXT, PNG, JPG, JPEG (with OCR)

## Usage

### Local Development
```bash
pip install -r ../../requirements.txt
streamlit run main.py
```

### Deployment (Streamlit Cloud)
- Set the main file path to:
  ```
  src/resume_ai_copilot/main.py
  ```
- Set environment variables (e.g., `GOOGLE_API_KEY`) in the app settings.

## Example Queries
- "Analyze my resume for this software engineering role."
- "Generate interview questions based on my experience."
- "Rewrite this bullet point: 'Managed projects'"

## Folder Structure
```
resume_ai_copilot/
├── main.py           # Entry point for deployment
├── core/             # Core logic
├── prompts/          # Prompt templates
├── ui/               # Streamlit UI
├── workflow/         # Workflow setup
├── config/           # LLM config
├── types/            # State types
├── utils/            # Utilities
└── README.md         # This file
``` 