# Resume AI Co-Pilot - Setup Guide

## Prerequisites

### 1. Python Environment
- **Python 3.8+** (recommended: Python 3.9 or 3.10)
- **Virtual Environment** (recommended for isolation)

### 2. Required Dependencies
All dependencies are listed in `requirements.txt`:
```
streamlit
langchain
langgraph
langchain-google-genai
pypdf
python-docx
PyPDF2
```

### 3. Google AI API Access
- **Google AI Studio Account** (free tier available)
- **API Key** for Gemini models
- **Models Used:**
  - `gemini-2.5-flash` (for routing - fast)
  - `gemini-2.5-pro` (for analysis, quiz, rewriting - high quality)

### 4. File Structure
Ensure you have these files in your project:
```
agent-hub/
├── README.md
├── start.md
├── requirements.txt
├── agent_core.py
├── langgraph_setup.py
├── streamlit_app.py
└── prompts/ (optional - for future prompt management)
```

## Setup Instructions

### Step 1: Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Google AI API Configuration
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Set environment variable:
```bash
# Windows:
set GOOGLE_API_KEY=your_api_key_here

# macOS/Linux:
export GOOGLE_API_KEY=your_api_key_here
```

### Step 3: Test Files Preparation
For testing, prepare:
- **Sample Resume** (PDF or DOCX format)
- **Sample Job Description** (PDF, DOCX, or TXT format)

## Running the Application

### Start the Streamlit App
```bash
streamlit run streamlit_app.py
```

### Access the Application
- Open your browser to: `http://localhost:8501`
- The app will load with a clean, responsive interface

## Testing the Workflow

### 1. Initial Setup
- Upload a resume file (PDF/DOCX)
- Upload a job description file (PDF/DOCX/TXT)
- Verify files are processed successfully

### 2. Test Different Queries
Try these example queries to test the routing:

**Analysis:**
- "Analyze my resume for this job"
- "How does my resume match this position?"

**Interview Questions:**
- "Generate interview questions"
- "Give me some interview questions based on my resume"

**Resume Rewriting:**
- "Rewrite this bullet point: 'Managed projects'"
- "Improve this section of my resume"

**General:**
- "Hello" (should trigger greeting)
- "What can you do?" (should show capabilities)

### 3. Expected Behavior
- **Mock Mode:** Currently returns sample responses
- **Routing:** Should correctly identify user intent
- **Error Handling:** Should prompt for missing documents
- **UI:** Should be responsive and user-friendly

## Current Status

### ✅ Implemented
- Multi-agent LangGraph workflow
- Streamlit UI with file uploads and chat
- Mock responses for all agent nodes
- Document parsing (PDF/DOCX/TXT)
- State management and conversation history

### 🔄 Next Steps (After Testing)
- Integrate real Gemini LLM calls
- Refine prompts for better quality
- Add error handling improvements
- UI/UX polish

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt
```

**2. API Key Issues**
```bash
# Verify environment variable is set
echo $GOOGLE_API_KEY  # macOS/Linux
echo %GOOGLE_API_KEY% # Windows
```

**3. Port Already in Use**
```bash
# Kill existing Streamlit process or use different port
streamlit run streamlit_app.py --server.port 8502
```

**4. File Upload Issues**
- Ensure files are in supported formats (PDF, DOCX, TXT)
- Check file size (recommended < 10MB)

## Development Notes

### Architecture
- **LangGraph:** Orchestrates multi-agent workflow
- **Streamlit:** Provides responsive web interface
- **State Management:** Maintains conversation context
- **Document Processing:** Handles multiple file formats

### Privacy & Security
- **No Data Storage:** All data is session-only (in-memory)
- **File Processing:** Documents are processed locally
- **API Calls:** Only when real LLM integration is added

### Performance
- **Mock Mode:** Fast responses (< 1 second)
- **Real LLM Mode:** Expected 10-15 seconds per response
- **File Processing:** Depends on file size and complexity

## Ready to Start?

1. ✅ Complete environment setup
2. ✅ Install dependencies
3. ✅ Configure API key (for future LLM integration)
4. ✅ Prepare test files
5. 🚀 Run `streamlit run streamlit_app.py`
6. 🧪 Test the workflow with sample queries

**The application is ready for testing in mock mode!** 