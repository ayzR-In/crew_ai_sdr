from crewai import Crew
from tasks import sales_tasks
from agents import sales_agents

company_name = 'leanitcorp'
employees = '100'
industry = 'consulting'
technologies = 'salesforce'
keywords = 'salesforce implementation partner'

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

        print(result_sales_analysis)

        
    except Exception as e:
        return None
    
crew_ai_funciton(company_name, employees, industry, technologies, keywords)