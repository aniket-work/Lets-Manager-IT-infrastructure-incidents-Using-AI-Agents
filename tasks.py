from crewai import Task


def create_tasks(task_configs, agents):
    tasks = []
    agent_map = {agent.role: agent for agent in agents}

    for config in task_configs:
        task = Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=agent_map[config['agent']]
        )
        tasks.append(task)

    return tasks