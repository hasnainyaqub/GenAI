from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "The quick brown fox jumps over the lazy dog." 
]

vector = embedding.embed_documents(documents)

print(str(vector))
