# Resume AI Co-Pilot - Organized Structure

A comprehensive AI-powered resume analysis and interview preparation tool built with LangGraph and Streamlit.

## 🏗️ Project Structure

```
agent-hub/
├── src/                          # Main source code
│   ├── core/                     # Core agent logic
│   │   ├── __init__.py
│   │   ├── document_ingestion.py # Document processing
│   │   ├── router.py             # Intent classification
│   │   ├── analyzer.py           # Resume analysis
│   │   ├── quiz_generator.py     # Interview questions
│   │   ├── rewriter.py           # Resume improvements
│   │   └── formatter.py          # Response formatting
│   ├── prompts/                  # All prompt templates
│   │   ├── __init__.py
│   │   ├── router_prompts.py     # Routing prompts
│   │   ├── analysis_prompts.py   # Analysis prompts
│   │   ├── quiz_prompts.py       # Quiz generation prompts
│   │   ├── rewrite_prompts.py    # Rewrite prompts
│   │   ├── fallback_prompts.py   # Fallback responses
│   │   └── system_prompts.py     # System messages
│   ├── ui/                       # User interface
│   │   ├── __init__.py
│   │   ├── streamlit_app.py      # Main UI
│   │   └── streamlit_app_streaming.py # Streaming UI
│   ├── workflow/                 # LangGraph workflow
│   │   ├── __init__.py
│   │   └── langgraph_setup.py   # Workflow configuration
│   ├── config/                   # Configuration
│   │   ├── __init__.py
│   │   └── llm_config.py        # LLM configuration
│   ├── types/                    # Type definitions
│   │   ├── __init__.py
│   │   └── state.py             # State management
│   ├── utils/                    # Utilities
│   │   ├── __init__.py
│   │   ├── debug_router.py      # Router debugging
│   │   └── test_gemini.py       # LLM testing
│   └── __init__.py              # Main package init
├── main.py                      # Main entry point
├── requirements.txt              # Dependencies
├── README.md                    # Original README
└── README_ORGANIZED.md          # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
Create a `.env` file in the root directory:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Test LLM Integration
```bash
python main.py --test-gemini
```

### 4. Run the Application
```bash
streamlit run main.py
```

## 📁 Module Breakdown

### Core Module (`src/core/`)
- **document_ingestion.py**: Handles PDF/DOCX file parsing
- **router.py**: Classifies user intent using LLM
- **analyzer.py**: Performs resume analysis with streaming support
- **quiz_generator.py**: Generates interview questions
- **rewriter.py**: Improves resume sections
- **formatter.py**: Formats responses for UI

### Prompts Module (`src/prompts/`)
- **router_prompts.py**: Intent classification prompts
- **analysis_prompts.py**: Resume analysis prompts
- **quiz_prompts.py**: Interview question generation
- **rewrite_prompts.py**: Resume improvement prompts
- **fallback_prompts.py**: Error fallback responses
- **system_prompts.py**: System messages and greetings

### UI Module (`src/ui/`)
- **streamlit_app.py**: Main Streamlit interface
- **streamlit_app_streaming.py**: Real-time streaming interface

### Workflow Module (`src/workflow/`)
- **langgraph_setup.py**: LangGraph workflow configuration

### Config Module (`src/config/`)
- **llm_config.py**: LLM initialization and configuration

### Types Module (`src/types/`)
- **state.py**: TypedDict for state management

### Utils Module (`src/utils/`)
- **debug_router.py**: Router debugging utilities
- **test_gemini.py**: LLM testing utilities

## 🔧 Key Features

### 1. Modular Architecture
- **Separation of Concerns**: Each module has a specific responsibility
- **Easy Maintenance**: Small, focused files (150-200 lines max)
- **Clear Dependencies**: Explicit imports and dependencies

### 2. Dual LLM Strategy
- **Gemini Flash**: Fast routing and simple tasks
- **Gemini Pro**: High-quality analysis and complex tasks
- **Think Mode Toggle**: User can choose between speed and quality

### 3. Streaming Support
- **Real-time Responses**: Character-by-character streaming
- **Progress Indicators**: Visual feedback during processing
- **Fallback Handling**: Graceful error recovery

### 4. Document Processing
- **Multi-format Support**: PDF, DOCX, TXT files
- **Auto-processing**: Automatic text extraction
- **Error Handling**: Robust file processing

## 🎯 Usage Examples

### Resume Analysis
```
User: "Analyze my resume for this software engineering role"
→ Router: ANALYZE
→ Analyzer: Comprehensive resume vs JD analysis
```

### Interview Questions
```
User: "Generate interview questions based on my experience"
→ Router: QUIZ
→ Quiz Generator: Personalized behavioral questions
```

### Resume Improvements
```
User: "Rewrite this bullet point: 'Managed projects'"
→ Router: REWRITE
→ Rewriter: Improved version with metrics
```

## 🛠️ Development

### Adding New Features
1. **Core Logic**: Add to appropriate module in `src/core/`
2. **Prompts**: Create new prompt file in `src/prompts/`
3. **UI**: Update relevant file in `src/ui/`
4. **Workflow**: Modify `src/workflow/langgraph_setup.py`

### Testing
```bash
# Test LLM integration
python main.py --test-gemini

# Debug router logic
python main.py --debug-router

# Run streaming version
streamlit run src/ui/streamlit_app_streaming.py
```

### Code Organization Principles
- **Single Responsibility**: Each file has one clear purpose
- **Dependency Injection**: Clear import structure
- **Error Handling**: Comprehensive fallback mechanisms
- **Type Safety**: TypedDict for state management
- **Documentation**: Clear docstrings and comments

## 📊 File Size Analysis

| Module | Files | Avg Lines | Purpose |
|--------|-------|-----------|---------|
| Core | 6 | ~80 | Agent logic |
| Prompts | 6 | ~40 | LLM prompts |
| UI | 2 | ~150 | User interface |
| Workflow | 1 | ~50 | LangGraph setup |
| Config | 1 | ~30 | LLM config |
| Types | 1 | ~15 | Type definitions |
| Utils | 2 | ~70 | Debug/testing |

**Total**: 19 files, average ~60 lines per file

## 🔄 Migration from Old Structure

The old monolithic files have been broken down:

- `agent_core.py` (407 lines) → 6 core modules (~80 lines each)
- `prompts.py` (247 lines) → 6 prompt modules (~40 lines each)
- `streamlit_app.py` (194 lines) → UI modules (~150 lines each)

## 🎉 Benefits of New Structure

1. **Maintainability**: Easy to find and modify specific functionality
2. **Testability**: Individual modules can be tested in isolation
3. **Scalability**: New features can be added without affecting existing code
4. **Readability**: Smaller files are easier to understand
5. **Collaboration**: Multiple developers can work on different modules
6. **Documentation**: Clear module boundaries and responsibilities

## 🚀 Next Steps

1. **Add Unit Tests**: Create tests for each module
2. **Add Logging**: Implement comprehensive logging
3. **Add Configuration**: Environment-based configuration
4. **Add Monitoring**: Performance and usage metrics
5. **Add CI/CD**: Automated testing and deployment

---

**Note**: This organized structure maintains all original functionality while making the codebase much more maintainable and scalable. 