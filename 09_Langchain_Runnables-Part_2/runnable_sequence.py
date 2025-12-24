from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='Write a 2 lines joke about {topic}.',
    input_variables=['topic'],
)

model = ChatGroq(model='groq/compound', temperature=0.5)
model_2 = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.2)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {joke}',
    input_variables=['joke'],
)

runnable = RunnableSequence(prompt, model, parser, prompt2, model_2, parser)
response = runnable.invoke({'topic': 'AI'})

print(response)