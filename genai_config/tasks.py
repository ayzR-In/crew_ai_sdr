from textwrap import dedent
from crewai import Task
import json
from pydantic import BaseModel

# Define the Pydantic model for output
class SDR_OUT(BaseModel):
    content: str

class sales_tasks():
    # Sales Task
    def company_analysis(self, agent, company_name, employees, industry, technologies, keywords):
        return Task(
            description=dedent(
                f"""
            Analyze the company data for {company_name} with the following metrics:
            - Employee count: {employees}
            - Industry: {industry}
            - Technologies: {technologies}
            - Keywords: {keywords}
            """
            ),
            expected_output=dedent(
                f"""
            Make the output within 10-12 words, follow the examples provided:
            - "doubled your team size in 6 months"
            - "expanded to three new markets this quarter"
            - "secured Series B funding of $40M"
            - "achieved 150% year-over-year revenue growth"
            - "opened two additional office locations"
            - "acquired three companies within 18 months"
            - "scaled your customer base to 10,000 users"
            - "launched operations in five new countries"
            - "increased your product line from 3 to 15 SKUs"
            - "grown your enterprise client portfolio by 200%".
            """
            ),
            verbose=True,
            agent=agent,
            output_json=SDR_OUT
        )
    
    # Output config pending.
    # Passing data for task processing.