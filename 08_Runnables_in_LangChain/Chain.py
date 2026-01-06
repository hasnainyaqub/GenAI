from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile')

parser = StrOutputParser()

template = PromptTemplate(
    input_variables=['question'],
    template='You are a helpful assistant. Answer the following question:\n{question}',
)


chain = template | model | parser

question = input("Enter your question: ")

response = chain.invoke({"question": question})

print("Response:", response)