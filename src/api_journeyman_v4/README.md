# API Journeyman V4: The Integration Co-Pilot

This AI agent acts as an expert partner for integrating third-party services into your existing codebase. It understands your project's language and structure, analyzes the service you want to add, and provides context-aware guidance and code generation.

## Key Features

*   **Project-Awareness:** Scans your local project folder to understand its language, frameworks, and coding patterns.
*   **Interactive Folder Selection:** Browse and select your project folder using an intuitive file dialog, or enter the path manually.
*   **Smart Folder Exclusion:** Exclude unnecessary folders (like `node_modules`, `__pycache__`, `.git`) from analysis with one-click toggles.
*   **Autonomous Service Analysis:** Automatically finds and analyzes API documentation for any service, just from its name.
*   **Parallel Processing:** Concurrently analyzes your project and the service documentation for faster results.
*   **Interactive Guidance:** Presents a summary of its findings and lets you choose your next step.
*   **Multi-Language, Contextual Code Generation:** Generates code that matches your project's style and provides instructions on where to place it.
*   **Enhanced UI Experience:** Modern, intuitive interface with progress indicators, validation, and helpful examples.

## Setup & Installation

1.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    You will also need to install Playwright's browser drivers for web scraping:
    ```bash
    playwright install
    ```

3.  **Set up environment variables:**
    *   Copy the `.env.example` file to a new file named `.env`.
    *   Fill in your `GOOGLE_API_KEY` and `TAVILY_API_KEY`. You can get a free Tavily key from [tavily.com](https://tavily.com).

4.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

## How to Use

1. **📂 Select Your Project**: Use the browse button or manually enter your project folder path
2. **🚫 Exclude Unnecessary Folders**: Toggle folders like `node_modules`, `__pycache__`, `.git` to exclude them from analysis
3. **🔌 Choose Your Service**: Enter the name of any service you want to integrate (Stripe, Twilio, OpenAI, etc.)
4. **🤖 Get AI-Powered Results**: Choose between step-by-step guides or direct code generation
5. **📥 Download & Implement**: Download the generated code and follow the integration guidance
