import streamlit as st

def main():
    st.set_page_config(page_title="Template Agent", layout="centered")
    st.title("🤖 Template Agent")
    st.write("This is a template agent. Start building your own agent here!")
    st.info("Edit src/template_agent/main.py and src/template_agent/README.md to get started.")

if __name__ == '__main__':
    main() 