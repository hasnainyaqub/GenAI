from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv
load_dotenv()

# web_search_tool
web_search_tool = DuckDuckGoSearchRun()

# wikipedia_tool
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# add_in_toolkit
toolkit = [web_search_tool, wikipedia_tool]

# building model
model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
    max_tokens=1000
)
model = model.bind_tools(toolkit)

# creating agent
agent = create_agent(model, toolkit)
print(agent)
user_query = input('Enter your query: ')

events = agent.stream(
    {"messages": [("user",user_query)]},
    stream_mode="values"
)

for event in events:
    if "messages" in event:
        print(event["messages"][-1].content)