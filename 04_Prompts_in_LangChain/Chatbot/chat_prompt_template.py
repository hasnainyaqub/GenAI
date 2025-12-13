from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models

# Define the chat prompt template
chat_prompt = ChatPromptTemplate(
    [
       ('system', "You are an expert in {domain}."),
       ('human', "{user_input}")
    ]
)
user = input("You: ")
prompt = chat_prompt.invoke({"domain": "AI", "user_input": user})
print(f"Prompt: {prompt}")