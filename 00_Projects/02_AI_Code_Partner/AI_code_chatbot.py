from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import PyPDF2
from dotenv import load_dotenv
load_dotenv()
# api_key = st.secrets['GROQ_API_KEY']

# headers = {
#        "authorization": f"Bearer {api_key}",
#         "content-type": "application/json"
# }

parser = StrOutputParser()

def read_uploaded_file(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    return ""

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AI Assistant. Be clear, accurate, and beginner-friendly. Always answer short and to the point."
     "Always follow the output format instructions. "
     "Tell today's date at the end in YYYY-MM-DD format."
    ),
    ("human",
     "Document Content:\n{document}\n\nUser Question:\n{input}"
    )
])

model = ChatGroq(
    model="groq/compound",
    temperature=0.7
)

chat = prompt | model | parser

st.title("AI Assistant Chatbot")

uploaded_file = st.file_uploader(
    "Upload a document (TXT or PDF), upload plain text files for best results.",
    type=["txt", "pdf"]
)

document_text = ""
if uploaded_file:
    document_text = read_uploaded_file(uploaded_file)
    st.success("Document uploaded successfully")

user_input = st.chat_input("Enter your question for the AI Assistant...")

if user_input:
    response = chat.invoke({
        "input": user_input,
        "document": document_text
    })
    st.write(response)

