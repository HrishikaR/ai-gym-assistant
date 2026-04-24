import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

DATA_PATH = os.path.join(BASE_DIR, "rag_data")
DB_PATH = os.path.join(BASE_DIR, "vector_store")

# 🔥 GLOBAL CACHE (no logic change)
_embeddings = None
_db = None


# 🔥 CREATE VECTOR DB (UNCHANGED)
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

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)


# 🔥 RETRIEVE CONTEXT (SAME LOGIC, OPTIMIZED LOAD)
def get_rag_context(query):
    global _embeddings, _db

    if _db is None:
        _embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        _db = FAISS.load_local(
            DB_PATH,
            _embeddings,
            allow_dangerous_deserialization=True
        )

    docs = _db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    return context
