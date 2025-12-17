from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response = chat_model.predict("Write a poem about the sea.")
print(response)