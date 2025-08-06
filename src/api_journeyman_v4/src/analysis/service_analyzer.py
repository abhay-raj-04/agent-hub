import json
from src.types.state import JourneymanState
from src.config.llm_config import get_llm
from src.tools.web_search import search_for_api_docs
from src.prompts.analysis_prompts import get_service_analysis_prompt
from langchain_community.document_loaders import WebBaseLoader

def analyze_service_docs_node(state: JourneymanState):
    print("--- [Analysis] Starting Service Docs Analysis ---")
    try:
        docs_url = search_for_api_docs.invoke({"service_name": state['service_name']})
        if "Error:" in docs_url:
            raise ValueError(docs_url)

        loader = WebBaseLoader(docs_url)
        docs = loader.load()
        docs_content = " ".join([d.page_content for d in docs])[:8000]

        llm = get_llm()
        prompt = get_service_analysis_prompt(docs_content, state['service_name'])
        response = llm.invoke(prompt)

        cleaned = response.content.strip().replace("```json", "").replace("```", "")
        service_info = json.loads(cleaned)
        service_info['service_name'] = state['service_name']
        state['service_analysis'] = service_info

    except Exception as e:
        state['error_message'] = f"Error analyzing service docs: {str(e)}"
    return state
