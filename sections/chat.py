import os
import streamlit as st
from groq import Groq

# ---------------- CONTEXT ----------------

AKASH_CONTEXT = """
You are Akash Kumar's professional AI assistant on his personal website.

Answer questions from recruiters, interviewers, hiring managers,
and collaborators about Akash Kumar.

Be professional, warm, concise, and technically strong.

Keep answers under 150 words unless more detail is needed.

STRICT RULE:
Only answer questions about:
- backend engineering
- distributed systems
- Kafka
- platform engineering
- AI-assisted engineering workflows
- projects
- experience
- skills
- education
- architecture
- scalability
- microservices
- cloud-native engineering

If asked anything outside this scope,
politely decline and share contact details.

If you don't know a specific detail,
say so and share contact details.

Never hallucinate fake experience.

Contact fallback:
"Reach Akash directly at kumarakash2009@gmail.com"

================ PROFILE ================

NAME: Akash Kumar
TITLE: Senior Backend Engineer
LOCATION: Bengaluru, India

EMAIL:
kumarakash2009@gmail.com

LINKEDIN:
https://linkedin.com/in/kumarakash92

SUMMARY:

Senior Backend Engineer with 12+ years of experience
designing, building, and scaling distributed systems
across retail, fintech, telecom, EV, gaming,
and e-commerce domains.

SPECIALIZATION:
- Java
- Spring Boot
- Kafka
- Distributed Systems
- Event-Driven Architecture
- Microservices
- AWS
- Kubernetes
- Redis
- Elasticsearch
- Platform Engineering
- AI-assisted Engineering

TESCO:
- Messaging-as-a-Service platform
- Kafka governance automation
- 1M+ events/minute
- AI-assisted observability workflows

CHARGEPOINT:
- Centralized Audit Log Platform
- License Management platform
- Reduced latency by 35%
- Improved throughput by 2x

AIRTEL:
- Telecom backend APIs
- Improved uptime to 99.9%
- Reduced incidents by 40%

AI/LLM EXPOSURE:
- LLM-based log summarization
- Semantic search
- Observability intelligence
- Foundational RAG concepts
- AI-assisted debugging workflows

OPEN TO:
- Staff Engineer roles
- Principal Engineer roles
- Platform Engineering
- Distributed Systems Engineering
"""

# ---------------- INITIAL MESSAGE ----------------

_INITIAL_MSG = {
    "role": "assistant",
    "content": (
        "Hi! I'm Akash's AI assistant. "
        "Ask me anything about his experience, "
        "projects, backend engineering, distributed systems, "
        "Kafka, or platform engineering expertise 👋"
    ),
}

# ---------------- API KEY ----------------

def _get_api_key() -> str:

    try:
        key = st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        key = ""

    if not key:
        key = os.environ.get("GROQ_API_KEY", "")

    return (key or "").strip()

# ---------------- AI RESPONSE ----------------

def _get_ai_response(messages: list) -> str:

    api_key = _get_api_key()

    if not api_key:

        return (
            "The AI assistant isn't live yet — the API key isn't configured.\n\n"
            "In the meantime, reach Akash directly:\n"
            "📧 **kumarakash2009@gmail.com**"
        )

    try:

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": AKASH_CONTEXT
                }
            ] + messages,
            max_tokens=300,
            temperature=0.5,
        )

        reply = response.choices[0].message.content.strip()

        # ---------------- FALLBACK ENFORCEMENT ----------------

        fallback_phrases = [
            "i don't know",
            "i do not know",
            "not sure",
            "no information",
            "don't have information",
            "cannot find",
            "not available",
            "unknown",
        ]

        if any(p in reply.lower() for p in fallback_phrases):

            reply += (
                "\n\n📧 Reach Akash directly at "
                "**kumarakash2009@gmail.com**"
            )

        return reply

    except Exception as e:

        return (
            f"⚠️ {str(e)}\n\n"
            "📧 Reach Akash directly at "
            "**kumarakash2009@gmail.com**"
        )

# ---------------- CHAT RENDER ----------------

def render_chat_inline() -> None:
    """
    Renders an inline AI chat panel.
    """

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [_INITIAL_MSG]

    # ---------------- HEADER ----------------

    st.markdown(
        """
        <div style="
          background: linear-gradient(135deg, #172554 0%, #0f172a 100%);
          border: 1.5px solid rgba(96,165,250,0.25);
          border-radius: 20px;
          padding: 1.4rem 1.6rem 1rem 1.6rem;
          margin-top: 0.5rem;
        ">
          <div style="
            font-size:1.25rem;
            font-weight:800;
            color:white;
            margin-bottom:0.25rem;
          ">
            💬 AI Chat with Akash
          </div>

          <div style="
            font-size:0.82rem;
            color:#cbd5e1;
            margin-bottom:0.8rem;
          ">
            Ask about backend engineering, Kafka,
            distributed systems, platform engineering,
            or AI-assisted engineering workflows.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- CHAT AREA ----------------

    chat_container = st.container()

    with chat_container:

        for msg in st.session_state.chat_messages:

            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # ---------------- INPUT ROW ----------------

    col_input, col_clear = st.columns([5, 1], gap="small")

    with col_input:

        user_input = st.chat_input(
            "Ask about Akash...",
            key="chat_input_main"
        )

    with col_clear:

        if st.button(
            "🗑",
            help="Clear chat",
            use_container_width=True,
            key="chat_clear_btn"
        ):

            st.session_state.chat_messages = [_INITIAL_MSG]

            st.rerun()

    # ---------------- USER INPUT ----------------

    if user_input:

        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })

        api_msgs = [
            {
                "role": m["role"],
                "content": m["content"]
            }
            for m in st.session_state.chat_messages
            if m["role"] in ("user", "assistant")
        ][-10:]

        with st.spinner("Thinking..."):

            reply = _get_ai_response(api_msgs)

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": reply
        })

        st.rerun()