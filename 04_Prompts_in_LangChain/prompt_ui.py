from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Reasrearch Tool")

user_input = st.text_area("Enter your message:")

model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models

if st.button("Generate Response"):
    result = model.invoke(user_input)
    st.subheader("Response:")
    st.write(result.content)