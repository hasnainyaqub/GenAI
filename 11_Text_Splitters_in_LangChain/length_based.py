from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('11_Text_Splitters_in_LangChain/dl-curriculum.pdf')
docs = loader.load()

spliter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 100,
    chunk_overlap = 10
)

doc = spliter.split_documents(docs)

print(doc[2])