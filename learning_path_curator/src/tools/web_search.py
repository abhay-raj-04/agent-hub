import os
from tavily import TavilyClient
from langchain_core.tools import tool
from typing import List, Dict

@tool
def search_for_resources(topic: str) -> List[Dict[str, str]]:
    """
    Searches the web for learning resources on a specific topic.
    Returns a list of dictionaries with 'url' and 'title'.
    """
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        # Craft a query focused on educational content
        query = f"best free online tutorial or guide for learning {topic}"
        response = tavily.search(query=query, search_depth="basic", max_results=5)
        
        if response and response.get('results'):
            return [{"url": res['url'], "title": res['title']} for res in response['results']]
        return []
    except Exception as e:
        return [] # Return empty list on failure
