from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile") # or other Groq models

# chat history
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me About LangChain."),
]

result = model.invoke(chat_history)
chat_history.append(AIMessage(content=result.content))
print(f'Bot: {chat_history}')
