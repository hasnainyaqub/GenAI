# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = ChatOpenAI(
    model="deepseek/deepseek-chat",      # general purpose
    # model="deepseek/deepseek-r1:free"  # reasoning model (free tier!)
    # Use .env file for OpenRouter API key. Don't hardcode it here.
    # openai_api_key="sk-or-v1-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # ← your OpenRouter key
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.5,
    max_tokens=300,
)

response = llm.invoke("Explain how a Merkle tree works, then implement it in Rust")
print(response.content)