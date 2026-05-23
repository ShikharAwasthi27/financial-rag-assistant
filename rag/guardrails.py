FINANCIAL_KEYWORDS = [
    "revenue",
    "profit",
    "income",
    "cash flow",
    "margin",
    "risk",
    "guidance",
    "segment"
]


def is_financial_query(query):

    query = query.lower()

    return any(
        keyword in query
        for keyword in FINANCIAL_KEYWORDS
    )
