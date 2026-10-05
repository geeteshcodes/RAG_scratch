def prompt(query: str, retrieved_chunks: list[str]) -> str:
    if not query.strip():
        raise ValueError("Query cannot be empty")

    if not retrieved_chunks:
        raise ValueError("Retrieved chunks cannot be empty")

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""Answer the question using only the provided context.
    If the answer cannot be found in the context, say that you don't have enough information.

    Context:
    {context}

    Question:
    {query}
    """

    return prompt

