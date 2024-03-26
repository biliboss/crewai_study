from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.agent_toolkits.gmail.toolkit import GmailToolkit
from langchain_community.tools.gmail import get_gmail_credentials
from langchain_community.tools.gmail.utils import build_resource_service

from crewai_read_email.tools.custom_gmail_search_tool import CustomGmailSearch

# Uncomment the following line to use an example of a custom tool
# from crewai_study.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="gmail_client_secret.json",
)
api_resource = build_resource_service(credentials=credentials)
custom_gmail_search_tool = CustomGmailSearch(api_resource=api_resource)
gmail_toolkit = GmailToolkit(api_resource=api_resource)
gmail_tools = gmail_toolkit.get_tools()
@CrewBase
class ReadEmailCrew():
	"""CrewaiStudy crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def secretary(self) -> Agent:
		return Agent(
			config=self.agents_config['secretary'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@task
	def fetch_emails(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_emails'],
			tools=[custom_gmail_search_tool],
			agent=self.secretary(),
			# callback=self.fetch_emails_callback
		)
	@task
	def evaluate_spam(self) -> Task:
		return Task(
			config=self.tasks_config['evaluate_spam'],
			agent=self.secretary(),
			# callback=self.fetch_emails_callback
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiStudy crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)