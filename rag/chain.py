from langchain_openai import ChatOpenAI
from rag.prompts import SYSTEM_PROMPT


class FinancialRAG:

    def __init__(
        self,
        retriever,
        reranker,
        query_rewriter
    ):

        self.retriever = retriever
        self.reranker = reranker
        self.query_rewriter = query_rewriter

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    def generate_answer(self, query):

        rewritten_query = self.query_rewriter.rewrite(query)

        docs = self.retriever.retrieve(rewritten_query)

        reranked_docs = self.reranker.rerank(
            query,
            docs
        )

        context = "\n\n".join([
            doc.page_content
            for doc in reranked_docs
        ])

        prompt = f"""
        {SYSTEM_PROMPT}

        Context:
        {context}

        Question:
        {query}
        """

        response = self.llm.invoke(prompt)

        sources = []

        for doc in reranked_docs:
            if "source" in doc.metadata:
                sources.append(doc.metadata["source"])

        return {
            "answer": response.content,
            "sources": list(set(sources))
        }
