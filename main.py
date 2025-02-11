from crewai import Crew

from genai_config.tasks import sales_tasks
from genai_config.agents import sales_agents
from dml.data_fetcher import llm_data
from dml.data_saver import llm_output_updater

def crew_ai_funciton(company_name, employees, industry, technologies, keywords):

    try:
        agent = sales_agents()
        tasks = sales_tasks()

        # Create agents
        sales_agent = agent.sales_development_rep()
        
        # Create tasks
        sales_task = tasks.company_analysis(sales_agent, company_name, employees, industry, technologies, keywords)

        # Execute tasks
        sales_crew = Crew(
            agents=[sales_agent],
            tasks=[sales_task],
            verbose=True,
            max_rpm=29
        )

        result_sales_analysis = sales_crew.kickoff()

        abhinav = result_sales_analysis['content']
        return abhinav

        
    except Exception as e:
        return None

if __name__ == "__main__":
    rows = llm_data()
    for row in rows:
        llm_output = crew_ai_funciton(row['company'], row['employee_size'], row['industry'], row['technologies'], row['keywords'])
        llm_output_updater(row['first_name'], row['last_name'], row['title'], row['email'],row['company'],llm_output)