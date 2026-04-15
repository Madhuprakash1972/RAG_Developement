# src/loader.py
from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader, TextLoader
from pathlib import Path
from src.config import DOCUMENTS_DIR

def load_documents():
    """Improved document loader"""
    all_docs = []
    
    print(f"📁 Scanning folder: {DOCUMENTS_DIR}")
    print(f"Files found: {list(DOCUMENTS_DIR.iterdir())}")   # ← This will show you actual files
    
    # Load PDFs
    try:
        pdf_loader = PyPDFDirectoryLoader(str(DOCUMENTS_DIR))
        pdf_docs = pdf_loader.load()
        all_docs.extend(pdf_docs)
        print(f"✅ Loaded {len(pdf_docs)} PDF file(s)")
    except Exception as e:
        print(f"PDF Error: {e}")

    # Load .txt and .md files
    for pattern in ["**/*.txt", "**/*.md", "**/*.text"]:
        try:
            loader = DirectoryLoader(
                str(DOCUMENTS_DIR),
                glob=pattern,
                loader_cls=TextLoader,
                loader_kwargs={"encoding": "utf-8"},
                silent_errors=True
            )
            docs = loader.load()
            all_docs.extend(docs)
            if docs:
                print(f"✅ Loaded {len(docs)} {pattern} file(s)")
        except Exception as e:
            print(f"Text loader error ({pattern}): {e}")

    print(f"\n🎯 Total documents loaded: {len(all_docs)}")
    return all_docs
