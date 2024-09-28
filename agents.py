import os
from crewai import Agent
from crewai_tools import FileReadTool, FirecrawlCrawlWebsiteTool
from config import load_settings
from langchain_groq import ChatGroq

from constant import MODEL_NAME, GROQ_API_KEY


def create_agents(agent_configs):
    settings = load_settings()
    llm = ChatGroq(model_name=MODEL_NAME, groq_api_key=os.getenv(GROQ_API_KEY), llm_provider="groq",
                   api_base="https://api.groq.com")

    agents = []
    for config in agent_configs:
        tools = []
        if 'tools' in config:
            if "FileReadTool" in config['tools']:
                tools.append(FileReadTool())
            if "FirecrawlCrawlWebsiteTool" in config['tools']:
                tools.append(FirecrawlCrawlWebsiteTool(api_key=settings['firecrawl_api_key']))

        agent = Agent(
            role=config['role'],
            goal=config['goal'],
            tools=tools,
            llm=llm,
            verbose=True,
            backstory=config['backstory']
        )
        agents.append(agent)

    return agents