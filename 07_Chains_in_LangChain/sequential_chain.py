from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Initialize the Groq model
model = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.7)
# Initialize the OpenRouter Api model
# model = ChatOpenAI(
#                     api_key=getenv("OPENROUTER_API_KEY"),
#                     model='deepseek/deepseek-r1', 
#                     base_url="https://openrouter.ai/api/v1", 
#                     temperature=0
# )

temp1 = PromptTemplate(
    template='Generate a detailed report about a {topic}.',
    input_variables=['topic'],
)

temp2 = PromptTemplate( 
    template='Generate a 5 point summary of the following report:\n\n{story}',
    input_variables=['story'],
)

parser = StrOutputParser()

chain = temp1 | model | parser | temp2 | model | parser
result = chain.invoke({'topic': 'political conditions in Pakistan'})
print(result)