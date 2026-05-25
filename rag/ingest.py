from pathlib import Path
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb

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
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.Client()
    collection = client.get_or_create_collection("akash_profile")

    all_chunks, all_ids, all_meta = [], [], []

    for md_file in sorted(DOCS_DIR.glob("*.md")):
        text = md_file.read_text()
        chunks = _chunk_text(text)
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_ids.append(f"{md_file.stem}_{i}")
            all_meta.append({"source": md_file.stem})

    if not all_chunks:
        return collection, model

    embeddings = model.encode(all_chunks).tolist()
    collection.add(
        documents=all_chunks,
        embeddings=embeddings,
        ids=all_ids,
        metadatas=all_meta,
    )

    return collection, model