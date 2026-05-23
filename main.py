from ingestion.loader import FinancialDocumentLoader
from ingestion.cleaner import TextCleaner
from rag.chunking import ChunkingStrategy
from rag.embeddings import get_embedding_model
from rag.vector_store import VectorStoreManager


def main():

    loader = FinancialDocumentLoader()

    docs = loader.load_directory("data/raw")

    cleaner = TextCleaner()

    cleaned_docs = []

    for doc in docs:

        for page in doc["pages"]:

            cleaned_text = cleaner.clean_text(
                page["text"]
            )

            cleaned_docs.append(cleaned_text)

    chunker = ChunkingStrategy()

    chunks = chunker.create_chunks(cleaned_docs)

    embeddings = get_embedding_model()

    vector_manager = VectorStoreManager(
        embeddings
    )

    vectorstore = vector_manager.create_index(
        chunks
    )

    vector_manager.save_index(
        vectorstore,
        "vectorstore/faiss_index"
    )


if __name__ == "__main__":
    main()
