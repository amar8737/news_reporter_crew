from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field

# Create a pydentic model for structured output
class NewsReport(BaseModel):
    headline: str = Field(description="The headline of the news report")
    summary: str = Field(description="A concise summary of the news article")
    url: List[str] = Field(description="The URL of the original news article")
    news_agency: List[str] = Field(description="List of sources for the news article")
# Define the NewsReporterAgent

@CrewBase
class NewsReporterCrew(BaseAgent):
    "NewsReportCrew crew"

    agents: List[Agent]
    tasks: List[Task]

    # config paths
    agent_config_path: str = "config/agents.yaml"
    task_config_path: str = "config/tasks.yaml"

    @agent
    def news_reporter_agent(self) -> Agent:
        "News Reporter Agent"
        return Agent(self.agents["news_reporter"],
                     verbose=True)
    @task
    def generate_news_report(self) -> Task:
        "Generate News Report Task"
        return Task(self.tasks["reporting_task"],
                    output_json=NewsReport,
                    output_file= "news_report{country}.json",
                    verbose=True)    

    @crew
    def news_reporter_crew(self) -> Crew:
        "News Reporter Crew Process"
        return Crew(
            agents=self.agents,
            tasks=self.tasks
        )  
