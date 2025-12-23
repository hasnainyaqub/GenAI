from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define a prompt template
template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question:\n{question}",
)

# Define the input question
question = input("Enter your question: ")

# Format the prompt with the input question
prompt = template.format(question=question)

# Get the response from the LLM
response = llm.invoke(prompt)

# Print the response
print("Response:", response.content)