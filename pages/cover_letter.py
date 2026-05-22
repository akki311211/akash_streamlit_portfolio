"""
Cover Letter Generator — private page (not linked from the main site).
Access at: http://localhost:8501/cover_letter
"""

from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Cover Letter Generator", page_icon="✍️", layout="wide")

# Inject styles
css_path = Path(__file__).parent.parent / "styles.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# ---- Hide Streamlit sidebar nav so page feels standalone ----
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"]    { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

COVER_LETTER_SYSTEM = """You are Rohit Jindal's professional writing assistant.
Write a compelling, personalized cover letter for a job Rohit is applying to.

Write in Rohit's authentic, confident, and professional first-person voice.
The letter must be:
- Concise (3-4 paragraphs, ~300 words)
- Tailored specifically to the job description provided
- Highlight the most relevant experience and impact metrics
- Open with a strong hook (NOT "I am writing to apply for...")
- Close with a clear call to action
- Professional but warm

=== ROHIT JINDAL — BACKGROUND ===
Name: Rohit Jindal | Title: Senior Data Scientist | Location: Bangalore, India
Email: jindal.rohit540@gmail.com | Phone: +91 79826 91190
LinkedIn: https://www.linkedin.com/in/jindal-rohit540/

SUMMARY: 5+ years building production-grade Applied AI and GenAI systems across
supply chain, finance, and customer operations — $3.5M+ annual business impact.
Expert in agentic RAG, large-scale forecasting, inventory optimization, and
end-to-end MLOps (CI/CD, observability, evaluation) on Microsoft Fabric and Databricks.

CURRENT: Senior Data Scientist, Target Corporation (Aug 2023–Present)
- Agentic RAG (LangGraph, LangChain, FAISS/Qdrant) for Finance Operations
- 12-week demand forecasting on Microsoft Fabric + PySpark
- Markov-Chain inventory optimization: ~$2.5M annual impact, 78% OOS recall
- Siamese-BERT PCC classifier: ~$1M annual savings, 78% accuracy
- LLM eval + observability (LangSmith); CI/CD with GitHub Actions + Docker

PREVIOUS:
- Mastercard AI Garage (2021): fraud detection +7% recall, ICAIF 2021 paper
- State Street Global Advisors: 'Short Interest Surprise' equity factor, ~2.3% alpha
- Chicago Public Schools: absenteeism & meal demand models, Microsoft Fabric migration
- IRCON International (2019–2021): ML on ₹1,600-crore infrastructure project

EDUCATION:
- M.Tech Data & Analytics, IISc Bangalore (CGPA 8.2/10)
- B.Tech, Delhi College of Engineering (DTU), 80%
- Executive Program, University of Cambridge & BITS Pilani

TEACHING: Springboard instructor (RAG, LLM System Design),
REVA University NLP trainer, 100+ professionals mentored, 700+ hours taught.

SKILLS: LangGraph · LangChain · LangSmith · RAG · Agentic AI · FAISS · Qdrant ·
Microsoft Fabric · PySpark · XGBoost · Siamese-BERT · Transformers · Databricks ·
Spark · Docker · Kubernetes · MLflow · GitHub Actions · Python · R · SQL

Sign off as: Rohit Jindal
Do NOT use placeholder brackets like [Company Name] — infer from JD or write "your team".
"""

DEFAULT_COVER_LETTER = """Dear Hiring Manager,

I bring something that is genuinely rare: the mathematical rigor of India's top research institution (IISc, M.Tech Data & Analytics, CGPA 8.2), real-world industry impact at scale (Senior Data Scientist at Target Corporation, $3.5M+ annual business impact), and the communication clarity of someone who has taught 700+ hours to working professionals at Springboard and REVA University.

At Target, I architected production Agentic RAG systems using LangGraph and LangChain that automated Finance Operations document workflows, built a 12-week demand forecasting product on Microsoft Fabric that runs fully automated every Sunday, and developed a Markov-Chain inventory optimization system delivering ~$2.5M in annual impact at ~78% out-of-stock recall. Before that, at Mastercard AI Garage, I improved fraud detection recall by 7% on 15M+ transactions — work that earned a paper acceptance at ICAIF 2021 (ACM). At State Street Global Advisors, I developed a novel equity factor that improved portfolio performance by ~7% and generated ~2.3% alpha.

What I bring beyond technical depth is articulation. Three years of teaching advanced AI/ML — from RAG pipelines and LLM System Design to statistical foundations — has made me someone who can communicate complex ideas clearly to engineers, product managers, and business stakeholders alike. That makes me effective not just as an individual contributor, but as someone who elevates the people around them.

I am actively looking for Senior / Staff Data Scientist or GenAI roles where I can have genuine business impact, work on hard problems, and continue growing. I would love the opportunity to speak with your team.

Warm regards,
Rohit Jindal
📧 jindal.rohit540@gmail.com · 📱 +91 79826 91190
🔗 linkedin.com/in/jindal-rohit540/"""


def _generate_cover_letter(job_description: str, extra_note: str) -> str:
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
    except Exception:
        api_key = ""

    if not api_key or api_key.strip() in ("", "sk-YOUR_KEY_HERE"):
        return (
            "🔧 API key not configured in `.streamlit/secrets.toml`.\n\n"
            "Showing the default cover letter instead:\n\n---\n\n" + DEFAULT_COVER_LETTER
        )

    try:
        from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError
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
            temperature=0.65,
        )
        return response.choices[0].message.content.strip()

    except AuthenticationError:
        return "🔑 API key invalid — update `.streamlit/secrets.toml`.\n\n---\n\n" + DEFAULT_COVER_LETTER
    except RateLimitError:
        return "⏳ Rate limited. Try again in a moment.\n\n---\n\n" + DEFAULT_COVER_LETTER
    except APIConnectionError:
        return "🌐 Connection error — check internet.\n\n---\n\n" + DEFAULT_COVER_LETTER
    except Exception:
        return "⚠️ Unexpected error.\n\n---\n\n" + DEFAULT_COVER_LETTER


# ── PAGE LAYOUT ──────────────────────────────────────────────
st.markdown('<h1 class="section-heading">✍️ Cover Letter Generator</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-lede">Private tool — not linked from the main site. '
    'Paste a job description to generate a tailored letter. '
    'Leave blank to see the default general cover letter.</p>',
    unsafe_allow_html=True,
)
st.markdown("---")

col_input, col_output = st.columns([1, 1], gap="large")

with col_input:
    st.markdown("**📋 Job Description** *(optional)*")
    job_desc = st.text_area(
        label="jd",
        placeholder="Paste the job description here. Leave blank for a general cover letter.",
        height=260,
        label_visibility="collapsed",
    )
    st.markdown("**💡 Extra Note** *(optional)*")
    extra = st.text_area(
        label="extra",
        placeholder="e.g. 'Emphasise the Markov Chain project', 'Keep it under 250 words'...",
        height=100,
        label_visibility="collapsed",
    )
    generate_btn = st.button("✨ Generate Cover Letter", use_container_width=True, type="primary")

with col_output:
    st.markdown("**📄 Cover Letter**")

    if "cl_result" not in st.session_state:
        # Show default on first load
        st.session_state.cl_result = DEFAULT_COVER_LETTER

    if generate_btn:
        if job_desc.strip():
            with st.spinner("Generating tailored cover letter..."):
                st.session_state.cl_result = _generate_cover_letter(job_desc, extra)
        else:
            st.session_state.cl_result = DEFAULT_COVER_LETTER

    result = st.session_state.cl_result
    st.text_area(label="out", value=result, height=440, label_visibility="collapsed")
    st.download_button(
        label="⬇️ Download as .txt",
        data=result,
        file_name="cover_letter_rohit_jindal.txt",
        mime="text/plain",
        use_container_width=True,
    )
