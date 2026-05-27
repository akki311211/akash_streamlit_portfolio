"""
RAG Ingestion — uses TF-IDF via scikit-learn.
Zero external model downloads. Works on Streamlit Cloud out of the box.
scikit-learn is already a Streamlit dependency.
"""

from pathlib import Path
import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

DOCS_DIR = Path(__file__).parent.parent / "docs"
CHUNK_SIZE = 300
OVERLAP = 50


def _chunk_text(text: str) -> list[str]:
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunk = " ".join(words[i : i + CHUNK_SIZE])
        chunks.append(chunk)
        i += CHUNK_SIZE - OVERLAP
    return [c for c in chunks if c.strip()]


@st.cache_resource(show_spinner="Initialising voice assistant...")
def build_vector_store():
    """
    Returns (vectorizer, matrix, chunks, metadatas).
    Uses TF-IDF cosine similarity — no model downloads needed.
    """
    all_chunks, all_meta = [], []

    for md_file in sorted(DOCS_DIR.glob("*.md")):
        text = md_file.read_text()
        chunks = _chunk_text(text)
        for chunk in chunks:
            all_chunks.append(chunk)
            all_meta.append({"source": md_file.stem})

    if not all_chunks:
        return None, None, [], []

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(all_chunks)

    return vectorizer, matrix, all_chunks, all_meta