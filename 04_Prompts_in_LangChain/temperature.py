from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models
result = model.invoke('write a 4 line poem about the AI', temperature=1.5)
print(result.content)