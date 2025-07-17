from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import tool

@tool
def get_webpage_content(url: str) -> str:
    """
    Loads and returns the text content of a given webpage URL.
    Returns a snippet of the content to be used for evaluation.
    """
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        content = " ".join([d.page_content for d in docs])
        return content[:4000] # Return first 4000 characters for analysis
    except Exception as e:
        # print(f"Error loading {url}: {e}")
        return "" # Return empty string on failure
