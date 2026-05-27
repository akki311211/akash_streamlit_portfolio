from pathlib import Path
import streamlit as st
import chromadb
from fastembed import TextEmbedding

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
    # fastembed: pure onnxruntime, no torch/torchvision needed
    model = TextEmbedding("BAAI/bge-small-en-v1.5")

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

    embeddings = list(model.embed(all_chunks))
    import numpy as np
    embeddings = [e.tolist() if hasattr(e, 'tolist') else list(e) for e in embeddings]

    collection.add(
        documents=all_chunks,
        embeddings=embeddings,
        ids=all_ids,
        metadatas=all_meta,
    )

    return collection, model