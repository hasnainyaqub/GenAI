from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

user_input = input("Enter your message: ")

model = ChatGroq(model="llama-3.1-8b-instant")  # or other Groq models
result = model.invoke([HumanMessage(content=user_input)])
print(result.content)