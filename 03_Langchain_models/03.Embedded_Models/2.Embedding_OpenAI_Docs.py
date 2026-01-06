from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language.",
    "Machine learning is a subset of artificial intelligence that involves the use of algorithms and statistical models to enable computers to improve their performance on a specific task through experience.",
    "Deep learning is a class of machine learning based on artificial neural networks with representation learning.",
    "Reinforcement learning is an area of machine learning concerned with how software agents ought to take actions in an environment in order to maximize some notion of cumulative reward.",
    "Computer vision is an interdisciplinary field that enables computers to interpret and make decisions based on visual data from the world.",
]

result = embedding.embed_documents(documents)

print(str(result))