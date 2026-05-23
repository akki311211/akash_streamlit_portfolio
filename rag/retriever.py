"""
RAG Retriever — embeds a query and fetches the top-k relevant chunks.
"""


def retrieve(
    query: str,
    collection,
    model,
    top_k: int = 3,
) -> tuple[str, list[str], list[float]]:
    """
    Returns:
        context   — retrieved chunks joined as a single string
        sources   — list of source doc names (e.g. 'experience', 'skills')
        distances — cosine distances (lower = more similar)
    """
    q_vec = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=q_vec,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    chunks    = results["documents"][0]
    sources   = [m["source"] for m in results["metadatas"][0]]
    distances = results["distances"][0]

    context = "\n\n---\n\n".join(chunks)
    return context, sources, distances
