"""
Cover Letter Generator — private page (not linked from the main site).
Access at: http://localhost:8501/cover_letter
"""

from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Cover Letter Generator",
    page_icon="✍️",
    layout="wide",
)

# ── Inject styles ────────────────────────────────────────────
css_path = Path(__file__).parent.parent / "styles.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# ── Hide sidebar/nav ─────────────────────────────────────────
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════
# SYSTEM PROMPT
# ══════════════════════════════════════════════════════════════

COVER_LETTER_SYSTEM = """
You are Akash Kumar's professional writing assistant.

Write a compelling, personalized cover letter for jobs Akash is applying to.

The tone should be:
- Senior/staff-level
- Confident but not arrogant
- Crisp and impact-focused
- Professional and modern

The letter must:
- Be 3-4 concise paragraphs
- Stay under ~350 words
- Be tailored to the job description
- Highlight leadership + backend engineering depth
- Mention distributed systems and platform ownership where relevant
- Avoid generic buzzwords
- End with a strong but concise closing

=== AKASH KUMAR — BACKGROUND ===

Name: Akash Kumar
Title: Staff / Senior Backend Engineer
Location: Bangalore, India

SUMMARY:
Backend and distributed systems engineer with experience building
high-scale platforms, event-driven architectures, streaming systems,
internal developer platforms, and cloud-native applications.

Strong experience across:
- Java
- Spring Boot
- Microservices
- Apache Kafka
- Distributed Systems
- AWS
- Kubernetes
- Cassandra
- Redis
- Elasticsearch

CURRENT ROLE:
Tesco
- Messaging as a Service platform
- Internal developer platform for Kafka/topic provisioning
- API-first architecture for topic/user/ACL management
- High-scale backend systems
- Platform engineering and developer enablement

PREVIOUS EXPERIENCE:
- ChargePoint → License Management platform
- Backend architecture and platform scalability
- Event-driven systems and cloud-native engineering
- Experience mentoring engineers and leading initiatives

LEADERSHIP:
- Technical leadership
- Mentoring engineers
- Cross-functional collaboration
- Architecture reviews
- Delivery ownership

SKILLS:
Java · Spring Boot · Kafka · Microservices · Distributed Systems ·
AWS · Kubernetes · Cassandra · Redis · Elasticsearch · Docker ·
CI/CD · REST APIs · Event-Driven Architecture · System Design

Sign off as:
Akash Kumar

Do not use placeholders like [Company Name].
Infer company/team context from the JD if possible.
"""

# ══════════════════════════════════════════════════════════════
# DEFAULT COVER LETTER
# ══════════════════════════════════════════════════════════════

DEFAULT_COVER_LETTER = """
Dear Hiring Manager,

I enjoy building backend platforms that solve hard scalability and developer productivity problems. Over the last several years, I have worked extensively on distributed systems, event-driven architectures, and internal platforms powering large-scale engineering ecosystems.

At Tesco, I am part of the team building Messaging as a Service — a platform enabling teams across the organization to seamlessly create and manage Kafka topics, users, ACLs, and streaming infrastructure through API-first workflows. My work involves designing scalable backend services, improving developer experience, and ensuring reliability across high-throughput systems. Prior to this, I worked on backend platforms including license management systems and cloud-native applications focused on scalability and operational efficiency.

My strengths lie in backend engineering, system design, distributed systems, and technical leadership. I have strong hands-on experience with Java, Spring Boot, Kafka, AWS, Kubernetes, Cassandra, Redis, and Elasticsearch. Alongside engineering execution, I actively mentor engineers, contribute to architecture discussions, and drive cross-functional delivery initiatives.

I am currently exploring Senior/Staff Backend Engineering opportunities where I can contribute to large-scale platform engineering challenges and help build high-impact systems. I would welcome the opportunity to connect and discuss how I can contribute to your team.

Best regards,
Akash Kumar
"""

# ══════════════════════════════════════════════════════════════
# GENERATION FUNCTION
# ══════════════════════════════════════════════════════════════

def _generate_cover_letter(job_description: str, extra_note: str) -> str:
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
    except Exception:
        api_key = ""

    if not api_key or api_key.strip() in ("", "sk-YOUR_KEY_HERE"):
        return (
            "🔧 API key not configured in `.streamlit/secrets.toml`.\n\n"
            "Showing the default cover letter instead:\n\n---\n\n"
            + DEFAULT_COVER_LETTER
        )

    try:
        from openai import (
            OpenAI,
            AuthenticationError,
            RateLimitError,
            APIConnectionError,
        )

        client = OpenAI(api_key=api_key)

        user_prompt = f"Job Description:\n{job_description}"

        if extra_note.strip():
            user_prompt += f"\n\nExtra context:\n{extra_note}"

        user_prompt += "\n\nWrite the cover letter now."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": COVER_LETTER_SYSTEM},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=700,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except AuthenticationError:
        return (
            "🔑 API key invalid — update `.streamlit/secrets.toml`.\n\n---\n\n"
            + DEFAULT_COVER_LETTER
        )

    except RateLimitError:
        return (
            "⏳ Rate limited. Try again shortly.\n\n---\n\n"
            + DEFAULT_COVER_LETTER
        )

    except APIConnectionError:
        return (
            "🌐 Connection error — check internet.\n\n---\n\n"
            + DEFAULT_COVER_LETTER
        )

    except Exception:
        return (
            "⚠️ Unexpected error occurred.\n\n---\n\n"
            + DEFAULT_COVER_LETTER
        )

# ══════════════════════════════════════════════════════════════
# PAGE UI
# ══════════════════════════════════════════════════════════════

st.markdown(
    '<h1 class="section-heading">✍️ Cover Letter Generator</h1>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="section-lede">'
    'Private tool — generate tailored backend engineering cover letters '
    'based on a job description.'
    '</p>',
    unsafe_allow_html=True,
)

st.markdown("---")

col_input, col_output = st.columns([1, 1], gap="large")

# ── INPUT ────────────────────────────────────────────────────
with col_input:
    st.markdown("### 📋 Job Description")

    job_desc = st.text_area(
        label="jd",
        placeholder="Paste the job description here...",
        height=280,
        label_visibility="collapsed",
    )

    st.markdown("### 💡 Extra Instructions")

    extra = st.text_area(
        label="extra",
        placeholder=(
            "Example:\n"
            "- Emphasize Kafka experience\n"
            "- Keep under 250 words\n"
            "- Focus on platform engineering"
        ),
        height=120,
        label_visibility="collapsed",
    )

    generate_btn = st.button(
        "✨ Generate Cover Letter",
        type="primary",
        use_container_width=True,
    )

# ── OUTPUT ───────────────────────────────────────────────────
with col_output:
    st.markdown("### 📄 Generated Cover Letter")

    if "cl_result" not in st.session_state:
        st.session_state.cl_result = DEFAULT_COVER_LETTER

    if generate_btn:
        if job_desc.strip():
            with st.spinner("Generating tailored cover letter..."):
                st.session_state.cl_result = _generate_cover_letter(
                    job_desc,
                    extra,
                )
        else:
            st.session_state.cl_result = DEFAULT_COVER_LETTER

    result = st.session_state.cl_result

    st.text_area(
        label="output",
        value=result,
        height=500,
        label_visibility="collapsed",
    )

    st.download_button(
        label="⬇️ Download as TXT",
        data=result,
        file_name="cover_letter_akash_kumar.txt",
        mime="text/plain",
        use_container_width=True,
    )