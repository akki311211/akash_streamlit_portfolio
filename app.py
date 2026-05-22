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

# ---------------- CSS ----------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown("""
    <div class="sidebar-profile">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="140">
        <h2>Akash Kumar</h2>
        <p>Senior Backend Engineer</p>
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

    st.markdown("""
    <div class="hero-section">

        <div class="hero-left">
            <h4>HELLO 👋</h4>
            <h1>I'm Akash Kumar</h1>

            <h3>
                Distributed Systems • Kafka • Platform Engineering
            </h3>

            <p>
                Senior Backend Engineer with 12+ years of experience
                designing scalable distributed systems across fintech,
                telecom, retail, EV, gaming, and e-commerce domains.
            </p>

            <div class="hero-buttons">
                <a href="https://linkedin.com/in/kumarakash92" target="_blank">
                    <button class="custom-btn">LinkedIn</button>
                </a>

                <a href="mailto:kumarakash2009@gmail.com">
                    <button class="custom-btn-secondary">Contact Me</button>
                </a>
            </div>
        </div>

        <div class="hero-right">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # METRICS
    col1, col2, col3 = st.columns(3)

    metrics = [
        ("12+", "Years Experience"),
        ("1M+", "Events / Minute"),
        ("99.9%", "System Uptime")
    ]

    cols = [col1, col2, col3]

    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <h1>{metrics[idx][0]}</h1>
                <p>{metrics[idx][1]}</p>
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

    st.markdown("<h1 class='section-title'>Experience</h1>", unsafe_allow_html=True)

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
            <h5>{exp['duration']}</h5>

            <ul>
                {''.join([f"<li>{d}</li>" for d in exp['details']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":

    st.markdown("<h1 class='section-title'>Projects</h1>", unsafe_allow_html=True)

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

    st.markdown("<h1 class='section-title'>AI & LLM Engineering</h1>", unsafe_allow_html=True)

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

    st.markdown("<h1 class='section-title'>Contact</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3>Let's Connect</h3>

        <p>📧 kumarakash2009@gmail.com</p>

        <p>🔗 linkedin.com/in/kumarakash92</p>

        <p>📍 Bengaluru, India</p>
    </div>
    """, unsafe_allow_html=True)