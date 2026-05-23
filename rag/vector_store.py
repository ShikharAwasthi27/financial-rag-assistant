from langchain.vectorstores import FAISS


class VectorStoreManager:

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def create_index(self, chunks):

        vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        return vectorstore

    def save_index(self, vectorstore, path):
        vectorstore.save_local(path)

    def load_index(self, path):

        return FAISS.load_local(
            path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )
