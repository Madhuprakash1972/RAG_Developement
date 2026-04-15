# src/embedder.py
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL_NAME

def get_embeddings():
    """Return local embedding model"""
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'},   # change to 'cuda' if you have GPU
        encode_kwargs={'normalize_embeddings': True}
    )
    print(f"✅ Embedding model loaded: {EMBEDDING_MODEL_NAME}")
    return embeddings
