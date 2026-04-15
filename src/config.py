# src/config.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.resolve()

# Data paths
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"
CHROMA_DB_PATH = DATA_DIR / "chroma_db"

# Models paths
MODELS_DIR = BASE_DIR / "models"
EMBEDDINGS_MODEL_DIR = MODELS_DIR / "embeddings"
LLM_MODEL_DIR = MODELS_DIR / "llm"

# Create all directories
for directory in [DOCUMENTS_DIR, CHROMA_DB_PATH, EMBEDDINGS_MODEL_DIR, LLM_MODEL_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ====================== Configuration ======================

# Embedding Model (local)
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_MODEL_PATH = EMBEDDINGS_MODEL_DIR / EMBEDDING_MODEL_NAME

# LLM - Qwen2.5-Omni-7B GGUF
LLM_MODEL_NAME = "google_gemma-3-4b-it-Q4_K_M.gguf"
LLM_MODEL_PATH = LLM_MODEL_DIR / LLM_MODEL_NAME

# Retrieval settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 100

# Mediator / Translator Settings
ENABLE_TRANSLATOR = True                    # Set False to disable
TRANSLATOR_MAX_TOKENS = 300

print("✅ Config loaded successfully!")
print(f"Documents  : {DOCUMENTS_DIR}")
print(f"Embedding  : {EMBEDDING_MODEL_NAME}")
print(f"LLM Path   : {LLM_MODEL_PATH}")
print(f"Chroma DB  : {CHROMA_DB_PATH}")
