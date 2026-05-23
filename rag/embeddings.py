from langchain.embeddings import HuggingFaceEmbeddings


def get_embedding_model():

    model_name = "BAAI/bge-large-en-v1.5"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )

    return embeddings
