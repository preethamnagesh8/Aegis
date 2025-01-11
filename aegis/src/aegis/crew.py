from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from aegis.tools.custom_tool import WordPressCreateBlog

# Uncomment the following line to use an example of a custom tool
# from aegis.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class AegisCrew():
	"""Aegis crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)
	
	@agent
	def content_planner(self) -> Agent:
		return Agent(
			config=self.agents_config['content_planner'],
			verbose=True
		)
	
	@agent
	def content_expander(self) -> Agent:
		return Agent(
			config=self.agents_config['content_expander'],
			tools = [WordPressCreateBlog()],
			verbose=True
		)
	
	@agent
	def code_enhancer(self) -> Agent:
		return Agent(
			config=self.agents_config['code_enhancer'],
			tools = [WordPressCreateBlog()],
			verbose=True
		)
	
	@agent
	def content_flow_reviewer(self) -> Agent:
		return Agent(
			config=self.agents_config['content_flow_reviewer'],
			tools = [WordPressCreateBlog()],
			verbose=True
		)
	
	@agent
	def blog_formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_formatter'],
			verbose=True
		)
	
	@agent
	def blog_publisher(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_publisher'],
			tools = [WordPressCreateBlog()],
			verbose=True
		)
	
	# Tasks from here --------------------

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)
	
	@task
	def content_planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_planning_task'],
		)
	
	@task
	def content_expansion_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_expansion_task'],
		)
	
	@task
	def code_enhancer_task(self) -> Task:
		return Task(
			config=self.tasks_config['code_enhancer_task'],
		)
	

	@task
	def content_flow_review_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_flow_review_task'],
		)
	
	
	@task
	def html_formatting_task(self) -> Task:
		return Task(
			config=self.tasks_config['html_formatting_task'],
		)
	
	@task
	def blog_publishing_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_publishing_task'],
		)
	
	#Manager Agent Definition --------------

	manager = Agent(
		role = "{topic} Blog Project Manager",
		goal = "Efficiently manage the crew and ensure generation of high-quality blog articles",
		backstory = "You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed as instructed and to the highest standard. Ensure to double check completion of each task and retry them 1 TIME AT MAXIMUM",
		allow_delegation = True,
	)

	@crew
	def crew(self) -> Crew:
		"""Creates the Aegis crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			manager_agent = self.manager,
			process=Process.hierarchical,
			verbose=True,
			memory=True
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)