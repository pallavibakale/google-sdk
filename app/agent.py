from google.adk.agents import Agent

basic_agent = Agent(
    model='gpt-4.1',
    name='root_agent',
    description='A simple agent that can answer questions',
    instruction="""You are a helpful stock market assistant. Answer questions about stock prices, trends, and related topics. If you dont know something, just say no""",
)

root_agent = basic_agent