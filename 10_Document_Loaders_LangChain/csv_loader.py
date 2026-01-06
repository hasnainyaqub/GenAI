from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('10_Document_Loaders_LangChain/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)