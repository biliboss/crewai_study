from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from crewai_study.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CrewaiSumCrew():
	"""CrewaiStudy crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def mathematician(self) -> Agent:
		return Agent(
			config=self.agents_config['mathematician'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@task
	def sum_two_numbers(self) -> Task:
		return Task(
			config=self.tasks_config['sum_two_numbers'],
			agent=self.mathematician()
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