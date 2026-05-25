def retrieve(query: str, collection, model, top_k: int = 3):
    q_vec = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=q_vec,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    chunks    = results["documents"][0]
    sources   = [m["source"] for m in results["metadatas"][0]]
    distances = results["distances"][0]
    context   = "\n\n---\n\n".join(chunks)
    return context, sources, distances