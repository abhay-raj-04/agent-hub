# Template Agent

This is a minimal template for creating a new agent in the Agent Hub.

## How to Use
- Copy this folder and rename it for your new agent (e.g., `src/my_new_agent`).
- Edit `main.py` to build your agent's UI and logic.
- Add any subfolders (core, prompts, etc.) as needed.
- Update this README with your agent's details.

## Local Development
```bash
pip install -r ../../requirements.txt
streamlit run main.py
```

## Deployment (Streamlit Cloud)
- Set the main file path to:
  ```
  src/template_agent/main.py
  ```
- Set environment variables as needed in the app settings.

## Example
This template just shows a title and a message. Replace it with your own logic! 