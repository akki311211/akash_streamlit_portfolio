def retrieve(query: str, collection, model, top_k: int = 3):
    # fastembed returns a generator — convert to list
    q_vec = list(model.embed([query]))
    q_vec = [q_vec[0].tolist() if hasattr(q_vec[0], 'tolist') else list(q_vec[0])]

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