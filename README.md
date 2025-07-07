# Agent Hub

A modular hub for AI agents. Each agent is organized in its own folder under `src/` and can be deployed independently (e.g., on Streamlit Cloud).

## Available Agents

| Agent Name         | Description                        | Folder                | Deploy Path                  |
|--------------------|------------------------------------|-----------------------|------------------------------|
| Resume AI Copilot  | Resume analysis, interview prep, etc. | src/resume_ai_copilot | src/resume_ai_copilot/main.py|

## How to Add a New Agent
1. Copy the folder structure of `resume_ai_copilot` to a new folder under `src/` (e.g., `src/your_new_agent`).
2. Implement your agent logic, UI, etc.
3. Add a `main.py` in the new agent folder as an entry point for deployment.
4. Add a `README.md` for the new agent.
5. Add the agent to the table above.

## How to Deploy an Agent (Streamlit Cloud)
- Set the **main file path** to the agent's entry point (e.g., `src/resume_ai_copilot/main.py`).
- Set environment variables (e.g., `GOOGLE_API_KEY`) in the app settings.

## Project Structure
```
agent-hub/
├── src/
│   ├── resume_ai_copilot/
│   │   ├── main.py
│   │   ├── README.md
│   │   └── ...
│   ├── your_new_agent/
│   │   ├── main.py
│   │   ├── README.md
│   │   └── ...
│   └── ...
├── requirements.txt
├── README.md
└── ...
```

## Local Development
```bash
pip install -r requirements.txt
cd src/resume_ai_copilot
streamlit run main.py
```

---

For more details, see each agent's README in its folder.
