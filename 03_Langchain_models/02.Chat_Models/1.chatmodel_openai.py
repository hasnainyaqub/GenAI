from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4")
result = model.invoke([HumanMessage(content="Hello world")])
print(result.content)