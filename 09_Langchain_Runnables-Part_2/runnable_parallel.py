from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}.',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Generate a linkedIn post about {topic}.',
    input_variables=['topic'],
)

model_1 = ChatGroq(model='groq/compound', temperature=0.5)
model_2 = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.2)

parser = StrOutputParser()

runnable = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model_1, parser), 
    'linkedin_post': RunnableSequence(prompt2, model_2, parser),
})

response = runnable.invoke({'topic': 'AI'})

print(response['tweet'])
print('----------------------'*100)
print(response['linkedin_post'])
print('----------------------'*100)
