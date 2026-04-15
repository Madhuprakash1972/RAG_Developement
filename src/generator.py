# src/generator.py
from langchain_community.llms import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate
from src.config import LLM_MODEL_PATH

def get_llm():
    """Load fast LLM model"""
    llm = LlamaCpp(
        model_path=str(LLM_MODEL_PATH),
        temperature=0.7,
        max_tokens=1024,
        top_p=0.9,
        n_ctx=8192,           # Keep reasonable for speed
        verbose=False,
        n_threads=8,          # Adjust to your CPU cores (e.g., 4, 6, 8, 12)
        n_gpu_layers=0,       # 0 = CPU only (set -1 if you have GPU later)
    )
    print(f"✅ Fast LLM loaded: {LLM_MODEL_PATH}")
    return llm

# Prompt template
PROMPT_TEMPLATE = """
You are a helpful assistant. Use the following context to answer the question.
If you don't know the answer, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer:
"""

def get_prompt():
    return ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
