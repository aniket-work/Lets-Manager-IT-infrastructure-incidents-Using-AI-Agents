from crewai import Crew

def create_crew(agents, tasks):
    return Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )