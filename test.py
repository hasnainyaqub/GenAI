from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='groq/compound-mini')

prompt = PromptTemplate(template="You are helpful assistant. Answer the following question:\n{question}", 
                        input_variables=["question"]
                        )

parser = StrOutputParser()

chain =  prompt | model | parser

class Question(BaseModel):
    question: str

user = input("Enter your question: ")
question = Question(question=user)

response = chain.invoke(question.model_dump())

print("Response:", response)

