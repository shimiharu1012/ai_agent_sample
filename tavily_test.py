import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def configure_tavily_api():
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Tavily API key is missing")
    return TavilyClient(api_key=api_key)


tavily_client = configure_tavily_api()
question=input("Enter your question: ")
response=tavily_client.search(question,max_results=3)
print(*response['results'],sep='\n')