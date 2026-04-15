from src.loader import load_documents
from src.chunker import split_documents
from src.vectorstore import create_vectorstore, get_vectorstore
from src.retriever import get_retriever
from src.generator import get_prompt, get_llm  # Added get_llm
from src.mediator import QueryMediator
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate # Added ChatPromptTemplate

class RAGSystem:  # Renamed from RAGAgent to match your main.py
    def __init__(self):
        self.llm = get_llm()                    # Main LLM for answering
        self.prompt = get_prompt()
        self.mediator = QueryMediator()         # ← Mediator added
        self.retriever = None
        print("🤖 AI Agent with Query Mediator is ready!")

    def ingest(self):
        docs = load_documents()
        if not docs:
            print("⚠️ No documents found!")
            return False

        chunks = split_documents(docs)
        create_vectorstore(chunks)
        self.retriever = get_retriever()
        print("✅ Ingestion completed!")
        return True

    def is_summary_request(self, question: str) -> bool:
        keywords = ['summary', 'summarize', 'summarise', 'overview', 'key points',
                   'tell about the document', 'what is the document']
        q = question.lower()
        return any(kw in q for kw in keywords)

    def query(self, user_question: str):
        """AI Agent with Mediator"""
        if not user_question.strip():
            return

        # Step 1: Use Mediator to improve/translate the question
        improved_question = self.mediator.improve_query(user_question)

        if self.retriever is None:
            self.retriever = get_retriever()

        # Retrieve context using improved question
        retrieved_docs = self.retriever.get_relevant_documents(improved_question)
        context = "\n\n".join([doc.page_content[:1500] for doc in retrieved_docs])

        # Special handling for summary
        if self.is_summary_request(improved_question):
            print("\n📝 Generating clean Markdown summary...\n")
            summary_prompt = ChatPromptTemplate.from_template("""
Create a clean, well-formatted Markdown summary using the context.

Use headings, bullet points, and bold text where helpful.

Context:
{context}

Markdown Summary:
""")
            chain = summary_prompt | self.llm | StrOutputParser()
            answer = chain.invoke({"context": context})
            print("="*70)
            print(answer.strip())
            print("="*70)
            return answer

        # Normal query
        print("🤔 Thinking...")
        chain = (
            {"context": lambda x: context, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

        answer = chain.invoke(improved_question)
        print("\nAnswer:\n")
        print(answer.strip())
        return answer
