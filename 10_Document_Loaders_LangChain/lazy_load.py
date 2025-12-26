from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='10_Document_Loaders_LangChain/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

for document in docs:
    print(document.metadata)