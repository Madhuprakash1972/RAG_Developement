# src/vectorstore.py
from langchain_community.vectorstores import Chroma
from src.embedder import get_embeddings
from src.config import CHROMA_DB_PATH

def create_vectorstore(chunks):
    """Create or load Chroma vector store"""
    embeddings = get_embeddings()
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB_PATH)
    )
    print(f"✅ Vector store created with {len(chunks)} chunks")
    return vectorstore

def get_vectorstore():
    """Load existing vector store"""
    embeddings = get_embeddings()
    vectorstore = Chroma(
        persist_directory=str(CHROMA_DB_PATH),
        embedding_function=embeddings
    )
    return vectorstore
