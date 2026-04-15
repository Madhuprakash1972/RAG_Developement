# RAG Development Project

A local Retrieval-Augmented Generation (RAG) system using LangChain, ChromaDB, and Gemma-3.

## Project Structure
- `main.py`: Entry point for the application.
- `src/`: Source code (loaders, chunkers, vectorstore, etc.).
- `models/`: Folder for LLM and Embedding models (Ignored by Git).
- `data/`: Local storage for documents and the vector database.

## Model Setup

To keep the repository lightweight, models are not included. Please download them from the links below and place them in the correct folders.

### 1. LLM (Large Language Model)
- **Model:** Google Gemma-3-4B-IT (Quantized GGUF)
- **Download Link:** [Download google_gemma-3-4b-it-Q4_K_M.gguf](https://huggingface.co/google/gemma-3-4b-it-gguf/resolve/main/google_gemma-3-4b-it-Q4_K_M.gguf)
- **Destination Path:** `models/llm/google_gemma-3-4b-it-Q4_K_M.gguf`

### 2. Embedding Model
- **Model:** all-MiniLM-L6-v2
- **Download Link:** [Hugging Face: all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Destination Path:** `models/embedding/`
- *Note: If you have an internet connection, the `sentence-transformers` library will usually download this automatically on the first run.*

## Installation

1. **Install required packages:**
   ```bash
   pip install -r requirement.txt
