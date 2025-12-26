from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("10_Document_Loaders_LangChain/dl-curriculum.pdf")

documents = loader.load()

print(len(documents))

print(documents[0].page_content)
print(documents[1].metadata)