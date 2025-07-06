# Resume AI Co-Pilot

An intelligent AI-powered resume analysis and interview preparation tool built with LangGraph and Streamlit.

## 🎯 Project Overview

The Resume AI Co-Pilot helps job seekers optimize their resumes and prepare for interviews through intelligent conversation. Users upload their resume and optionally a job description, then ask natural language questions to get personalized feedback and guidance.

## 🏗️ Architecture

### Multi-Agent System
The application uses a LangGraph-powered multi-agent architecture where specialized AI agents handle different tasks:

- **Router Agent**: Classifies user intent and directs workflow
- **Analysis Agent**: Provides detailed resume vs job description analysis
- **Quiz Agent**: Generates personalized interview questions
- **Rewriter Agent**: Improves specific resume sections
- **Formatter Agent**: Formats responses for user-friendly display

### Dual LLM Strategy
- **Gemini Flash**: Fast routing and simple tasks
- **Gemini Pro**: High-quality analysis and complex reasoning

## 📁 Project Structure

```
src/
├── core/           # Agent logic (6 files)
├── prompts/        # LLM prompts (6 files)
├── ui/             # User interface (2 files)
├── workflow/       # LangGraph setup (1 file)
├── config/         # LLM configuration (1 file)
├── types/          # Type definitions (1 file)
└── utils/          # Debug/testing (2 files)
```

## 🚀 Key Features

### Resume Analysis
- Compare resume against job descriptions
- Identify keyword gaps and skill mismatches
- Assess ATS compatibility
- Provide actionable improvement suggestions

### Interview Preparation
- Generate personalized behavioral questions
- Base questions on actual resume content
- Focus on specific experiences and achievements

### Resume Improvements
- Rewrite specific sections with stronger action verbs
- Add quantifiable metrics and achievements
- Improve clarity and impact

### Document Processing
- Support for PDF, DOCX, and TXT files
- Automatic text extraction
- Error handling and validation

## 🛠️ Technology Stack

- **Backend**: Python, LangGraph, LangChain
- **AI Models**: Google Gemini (Flash & Pro)
- **Frontend**: Streamlit
- **Document Processing**: PyPDF2, python-docx
- **State Management**: TypedDict for type safety

## 🎯 User Experience

### Think Mode Toggle
Users can choose between:
- **Fast Mode**: Quick responses using Gemini Flash
- **Think Mode**: High-quality analysis using Gemini Pro

### Real-time Streaming
- Character-by-character response streaming
- Visual progress indicators
- Smooth user experience

### Conversation Memory
- Maintains conversation history
- Context-aware responses
- Follow-up question handling

## 🔧 Development Principles

### Modular Architecture
- **Separation of Concerns**: Each module has a specific responsibility
- **Easy Maintenance**: Small, focused files (150-200 lines max)
- **Clear Dependencies**: Explicit imports and dependencies

### Error Handling
- Comprehensive fallback mechanisms
- Graceful degradation when LLM fails
- User-friendly error messages

### Type Safety
- TypedDict for state management
- Clear type definitions
- Better code reliability

## 📊 Benefits of Organized Structure

### Before vs After
- **Before**: 4 large files (200+ lines each)
- **After**: 19 focused modules (average 60 lines each)

### Maintainability
- Easy to find and modify specific functionality
- Clear module boundaries
- Reduced cognitive load

### Scalability
- New features can be added without affecting existing code
- Individual modules can be tested in isolation
- Multiple developers can work on different modules

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Test the Setup**
   ```bash
   python run.py --test
   ```

4. **Run the Application**
   ```bash
   python run.py --app
   ```

## 🎯 Use Cases

### Resume Analysis
User uploads resume and job description, then asks: "Analyze my resume for this software engineering role"

### Interview Questions
User uploads resume and asks: "Generate interview questions based on my experience"

### Resume Improvements
User uploads resume and asks: "Rewrite this bullet point: 'Managed projects'"

## 🔮 Future Enhancements

- Unit tests for each module
- Comprehensive logging system
- Performance monitoring
- Additional document formats
- Export functionality
- Integration with job boards

---

**Built with ❤️ using LangGraph and Streamlit**
