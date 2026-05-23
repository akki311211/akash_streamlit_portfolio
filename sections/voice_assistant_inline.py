"""
Voice Assistant — inline panel, renders on the main portfolio page.
Same pattern as sections/chat.py — toggled via session_state["voice_open"].
"""

import os
import io
import streamlit as st
from groq import Groq


# ── Groq client ────────────────────────────────────────────────
def _get_groq_client():
    try:
        key = st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        key = ""
    if not key:
        key = os.environ.get("GROQ_API_KEY", "")
    return Groq(api_key=key.strip()) if key.strip() else None


# ── RAG: build index once for the whole app ────────────────────
@st.cache_resource(show_spinner="Initialising voice assistant...")
def _build_vector_store():
    from rag.ingest import build_vector_store
    return build_vector_store()


def _get_rag():
    try:
        return _build_vector_store()
    except Exception:
        return None, None


# ── Retrieve relevant chunks ───────────────────────────────────
def _retrieve(query: str, collection, model, top_k: int = 3):
    from rag.retriever import retrieve
    return retrieve(query, collection, model, top_k=top_k)


# ── Transcribe audio via Groq Whisper ─────────────────────────
def _transcribe(audio_bytes: bytes) -> str:
    client = _get_groq_client()
    if not client:
        return ""
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = "audio.wav"
    result = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=audio_file,
    )
    return result.text.strip()


# ── RAG retrieve + Groq generate ──────────────────────────────
def _rag_answer(question: str, collection, embed_model):
    client = _get_groq_client()
    if not client:
        return "API key not configured. Reach Akash at kumarakash2009@gmail.com", [], []

    if collection and embed_model:
        context, sources, distances = _retrieve(question, collection, embed_model)
    else:
        context, sources, distances = "No RAG context available.", [], []

    prompt = f"""You are Akash Kumar's professional voice assistant on his portfolio website.
Answer the recruiter's question using ONLY the context provided below.
Be concise — 2 to 3 sentences max.
If the answer is not in the context, say so and share: kumarakash2009@gmail.com

Context:
{context}

Question: {question}
Answer:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip(), sources, distances


# ── Browser TTS ───────────────────────────────────────────────
def _speak(text: str):
    safe = (
        text.replace("\\", "")
            .replace("`", "")
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace("\n", " ")
    )
    st.components.v1.html(
        f"""<script>
        window.speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance('{safe}');
        u.rate = 0.95;
        window.speechSynthesis.speak(u);
        </script>""",
        height=0,
    )


# ══════════════════════════════════════════════════════════════
# MAIN RENDER FUNCTION
# ══════════════════════════════════════════════════════════════

def render_voice_assistant_inline() -> None:

    collection, embed_model = _get_rag()

    # ── Header — matches chat panel style ─────────────────────
    st.markdown(
        """
        <div style="
          background: linear-gradient(135deg, #172554 0%, #0f172a 100%);
          border: 1.5px solid rgba(96,165,250,0.25);
          border-radius: 20px;
          padding: 1.4rem 1.6rem 1rem 1.6rem;
          margin-top: 0.5rem;
        ">
          <div style="font-size:1.25rem; font-weight:800; color:white; margin-bottom:0.25rem;">
            🎙️ Ask Akash — Voice Assistant
          </div>
          <div style="font-size:0.82rem; color:#cbd5e1;">
            Record a question or pick one below — answers are spoken back to you.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── Voice recording ───────────────────────────────────────
    try:
        from st_audiorec import st_audiorec

        st.markdown(
            "<div style='color:#94a3b8; font-size:0.85rem; margin-bottom:0.4rem;'>"
            "🎤 Hit <b>Start Recording</b>, ask your question, then <b>Stop</b>"
            "</div>",
            unsafe_allow_html=True,
        )

        audio_data = st_audiorec()

        if audio_data:
            with st.spinner("Transcribing..."):
                question = _transcribe(audio_data)

            if question:
                st.markdown(
                    f"<div style='color:#94a3b8; font-size:0.85rem;'>You asked: <i>{question}</i></div>",
                    unsafe_allow_html=True,
                )
                with st.spinner("Thinking..."):
                    answer, sources, distances = _rag_answer(question, collection, embed_model)
                st.success(answer)
                _speak(answer)
            else:
                st.warning("Could not transcribe. Please try again or use text below.")

    except ImportError:
        st.info("Install `streamlit-audiorec` for voice input: `pip install streamlit-audiorec`")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    # ── Divider ───────────────────────────────────────────────
    st.markdown(
        "<div style='border-top: 1px solid rgba(148,163,184,0.15); margin: 0.5rem 0 1rem 0;'></div>",
        unsafe_allow_html=True,
    )

    # ── Suggested questions ───────────────────────────────────
    st.markdown(
        "<div style='color:#94a3b8; font-size:0.85rem; margin-bottom:0.6rem;'>"
        "⌨️ Or pick a question"
        "</div>",
        unsafe_allow_html=True,
    )

    suggestions = [
        "What did Akash build at Tesco?",
        "What is Akash's Kafka experience?",
        "Tell me about Akash's AI experience.",
        "What did Akash do at ChargePoint?",
    ]
    cols = st.columns(2)
    for i, s in enumerate(suggestions):
        if cols[i % 2].button(s, key=f"va_suggestion_{i}", use_container_width=True):
            st.session_state["va_question"] = s

    # ── Text input row ────────────────────────────────────────
    col_input, col_clear = st.columns([5, 1], gap="small")
    with col_input:
        text_q = st.chat_input(
            "Type your question about Akash...",
            key="va_chat_input",
        )
    with col_clear:
        if st.button("🗑", key="va_clear_btn", help="Clear answer", use_container_width=True):
            st.session_state.pop("va_question", None)
            st.rerun()

    # Handle suggestion tap
    if "va_question" in st.session_state and not text_q:
        text_q = st.session_state.pop("va_question")

    if text_q:
        with st.spinner("Thinking..."):
            answer, sources, distances = _rag_answer(text_q, collection, embed_model)
        st.success(answer)
        _speak(answer)