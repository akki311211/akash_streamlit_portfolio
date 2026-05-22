import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Akash Kumar Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ----------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.image("profile.jpg", width=160)

    st.markdown("""
    <div style='text-align:center; margin-bottom:30px;'>
        <h2 style='margin-bottom:0;'>Akash Kumar</h2>
        <p style='color:#94A3B8;'>
            Senior Backend Engineer
        </p>
    </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Experience",
            "Projects",
            "Skills",
            "AI/LLM",
            "Contact",
        ],
        icons=[
            "house",
            "briefcase",
            "kanban",
            "cpu",
            "robot",
            "envelope",
        ],
        default_index=0,
    )

# ---------------- HOME ----------------
if selected == "Home":

    left, right = st.columns([1, 2])

    with left:
        st.image("profile.jpg", width=280)

    with right:

        st.markdown("""
        <div class="hero-box">

            <h4>HELLO 👋</h4>

            <h1>I'm Akash Kumar</h1>

            <h3>
                Distributed Systems • Kafka • Platform Engineering
            </h3>

            <p>
                Senior Backend Engineer with 12+ years of experience
                building scalable backend systems across fintech,
                telecom, retail, EV, gaming, and e-commerce domains.
            </p>

        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:
            st.link_button(
                "LinkedIn",
                "https://linkedin.com/in/kumarakash92"
            )

        with c2:
            st.link_button(
                "Contact Me",
                "mailto:kumarakash2009@gmail.com"
            )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # METRICS
    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown("""
        <div class="metric-card">
            <h1>12+</h1>
            <p>Years Experience</p>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="metric-card">
            <h1>1M+</h1>
            <p>Events / Minute</p>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="metric-card">
            <h1>99.9%</h1>
            <p>System Uptime</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ABOUT
    st.markdown("""
    <div class="glass-card">

    <h2>About Me</h2>

    <p>
    Backend Engineer specializing in:
    </p>

    <ul>
        <li>Java & Spring Boot</li>
        <li>Kafka & Event-Driven Systems</li>
        <li>Distributed Systems</li>
        <li>Cloud-Native Architecture</li>
        <li>Platform Engineering</li>
        <li>AI-Assisted Engineering Workflows</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------
elif selected == "Experience":

    st.markdown(
        "<h1 class='section-title'>Experience</h1>",
        unsafe_allow_html=True
    )

    experiences = [
        {
            "company": "Tesco",
            "role": "SDE3",
            "duration": "2025 - Present",
            "details": [
                "Built Messaging-as-a-Service platform",
                "Scaled systems to 1M+ events/minute",
                "Kafka ACL governance automation",
                "AI-assisted observability workflows"
            ]
        },
        {
            "company": "ChargePoint",
            "role": "Staff Software Engineer",
            "duration": "2023 - 2025",
            "details": [
                "Built License Management platform",
                "Created centralized Audit Log platform",
                "Reduced latency by 35%",
                "Improved throughput by 2x"
            ]
        },
        {
            "company": "Airtel",
            "role": "Senior Backend Engineer",
            "duration": "2019 - 2022",
            "details": [
                "Designed telecom backend APIs",
                "Improved uptime to 99.9%",
                "Reduced incidents by 40%"
            ]
        }
    ]

    for exp in experiences:

        st.markdown(f"""
        <div class="timeline-card">

            <h2>{exp['company']}</h2>

            <h4>{exp['role']}</h4>

            <p style="color:#94A3B8;">
                {exp['duration']}
            </p>

            <ul>
                {''.join([f"<li>{d}</li>" for d in exp['details']])}
            </ul>

        </div>
        """, unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":

    st.markdown(
        "<h1 class='section-title'>Projects</h1>",
        unsafe_allow_html=True
    )

    projects = [
        {
            "title": "Messaging-as-a-Service",
            "desc": "Kafka-based self-service platform for topic provisioning and governance.",
            "tech": "Java • Kafka • Spring Boot • Kubernetes"
        },
        {
            "title": "Centralized Audit Log Platform",
            "desc": "High-scale observability and audit event processing platform.",
            "tech": "Kafka • Elasticsearch • Redis"
        },
        {
            "title": "AI-Powered Log Summarization",
            "desc": "LLM-assisted debugging and operational intelligence workflows.",
            "tech": "LLM • Semantic Search • RAG"
        }
    ]

    cols = st.columns(3)

    for idx, project in enumerate(projects):

        with cols[idx]:

            st.markdown(f"""
            <div class="project-card">

                <h3>{project['title']}</h3>

                <p>{project['desc']}</p>

                <div class="tech-stack">
                    {project['tech']}
                </div>

            </div>
            """, unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif selected == "Skills":

    st.markdown(
        "<h1 class='section-title'>Skills</h1>",
        unsafe_allow_html=True
    )

    skills = [
        "Java",
        "Spring Boot",
        "Kafka",
        "AWS",
        "Kubernetes",
        "Redis",
        "MongoDB",
        "Elasticsearch",
        "AI/LLM",
        "Microservices",
        "System Design"
    ]

    skill_html = ""

    for skill in skills:
        skill_html += f"<span class='badge'>{skill}</span>"

    st.markdown(skill_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    data = {
        "Skill": [
            "Java",
            "Kafka",
            "Spring Boot",
            "AWS",
            "Redis",
            "Elasticsearch",
            "AI/LLM"
        ],
        "Expertise": [95, 90, 92, 85, 88, 84, 70]
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Skill",
        y="Expertise",
        title="Technical Expertise",
    )

    fig.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- AI/LLM ----------------
elif selected == "AI/LLM":

    st.markdown(
        "<h1 class='section-title'>AI & LLM Engineering</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="glass-card">

        <ul>
            <li>LLM-assisted log summarization</li>
            <li>Semantic search workflows</li>
            <li>Retrieval-Augmented Generation (RAG)</li>
            <li>AI-assisted debugging</li>
            <li>Observability intelligence</li>
            <li>Engineering productivity tooling</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif selected == "Contact":

    st.markdown(
        "<h1 class='section-title'>Contact</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="glass-card">

        <h3>Let's Connect</h3>

        <p>📧 kumarakash2009@gmail.com</p>

        <p>🔗 linkedin.com/in/kumarakash92</p>

        <p>📍 Bengaluru, India</p>

    </div>
    """, unsafe_allow_html=True)