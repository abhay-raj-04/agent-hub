#!/usr/bin/env python3
"""
Main entry point for Resume AI Co-Pilot
This file provides easy access to all the main functionality
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.streamlit_app import main as streamlit_main
from src.utils.debug_router import debug_router
from src.utils.test_gemini import test_gemini

def main():
    """Main entry point"""
    print("🚀 Resume AI Co-Pilot")
    print("=" * 30)
    print("Available commands:")
    print("1. streamlit run main.py --server.port 8501")
    print("2. python main.py --test-gemini")
    print("3. python main.py --debug-router")
    print()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "--test-gemini":
            test_gemini()
        elif command == "--debug-router":
            debug_router()
        elif command == "--streamlit":
            streamlit_main()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: --test-gemini, --debug-router, --streamlit")
    else:
        print("Starting Streamlit app...")
        streamlit_main()

if __name__ == "__main__":
    main() 