import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Akash Kumar Portfolio",
    page_icon="🚀",
    layout="wide",
)

# LOAD CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        menu_title="Akash Kumar",
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
            "gear",
            "cpu",
            "envelope",
        ],
        menu_icon="cast",
        default_index=0,
    )

# HOME
if selected == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        st.image("profile.jpg", width=280)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hero">
            <h1>Akash Kumar</h1>
            <h3>Senior Backend Engineer</h3>
            <p>
            Distributed Systems • Kafka • Platform Engineering • AI-Assisted Observability
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>12+</h2>
            <p>Years Experience</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>1M+</h2>
            <p>Events / Minute</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>99.9%</h2>
            <p>System Uptime</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
    <h2>About Me</h2>

    Backend Engineer with 12+ years of experience building scalable distributed systems
    across retail, fintech, telecom, EV, gaming, and e-commerce domains.

    Specialized in:
    <ul>
        <li>Java & Spring Boot</li>
        <li>Kafka & Event-Driven Systems</li>
        <li>Distributed Architecture</li>
        <li>Cloud-Native Platforms</li>
        <li>AI-Assisted Engineering Workflows</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# EXPERIENCE
elif selected == "Experience":

    st.markdown("<h1 class='section-title'>Experience</h1>", unsafe_allow_html=True)

    experiences = [
        {
            "company": "Tesco",
            "role": "SDE3",
            "duration": "2025 - Present",
            "points": [
                "Built Messaging-as-a-Service platform",
                "Scaled systems to 1M+ events/minute",
                "Kafka topic provisioning automation",
                "AI-assisted log summarization"
            ]
        },
        {
            "company": "ChargePoint",
            "role": "Staff Software Engineer",
            "duration": "2023 - 2025",
            "points": [
                "Built License Management platform",
                "Created centralized Audit Log platform",
                "Reduced API latency by 35%",
                "Improved throughput by 2x"
            ]
        },
        {
            "company": "Airtel",
            "role": "Senior Backend Engineer",
            "duration": "2019 - 2022",
            "points": [
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
            <p><i>{exp['duration']}</i></p>
            <ul>
                {''.join([f"<li>{p}</li>" for p in exp['points']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS
elif selected == "Projects":

    st.markdown("<h1 class='section-title'>Projects</h1>", unsafe_allow_html=True)

    projects = [
        {
            "title": "Messaging-as-a-Service Platform",
            "desc": "Kafka-based self-service platform for topic provisioning and governance.",
            "tech": "Java • Kafka • Spring Boot • Kubernetes"
        },
        {
            "title": "Centralized Audit Log Platform",
            "desc": "High-scale observability and audit event processing system.",
            "tech": "Kafka • Elasticsearch • Redis"
        },
        {
            "title": "AI-Powered Log Summarization",
            "desc": "LLM-assisted operational intelligence and RCA workflows.",
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
                <div class="tech-stack">{project['tech']}</div>
            </div>
            """, unsafe_allow_html=True)

# SKILLS
elif selected == "Skills":

    st.markdown("<h1 class='section-title'>Skills</h1>", unsafe_allow_html=True)

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
        "System Design",
    ]

    badges = ""

    for skill in skills:
        badges += f"<span class='badge'>{skill}</span>"

    st.markdown(f"<div>{badges}</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    skill_data = {
        "Skill": [
            "Java",
            "Kafka",
            "Spring Boot",
            "AWS",
            "Redis",
            "Elasticsearch",
            "AI/LLM",
        ],
        "Expertise": [95, 90, 92, 85, 88, 84, 70],
    }

    df = pd.DataFrame(skill_data)

    fig = px.bar(
        df,
        x="Skill",
        y="Expertise",
        title="Technical Expertise",
    )

    fig.update_layout(
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font_color="white",
    )

    st.plotly_chart(fig, use_container_width=True)

# AI/LLM
elif selected == "AI/LLM":

    st.markdown("<h1 class='section-title'>AI & LLM Engineering</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <ul>
            <li>LLM-assisted log summarization</li>
            <li>Semantic search concepts</li>
            <li>Retrieval-Augmented Generation (RAG)</li>
            <li>Observability intelligence</li>
            <li>AI-assisted debugging workflows</li>
            <li>Engineering productivity tooling</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# CONTACT
elif selected == "Contact":

    st.markdown("<h1 class='section-title'>Contact</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3>Let's Connect</h3>

        📧 kumarakash2009@gmail.com

        🔗 https://linkedin.com/in/kumarakash92

        📍 Bengaluru, India
    </div>
    """, unsafe_allow_html=True)