from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# Sample documents
documents = [
    "The cat sits on the mat.",
    "Dogs are great pets.",
    "The sun is shining today.",
    "I love programming in Python."
]
# Generate embeddings for the documents
doc_embeddings = embedding_model.embed_documents(documents)

query = "I enjoy coding."
# Generate embedding for the query
query_embedding = embedding_model.embed_query(query)

# Calculate cosine similarity between query and document embeddings
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
# Get the index of the most similar document
index, similarity_score = sorted(list(enumerate(similarities)),key=lambda x:x[1])[-1]

print(query)
print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {similarity_score}")