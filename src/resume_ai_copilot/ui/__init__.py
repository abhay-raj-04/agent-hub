# UI module for Resume AI Co-Pilot

from .streamlit_app import main as streamlit_main
from .streamlit_app_streaming import main as streamlit_streaming_main

__all__ = ['streamlit_main', 'streamlit_streaming_main'] 