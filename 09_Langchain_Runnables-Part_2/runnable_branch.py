from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnablePassthrough, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Write A detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

model = ChatGroq(model='groq/compound', temperature=0.5)

parser = StrOutputParser()

rep_genChain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, prompt2 | model | parser),
    RunnablePassthrough()
)

finalChain = RunnableSequence(rep_genChain, branch_chain)

result = finalChain.invoke({'topic':'black hole'})

print(result)

