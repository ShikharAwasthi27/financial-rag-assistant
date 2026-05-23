from langchain_openai import ChatOpenAI


class QueryRewriter:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    def rewrite(self, query):

        prompt = f"""
        Rewrite the financial query for better retrieval.

        Query:
        {query}
        """

        response = self.llm.invoke(prompt)

        return response.content
