import streamlit as st

st.title("Financial RAG Assistant")

query = st.text_input(
    "Ask a financial question"
)

if query:

    result = rag.generate_answer(query)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")

    for source in result["sources"]:
        st.write(source)
