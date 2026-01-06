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
# input_url = input("Enter YouTube video link: ")
input_url = 'https://www.youtube.com/watch?v=J5_-l7WIO_w&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=29'
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

model = ChatGroq(model='groq/compound', temperature=0.1)

prompt1 = PromptTemplate(
    template="""
    You are a youtube video transcript translator or printer.
    if the transcript is in hindi or urdu then translate it to  English or roman urdu or hindi, if it is in other language then translate it to English or roman urdu or hindi {user_defined_language}.
    Dont change the structure of the text. and dont change the meaning of the text.
    {text}
    """,
    input_variables=['text', 'user_defined_language'],
)

parser = StrOutputParser()

chain = prompt1 | model | parser

result = chain.invoke({'text': transcript_text, 'user_defined_language': 'Roman Urdu'})

print(result)