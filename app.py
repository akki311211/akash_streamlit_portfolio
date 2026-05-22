import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Akash Kumar Portfolio",
    page_icon="🚀",
    layout="wide",
)

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Akash Kumar",
        options=[
            "Home",
            "About",
            "Experience",
            "Projects",
            "Skills",
            "AI/LLM",
            "System Design",
            "Contact"
        ],
        icons=[
            "house",
            "person",
            "briefcase",
            "kanban",
            "gear",
            "cpu",
            "diagram-3",
            "envelope"
        ],
        default_index=0,
    )

if selected == "Home":
    st.title("Akash Kumar")
    st.subheader(
        "Senior Backend Engineer | Distributed Systems | Kafka | Platform Engineering"
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("""
        Backend Engineer with 12+ years of experience designing scalable distributed systems
        across retail, fintech, telecom, EV, gaming, and e-commerce domains.
        """)

    with col2:
        st.metric("Experience", "12+ Years")
        st.metric("Events Processed", "1M+/min")
        st.metric("System Uptime", "99.9%")

elif selected == "About":
    st.header("About Me")
    st.write("""
    Senior Backend Software Engineer with strong expertise in:
    - Java & Spring Boot
    - Kafka & Event-Driven Systems
    - Distributed Architecture
    - Cloud-Native Platforms
    - AI-Assisted Engineering Workflows
    """)

elif selected == "Experience":
    st.header("Professional Experience")

    experiences = [
        {
            "company": "Tesco",
            "role": "SDE3",
            "duration": "2025 - Present",
        },
        {
            "company": "ChargePoint",
            "role": "Staff Software Engineer",
            "duration": "2023 - 2025",
        },
        {
            "company": "Airtel",
            "role": "Senior Backend Engineer",
            "duration": "2019 - 2022",
        }
    ]

    for exp in experiences:
        st.subheader(f'{exp["company"]} — {exp["role"]}')
        st.caption(exp["duration"])

elif selected == "Projects":
    st.header("Featured Projects")

    st.markdown("""
    ### Messaging-as-a-Service Platform
    Kafka-based self-service platform for topic provisioning and governance.

    ### Centralized Audit Log Platform
    High-scale observability and audit event processing system.

    ### AI-Powered Log Summarization
    LLM-assisted operational intelligence and RCA workflows.
    """)

elif selected == "Skills":
    st.header("Technical Skills")

    skills = {
        "Skill": [
            "Java",
            "Spring Boot",
            "Kafka",
            "AWS",
            "Kubernetes",
            "Redis",
            "MongoDB",
            "Elasticsearch",
            "AI/LLM"
        ],
        "Expertise": [95, 92, 90, 85, 80, 88, 84, 82, 70]
    }

    df = pd.DataFrame(skills)

    fig = px.bar(
        df,
        x="Skill",
        y="Expertise",
        title="Technical Expertise",
    )

    st.plotly_chart(fig, use_container_width=True)

elif selected == "AI/LLM":
    st.header("AI & LLM Engineering")

    st.write("""
    - Log summarization using LLMs
    - Semantic search concepts
    - Retrieval-Augmented Generation (RAG)
    - Observability intelligence
    """)

elif selected == "System Design":
    st.header("System Design Showcase")

    st.write("""
    - Kafka-based event streaming
    - API-first platform
    - ACL & governance automation
    - High-throughput distributed systems
    """)

elif selected == "Contact":
    st.header("Contact")

    st.write("📧 Email: kumarakash2009@gmail.com")
    st.write("🔗 LinkedIn: https://linkedin.com/in/kumarakash92")
    st.write("📍 Bengaluru, India")
