from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0.7)

result = llm.invoke('What is the capital of Pakistan?')
print(result)