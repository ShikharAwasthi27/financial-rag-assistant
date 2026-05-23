# financial-rag-assistant
RAG-based financial question answering capstone project

A production-minded Retrieval-Augmented Generation (RAG) system for answering financial questions from SEC filings and enterprise financial reports using grounded evidence and source citations.

This project ingests financial documents (PDF/HTML/TXT), processes and chunks the content with metadata enrichment, generates embeddings, and stores them in a FAISS vector database for efficient semantic retrieval. The system uses query rewriting, reranking, and LLM-powered response generation to provide accurate, context-aware answers strictly based on retrieved financial data.

The application includes:
- Robust financial document ingestion and preprocessing
- Metadata-aware chunking and vector indexing
- Semantic retrieval with reranking
- Citation-based answer generation
- Guardrails for hallucination and out-of-scope queries
- Streamlit UI and FastAPI backend
- Evaluation framework using RAGAS metrics

The assistant is designed to support financial analysis tasks such as:
- Revenue trend analysis
- Risk factor identification
- Margin comparison
- Segment growth analysis
- Management discussion insights
- Forward-looking guidance extraction

# How to run
pip install -r requirements.txt

python main.py

streamlit run app/streamlit_app.py

uvicorn app.api:app --reload
streamlit run app/streamlit_app.py
uvicorn app.api:app --reload
