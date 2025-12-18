from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

# prompt = template.format()
# response = llm.invoke(prompt)
# output = parser.parse(response.content)
# print(output)

# using chain

chain = template | llm | parser

result = chain.invoke({'topic': 'the universe'})
print(result)