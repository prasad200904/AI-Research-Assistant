from crewai import Crew
from tasks.research_task import research_task
from tasks.analyst_task import analysis_task
from tasks.write_task import writing_task

def run_research(topic):

    research = research_task(topic)
    analysis = analysis_task(research)
    writing = writing_task(analysis)

    crew = Crew(
        agents=[
            research.agent,
            analysis.agent,
            writing.agent
        ],
        tasks=[research, analysis, writing],
        verbose=True
    )

    result = crew.kickoff()

    report = str(result)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    return report