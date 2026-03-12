from crewai import Task
from agents.data_analyst import data_analyst_agent

def analysis_task(research):

    return Task(
        description="""
        Analyze the provided research findings and extract meaningful insights.

        Focus on:
        - identifying key patterns and trends
        - highlighting important statistics
        - summarizing the most valuable insights
        - identifying major conclusions from the research
        """,

        expected_output="""
        A structured analysis including:
        - Key insights
        - Important statistics
        - Major trends
        - Final conclusions
        """,
        agent=data_analyst_agent
    )