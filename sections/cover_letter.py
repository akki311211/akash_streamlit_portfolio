"""
Cover Letter Generator — AI-powered, tailored per job description.
Uses gpt-4o-mini with Akash's voice and experience as context.
"""

import streamlit as st


COVER_LETTER_SYSTEM = """You are Akash Kumar's professional writing assistant.
Your task is to write a compelling, personalized cover letter for a job Akash is applying to.

Write in Akash's authentic, confident, and professional first-person voice.
The letter must be:
- Concise (3–4 paragraphs, ~300 words)
- Tailored specifically to the job description provided
- Highlight the most relevant experience and impact metrics from Akash's background
- Open with a strong hook, not "I am writing to apply for..."
- Close with a clear call to action
- Professional but warm in tone — not stiff corporate speak

=== AKASH KUMAR — BACKGROUND FOR COVER LETTER ===

Name: Akash Kumar | Title: Senior Backend Engineer | Location: Bengaluru, India
Email: kumarakash2009@gmail.com
LinkedIn: https://www.linkedin.com/in/kumarakash92/

SUMMARY:
Senior Backend Engineer with 12+ years of experience designing,
building, and scaling distributed systems across retail, fintech,
telecom, EV, gaming, and e-commerce domains.

Specialized in Java, Spring Boot, Kafka, microservices,
event-driven architecture, and cloud-native platform engineering,
with expertise in building high-throughput backend systems
processing millions of events at scale.

CURRENT: Tesco (2025–Present)
- Built Messaging-as-a-Service platform for Kafka ecosystem
- Developed topic provisioning and ACL governance automation
- Scaled distributed systems processing 1M+ events/minute
- Improved platform observability and operational efficiency
- Worked on AI-assisted debugging and log summarization workflows

PREVIOUS: ChargePoint (2023–2025)
- Built centralized Audit Log platform
- Designed License Management backend platform
- Reduced API latency by 35%
- Improved throughput by 2x through backend optimizations
- Enhanced scalability and reliability of distributed services

Airtel (2019–2022)
- Designed telecom backend APIs and distributed services
- Improved uptime to 99.9%
- Reduced production incidents by 40%
- Built scalable event-driven integrations

SKILLS:
Java · Spring Boot · Kafka · Distributed Systems · Microservices ·
AWS · Kubernetes · Redis · MongoDB · Elasticsearch ·
Event-Driven Architecture · Platform Engineering · System Design ·
Observability · AI-assisted Engineering

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

Write the cover letter now, tailored to the job description the user provides.

Do NOT include placeholder brackets like [Company Name].
If the company name is in the job description, use it.
Otherwise write "your team" or "the team" naturally.

Sign off as: Akash Kumar
"""


def _generate_cover_letter(job_description: str, extra_note: str) -> str:
    # Check key exists
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
    except Exception:
        api_key = ""

    if not api_key or api_key.strip() in ("", "sk-YOUR_KEY_HERE"):
        return (
            "🔧 Cover letter generator isn't configured yet — no OpenAI API key found.\n\n"
            "Add your key to `.streamlit/secrets.toml`:\n"
            "  OPENAI_API_KEY = \"sk-...\"\n\n"
            "Once added, refresh the page and try again."
        )

    try:
        from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError
        client = OpenAI(api_key=api_key)

        user_prompt = f"Job Description:\n{job_description}"
        if extra_note.strip():
            user_prompt += f"\n\nExtra context / personal note to weave in:\n{extra_note}"
        user_prompt += "\n\nPlease write the cover letter now."

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
        return (
            "🔑 API key is invalid or expired.\n\n"
            "Please update `OPENAI_API_KEY` in `.streamlit/secrets.toml` with a valid key "
            "from platform.openai.com, then refresh the page."
        )
    except RateLimitError:
        return (
            "⏳ OpenAI rate limit hit. Please wait a moment and try again."
        )
    except APIConnectionError:
        return (
            "🌐 Couldn't connect to OpenAI — check your internet connection and try again."
        )
    except Exception:
        return (
            "⚠️ Something unexpected went wrong generating the cover letter. Please try again."
        )


def render_cover_letter() -> None:
    st.markdown('<h2 class="section-heading">✍️ Cover Letter Generator</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-lede">Paste the job description below and get a tailored, '
        'AI-generated cover letter in Akash\'s voice — ready to send.</p>',
        unsafe_allow_html=True,
    )

    col_input, col_output = st.columns([1, 1], gap="large")

    with col_input:
        st.markdown(
            '<div style="font-weight:700;font-size:0.9rem;color:#334155;margin-bottom:0.4rem;">'
            '📋 Job Description</div>',
            unsafe_allow_html=True,
        )
        job_desc = st.text_area(
            label="job_desc",
            placeholder="Paste the full job description here — role, company, requirements...",
            height=280,
            label_visibility="collapsed",
            key="cl_job_desc",
        )

        st.markdown(
            '<div style="font-weight:700;font-size:0.9rem;color:#334155;margin:0.8rem 0 0.4rem 0;">'
            '💡 Extra Note <span style="font-weight:400;color:#94a3b8;">(optional)</span></div>',
            unsafe_allow_html=True,
        )
        extra = st.text_area(
            label="extra",
            placeholder="Anything specific to highlight? e.g. 'I know the hiring manager from X', "
                        "'Emphasise the Markov Chain project', 'Keep it under 250 words'...",
            height=100,
            label_visibility="collapsed",
            key="cl_extra",
        )

        generate_btn = st.button(
            "✨ Generate Cover Letter",
            use_container_width=True,
            type="primary",
            disabled=not job_desc.strip(),
        )

    with col_output:
        st.markdown(
            '<div style="font-weight:700;font-size:0.9rem;color:#334155;margin-bottom:0.4rem;">'
            '📄 Your Cover Letter</div>',
            unsafe_allow_html=True,
        )

        if "cover_letter_result" not in st.session_state:
            st.session_state.cover_letter_result = ""

        if generate_btn and job_desc.strip():
            with st.spinner("Crafting your cover letter..."):
                result = _generate_cover_letter(job_desc, extra)
                st.session_state.cover_letter_result = result

        if st.session_state.cover_letter_result:
            st.text_area(
                label="result",
                value=st.session_state.cover_letter_result,
                height=420,
                label_visibility="collapsed",
                key="cl_result_display",
            )
            st.download_button(
                label="⬇️ Download as .txt",
                data=st.session_state.cover_letter_result,
                file_name="cover_letter_akash_kumar.txt",
                mime="text/plain",
                use_container_width=True,
            )
        else:
            st.markdown(
                '''
                <div style="
                  height:420px;
                  border:2px dashed #e2e7f0;
                  border-radius:16px;
                  display:flex;
                  flex-direction:column;
                  align-items:center;
                  justify-content:center;
                  color:#94a3b8;
                  text-align:center;
                  padding:2rem;
                ">
                  <div style="font-size:2.5rem;margin-bottom:0.8rem;">✉️</div>
                  <div style="font-size:0.97rem;font-weight:600;">Your cover letter appears here</div>
                  <div style="font-size:0.83rem;margin-top:0.4rem;">
                    Paste a job description and click Generate
                  </div>
                </div>
                ''',
                unsafe_allow_html=True,
            )
