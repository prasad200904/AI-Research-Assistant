from crewai import Task
from agents.content_writer import content_writer_agent




def writing_task(analysis):

    return Task(
        description=f"""
        Create a research report about {analysis}.

        Write the report in the following sections:

        1. Introduction (3-4 sentences)
        2. Key Insights (3 bullet points)
        3. Conclusion (2-3 sentences)

        Keep the report clear and concise.
        """,

        expected_output="""
        A complete research report with:

        Introduction
        Key Insights
        Conclusion
        """,

        agent=content_writer_agent,



        output_file="report.txt"
    )