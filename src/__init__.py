# Resume AI Co-Pilot - Main Package

from .resume_ai_copilot.types.state import ResumeCoPilotState
from .resume_ai_copilot.core import *
from .resume_ai_copilot.workflow import app, create_workflow
from .resume_ai_copilot.ui import streamlit_main, streamlit_streaming_main
from .resume_ai_copilot.utils import debug_router, test_gemini

__version__ = "1.0.0"
__author__ = "Resume AI Co-Pilot Team"

__all__ = [
    'ResumeCoPilotState',
    'app',
    'create_workflow',
    'streamlit_main',
    'streamlit_streaming_main',
    'debug_router',
    'test_gemini'
]

# This __init__.py marks the src directory as a package.
# Submodules for each AI agent (e.g., resume_ai_copilot) should be placed here. 