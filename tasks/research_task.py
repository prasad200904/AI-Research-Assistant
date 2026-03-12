from crewai import Task
from agents.research_specialist import research_agent

def research_task(topic):

    return Task(
        description=f"""
        Conduct structured research on the topic: {topic}.

        Collect important information including:
        - key facts and concepts
        - important statistics
        - recent trends and developments
        - real-world applications

        Present the findings clearly so they can be analyzed further.
        """,

        expected_output="""
        Structured research notes including:
        - Key facts
        - Important statistics
        - Recent trends
        - Brief explanations
        """,
        agent=research_agent
    )