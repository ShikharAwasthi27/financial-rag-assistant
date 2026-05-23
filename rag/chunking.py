from langchain.text_splitter import RecursiveCharacterTextSplitter


class ChunkingStrategy:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )

    def create_chunks(self, documents):

        chunks = self.splitter.create_documents(documents)

        return chunks
