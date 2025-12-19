from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal

from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

parser = StrOutputParser()

class SentimentOutput(BaseModel):
    sentiment: Literal['Positive', 'Negative', 'Neutral'] = Field(..., description="Give the sentiment of the feedback")
pydparser = PydanticOutputParser(pydantic_object=SentimentOutput)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text as Positive, Negative, or Neutral:\n{text} \n {format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions': pydparser.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Generate a positive response to the following feedback:\n{text}',
    input_variables=['text'],
)

prompt3 = PromptTemplate(
    template='Generate a negative response to the following feedback:\n{text}',
    input_variables=['text'],
)

prompt_neutral = PromptTemplate(
    template='Generate a neutral response to the following feedback:\n{text}',
    input_variables=['text'],
)

classification_chain = prompt1 | model | pydparser

branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "Positive",
        prompt2 | model | parser
    ),
    (
        lambda x: x.sentiment == "Negative",
        prompt3 | model | parser
    ),
    (
        lambda x: x.sentiment == "Neutral",
        prompt_neutral | model | parser
    ),
    prompt_neutral | model | parser     # default branch
)



chain = classification_chain | branch_chain

iput_text = input("Enter customer feedback: ")
result = chain.invoke({'text': iput_text})

print(result)

chain.get_graph().print_ascii()