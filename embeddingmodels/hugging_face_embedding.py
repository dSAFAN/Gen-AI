from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = ["This is 1 query",
         "This is 2 query",
         "This is 3 query"]

vector = embedding.embed_documents(texts)

print(vector)