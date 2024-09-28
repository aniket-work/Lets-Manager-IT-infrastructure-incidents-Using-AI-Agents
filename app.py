import logging
from dotenv import load_dotenv
import streamlit as st
from config import load_config
from logging_setup import setup_logging
from agents import create_agents
from tasks import create_tasks
from crew import create_crew
from ui import run_ui

def main():
    # Load configuration
    config = load_config()

    # Set up logging
    logger = setup_logging(config['logging'])

    # Load environment variables
    load_dotenv()

    # Create agents
    agents = create_agents(config['agents'])

    # Create tasks
    tasks = create_tasks(config['tasks'], agents)

    # Create crew
    incident_crew = create_crew(agents, tasks)

    # Run Streamlit UI
    run_ui(incident_crew, logger)

if __name__ == "__main__":
    main()