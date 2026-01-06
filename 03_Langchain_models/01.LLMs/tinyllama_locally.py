from transformers import pipeline
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

llm = RunnableLambda(lambda x: pipe(x)[0]["generated_text"])
parser = StrOutputParser()

chain = llm | parser
print(chain.invoke("Explain AI in education"))
