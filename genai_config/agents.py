from textwrap import dedent
import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gpt-4o-mini",
)

class sales_agents:
    def sales_development_rep(self):
        """Agent for Sales Dev Rep"""
        return Agent(
            role='Sales Development Representative',
            goal='Generate personalized cold emails based on company analysis',
            backstory=dedent(
                """
                Expert in writing sales email with 10 years of experience.
                Specializes in B2B software sales with deep knowledge of Salesforce implementation benefits.
            """
            ),
            verbose=True,
            llm=llm
        )