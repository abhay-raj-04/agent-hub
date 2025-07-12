import os
from tavily import TavilyClient
from langchain_core.tools import tool

@tool
def search_for_api_docs(service_name: str) -> str:
    """
    Searches the web for the official API documentation URL for a given service.
    """
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        query = f"official developer API documentation for {service_name}"
        response = tavily.search(query=query, search_depth="basic", max_results=1)
        
        if response and response.get('results'):
            return response['results'][0]['url']
        return f"Error: Could not find a documentation URL for {service_name}."
    except Exception as e:
        return f"Error: An occurred during web search: {str(e)}"
