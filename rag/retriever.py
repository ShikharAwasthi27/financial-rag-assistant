class FinancialRetriever:

    def __init__(self, vectorstore):

        self.retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 8}
        )

    def retrieve(self, query):

        return self.retriever.get_relevant_documents(query)
