# Sample Documents Template for RAG Testing

Put the following files inside:  
`data/documents/`

## Recommended Files to Add (Total 5-6 files)

### 1. PDF Files (Best for testing RAG)
- **about_xai.pdf**  
  Content: Information about xAI company, mission, and Grok AI.

- **rag_technology.pdf**  
  Content: Detailed explanation of Retrieval-Augmented Generation (RAG).

- **grok_ai.pdf**  
  Content: About Grok AI model, its features, and inspiration.

- **llm_basics.pdf**  
  Content: Introduction to Large Language Models.

### 2. Text Files (Fast loading & good for testing)
- **company_info.txt**
- **faq.txt**

---

## Content for Each File (Copy & Create)

### 1. about_xai.pdf  (Create from this text)
**Title:** About xAI

xAI was founded by Elon Musk in July 2023.  
The primary mission of xAI is to understand the true nature of the universe.  

xAI developed Grok, a helpful and maximally truthful AI inspired by the Hitchhiker's Guide to the Galaxy and JARVIS from Iron Man.  
Grok has real-time knowledge through integration with X (Twitter).

### 2. rag_technology.pdf
**Title:** What is Retrieval-Augmented Generation (RAG)?

RAG is a technique that enhances Large Language Models by retrieving relevant information from external documents before generating a response.  

Key benefits of RAG:
- Reduces hallucinations
- Provides up-to-date knowledge
- Improves answer accuracy

Main components:
1. Document Ingestion & Chunking
2. Embedding Generation
3. Vector Database (like Chroma)
4. Retrieval
5. Generation using LLM

### 3. grok_ai.pdf
**Title:** Grok AI by xAI

Grok is an AI chatbot created by xAI.  
It is designed to answer questions with wit, humor, and rebellion against overly cautious AI norms.  

Grok can access real-time information and is known for being helpful while maintaining a fun personality.

### 4. company_info.txt   ← Create this text file
xAI Mission: Understand the true nature of the universe.
Founding Year: 2023
Founder: Elon Musk
Popular Product: Grok AI
Location: San Francisco Bay Area

### 5. faq.txt   ← Create this text file
Q: What is RAG?
A: Retrieval-Augmented Generation combines retrieval and generation for better answers.

Q: Which embedding model are we using?
A: all-MiniLM-L6-v2

Q: How to add new documents?
A: Place PDF, TXT, or MD files in the data/documents/ folder and restart the app.
