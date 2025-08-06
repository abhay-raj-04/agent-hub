from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool

@tool
def load_content(url: str) -> str:
    """Load text content from webpage for evaluation"""
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        content = " ".join([d.page_content for d in docs])
        return content[:4000] # Return first 4000 characters for analysis
    except Exception as e:
        # print(f"Error loading {url}: {e}")
        return "" # Return empty string on failure

@tool
def get_webpage_content(url: str) -> str:
    """Load text content from webpage for evaluation"""
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        content = " ".join([d.page_content for d in docs])
        return content[:4000] # Return first 4000 characters for analysis
    except Exception as e:
        # print(f"Error loading {url}: {e}")
        return "" # Return empty string on failure
