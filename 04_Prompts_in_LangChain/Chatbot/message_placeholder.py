from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat template
chat_prompt = ChatPromptTemplate(
    [
       ('system', "You are a helpful customer support agent."),
       MessagesPlaceholder(variable_name="chat_history"),
       ('human', "{query}")
    ]
)

# load chat history
chat_history = []
with open('04_Prompts_in_LangChain/Chatbot/chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

# create prompt with chat history
user_query = "Can you help me with my order?"
prompt = chat_prompt.invoke({"chat_history": chat_history, "query": user_query})
print(f"Prompt with chat history:\n{prompt}")
 
