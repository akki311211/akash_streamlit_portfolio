"""
RAG Retriever — TF-IDF cosine similarity search.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def retrieve(query: str, vectorizer, matrix, chunks: list, metadatas: list, top_k: int = 3):
    """
    Returns (context_string, sources_list, scores_list).
    """
    if vectorizer is None or matrix is None or not chunks:
        return "No RAG context available.", [], []

    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, matrix).flatten()

    top_indices = np.argsort(scores)[::-1][:top_k]

    top_chunks  = [chunks[i] for i in top_indices]
    top_sources = [metadatas[i]["source"] for i in top_indices]
    top_scores  = [float(scores[i]) for i in top_indices]

    context = "\n\n---\n\n".join(top_chunks)
    return context, top_sources, top_scores