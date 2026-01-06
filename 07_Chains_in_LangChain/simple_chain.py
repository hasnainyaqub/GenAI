from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(
    template='Generate a creative short 5 line story about {topic}.',
    input_variables=['topic']
)

model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models

parser = StrOutputParser()

# Create a simple chain
chain = template | model | parser 

# Run the chain with a specific topic
result = chain.invoke({'topic': 'a brave little toaster'})
print(result)
chain.get_graph().print_ascii()  # Visualize the chain structure                        