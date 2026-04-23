import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

DATA_PATH = os.path.join(BASE_DIR, "rag_data")
DB_PATH = os.path.join(BASE_DIR, "vector_store")


# 🔥 CREATE VECTOR DB (RUN ONCE)
def create_vector_db():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)

    print("✅ Vector DB Created")


# 🔥 RETRIEVE CONTEXT ONLY (NO LLM HERE)
def get_rag_context(query):
    embeddings = HuggingFaceEmbeddings()

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    return context