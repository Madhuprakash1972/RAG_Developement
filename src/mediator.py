# src/mediator.py
from langchain_core.prompts import ChatPromptTemplate
from src.generator import get_llm   # Reuse your existing LLM

class QueryMediator:
    def __init__(self):
        self.llm = get_llm()   # Reuse Gemma-3-4B
        print("🌐 Query Mediator (Translator) initialized")

    def improve_query(self, user_input: str) -> str:
        """Translate poor English / non-English into clear English"""
        
        mediator_prompt = ChatPromptTemplate.from_template("""
You are an expert English mediator and translator.

Task:
Take the user's possibly broken English or non-English input and convert it into **clear, natural, and grammatically correct English**.

Rules:
- Keep the original meaning exactly.
- Make it polite and professional.
- Make it suitable for a RAG document retrieval system.
- Do NOT add extra information.
- If the input is already clear English, just return it as is.
- Output ONLY the improved English question. No explanations.

User Input: {user_input}

Improved English Question:
""")

        chain = mediator_prompt | self.llm 
        improved = chain.invoke({"user_input": user_input}).strip()
        
        # Safety: If translation fails or is empty, return original
        if len(improved) < 5:
            return user_input
            
        print(f"Original : {user_input}")
        print(f"Improved : {improved}")
        
        return improved
