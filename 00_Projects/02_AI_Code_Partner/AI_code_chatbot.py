from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

parser = StrOutputParser()

prompt = PromptTemplate(
    template=        """
You are an AI Code Partner.
You help users understand, debug, and improve their code.
Be clear, accurate, and beginner-friendly.
Tell the today's date in the end of conversation.
Always follow the output format instructions.
User Question: {input}
""",
    input_variables=["input", "date"],
)

model = ChatGroq(model="groq/compound", temperature=0.7)

chat = RunnableSequence(
        prompt,
        model,
        parser,
    )
st.title("AI Code Partner")
user_input = st.chat_input("Enter your question for the AI Code Partner...")

if user_input:
    placeholder = st.empty()
    full_text = ""

    for chunk in chat.stream({"input": user_input}):
        if chunk:
            full_text += chunk
            placeholder.markdown(full_text)
