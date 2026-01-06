from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models

# chat history
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    print('--------------------------------')
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))   
    print(f'Bot: {result.content}')
    print('--------------------------------')

print(chat_history)