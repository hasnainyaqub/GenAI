from langchain_text_splitters import RecursiveCharacterTextSplitter

text = ''''
I am Hasnain Yaqoob, an aspiring Data Scientist who is actively building expertise across Machine Learning, Deep Learning, NLP, Computer Vision, and Generative AI. I am also learning FastAPI, Django and backend development to build complete and scalable AI powered applications. I enjoy working on real world problems, experimenting with modern AI techniques, and creating solutions that deliver practical value.
'''

spliter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=20
)

result = spliter.split_text(
    text
)

print(result)