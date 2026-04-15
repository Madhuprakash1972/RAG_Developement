# main.py
from src.rag import RAGSystem
import os
from src.config import DOCUMENTS_DIR

def main():
    print("🚀 Starting Minimal RAG System")
    print(f"Documents folder: {DOCUMENTS_DIR}\n")
    
    rag = RAGSystem()
    
    # Ingest documents (run only once or when documents change)
    if not os.path.exists(DOCUMENTS_DIR) or not any(DOCUMENTS_DIR.iterdir()):
        print("⚠️ Please add some PDF/txt/md files into data/documents/ folder")
    else:
        print("Ingesting documents...")
        rag.ingest()
    
    # Interactive query loop
    print("\n" + "="*60)
    print("RAG System Ready! Type 'exit' to quit.")
    print("="*60)
    
    while True:
        question = input("\nYour question: ").strip()
        if question.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        if question:
            answer = rag.query(question)
            print("\nAnswer:", answer)

if __name__ == "__main__":
    main()
