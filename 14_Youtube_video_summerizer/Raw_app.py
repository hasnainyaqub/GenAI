from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import re
load_dotenv()

def extract_youtube_id(url: str) -> str | None:
    """
    Extract YouTube video ID from a URL.
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://www.youtube.com/shorts/VIDEO_ID
    - https://www.youtube.com/shorts/VIDEO_ID
    """
    pattern = (
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    )
    match = re.search(pattern, url)
    return match.group(1) if match else None


# usage
input_url = input("Enter YouTube video link: ")
video_id = extract_youtube_id(input_url)

try:
    # Create API client
    api = YouTubeTranscriptApi()
    # Fetch transcript data for the video
    transcript = api.fetch(video_id, languages = ["en", "en-US", "hi", "ur"])
    # Convert transcript objects into a single text string
    text = " ".join(item.text for item in transcript)
except TranscriptsDisabled:
    # Raised when captions are disabled by the video owner
    print("Captions are disabled")
except NoTranscriptFound:
    # Raised when no transcript exists for the video
    print("No transcript found")
except Exception as e:
    # Catch any unexpected errors
    print("Error:", e)

# Convert FetchedTranscript → plain text
transcript_text = " ".join(item.text for item in transcript)
print(transcript_text)
# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.create_documents([transcript_text])

emb = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5",
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True}
)

vector_store = FAISS.from_documents(chunks, emb)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatGroq(model='groq/compound', temperature=0.2)

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer Only form the provided transcript context.
    if context is in other language translate it into english / roman urdu and answer.
    If No found. just say You dont know.

    {context}
    Question: {question}
    """,
    input_variables=['context', 'question']
)

# concatenate the retrieved_docs, function
def contcatenated_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(contcatenated_docs),
    'question': RunnablePassthrough()
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

print(main_chain.invoke('Can you summerize the video?'))