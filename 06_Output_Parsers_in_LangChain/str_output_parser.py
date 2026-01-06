from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
# We will use Gemini 2.5 Flash model for this example
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro") # or other Google GenAI models (e.g., "gemini-2.5-flash", 2.0, etc.)
# Alternatively, you can use Groq model
# chat_model = ChatGroq(model="llama-3.3-70b-versatile") # or other Groq models...


# 1st prompt -> detailed report
tem1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
tem2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)


parser = StrOutputParser()
chain = tem1 | chat_model | parser | tem2 | chat_model | parser

result = chain.invoke({'topic':'AI in healthcare'})
print(result)