from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import  StrOutputParser 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AI Code Partner. You help users understand, debug, and improve their code. "
     "Be clear, accurate, and beginner-friendly. "
     "Tell today's date at the end of the conversation in YYYY-MM-DD format. "
     "Always follow the output format instructions."
    ),
    ("human", "User Question: {input}")
])


model = ChatGroq(model="groq/compound", temperature=0.7)

chat = prompt | model | parser

st.title("AI Code Partner")
user_input = st.chat_input("Enter your question for the AI Code Partner...")

if user_input:
    response = chat.invoke({"input": user_input})
    st.write(response)
