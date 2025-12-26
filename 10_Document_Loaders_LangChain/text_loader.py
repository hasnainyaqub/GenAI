from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="groq/compound-mini")

prompt = PromptTemplate(
    template='Write a summary Report on {resume}',
    input_variables=['resume']
)

parser = StrOutputParser()
loader = TextLoader("10_Document_Loaders_LangChain/myInfo.txt")

documents = loader.load()

# print(documents)
print(documents[0].page_content)

chain = prompt | model | parser

result = chain.invoke(documents[0].page_content)

print(result)