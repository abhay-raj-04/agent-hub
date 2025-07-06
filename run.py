#!/usr/bin/env python3
"""
Simple run script for Resume AI Co-Pilot
This script provides easy access to all the main functionality
"""

import sys
import os

def show_help():
    """Show help information"""
    print("🚀 Resume AI Co-Pilot - Organized Structure")
    print("=" * 50)
    print()
    print("📁 Project Structure:")
    print("├── src/                    # Main source code")
    print("│   ├── core/              # Agent logic (6 files)")
    print("│   ├── prompts/           # LLM prompts (6 files)")
    print("│   ├── ui/                # User interface (2 files)")
    print("│   ├── workflow/          # LangGraph setup (1 file)")
    print("│   ├── config/            # LLM configuration (1 file)")
    print("│   ├── types/             # Type definitions (1 file)")
    print("│   └── utils/             # Debug/testing (2 files)")
    print("├── main.py                # Main entry point")
    print("└── requirements.txt       # Dependencies")
    print()
    print("🎯 Available Commands:")
    print("1. python run.py --app          # Run main Streamlit app")
    print("2. python run.py --streaming    # Run streaming version")
    print("3. python run.py --test         # Test LLM integration")
    print("4. python run.py --debug        # Debug router logic")
    print("5. python run.py --help         # Show this help")
    print()
    print("📊 File Organization:")
    print("• Total files: 19 (was 4 large files)")
    print("• Average file size: ~60 lines (was 200+ lines)")
    print("• Clear separation of concerns")
    print("• Easy to maintain and extend")
    print()
    print("🔧 Quick Start:")
    print("1. Install: pip install -r requirements.txt")
    print("2. Set API key: Create .env file with GOOGLE_API_KEY")
    print("3. Test: python run.py --test")
    print("4. Run: python run.py --app")

def run_app():
    """Run the main Streamlit app"""
    print("🚀 Starting Resume AI Co-Pilot...")
    os.system("streamlit run main.py")

def run_streaming():
    """Run the streaming version"""
    print("🚀 Starting Resume AI Co-Pilot (Streaming)...")
    os.system("streamlit run src/ui/streamlit_app_streaming.py")

def run_test():
    """Run LLM integration test"""
    print("🧪 Testing LLM Integration...")
    os.system("python main.py --test-gemini")

def run_debug():
    """Run router debug"""
    print("🔍 Debugging Router Logic...")
    os.system("python main.py --debug-router")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "--app":
        run_app()
    elif command == "--streaming":
        run_streaming()
    elif command == "--test":
        run_test()
    elif command == "--debug":
        run_debug()
    elif command == "--help":
        show_help()
    else:
        print(f"❌ Unknown command: {command}")
        print("Use --help to see available commands")

if __name__ == "__main__":
    main() 