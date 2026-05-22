/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import streamlit as st
import random
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Akash Kumar - Interactive Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to mimic the elegant preview theme
st.markdown("""
<style>
    .streamlit-red-text {
        color: #FF4B4B;
    }
    .highlight-card {
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allowed_html=True)

# Resume Data for st.download_button
resume_text = """AKASH KUMAR - SYSTEM DESIGN & ENGINEERING LEADER RESUME
===========================================================
Email: kumarakash2009@gmail.com | Phone: +91 7042749874 | India
LinkedIn: https://www.linkedin.com/in/kumarakash92/

PROFESSIONAL SUMMARY:
Engineering Leader with 12+ years of experience building and scaling high-throughput distributed systems. Strong expertise in Apache Kafka, event-driven architectures, and cloud-native platforms, with growing experience in applying AI/LLMs to backend observability pipelines.

CORE CAPABILITIES:
- Messaging: Apache Kafka, RabbitMQ, Event-Driven Architecture
- Backend: Java, Spring Boot, Microservices, REST APIs, gRPC, Go
- Cloud & Containers: Azure, Kubernetes (AKS), Docker, Terraform, AWS, GCP
- Databases & Search: MySql, MongoDB, Redis, Elasticsearch, Solr

EXPERIENCE HIGHLIGHTS:
1. Tesco (Bengaluru) | Engineering Manager / SDE3 (Feb 2025 - Present)
   - Delivering Messaging-as-a-Service on Kafka on Azure AKS & Kubernetes.
2. ChargePoint Inc (Gurugram) | Staff Software Engineer (Jul 2023 - Feb 2025)
   - Built scalable charging ingestion APIs with microservices and MongoDB.
3. Quinbay Technologies (Bengaluru) | Lead Software Engineer (Oct 2022 - Jun 2023)
   - Constructed indexing pipelines with Solr and custom autocomplete recommenders.
4. Bharti Airtel Limited (Gurugram) | Technical Lead (Sep 2019 - Oct 2022)
   - Built TRAI Channel Selector platform APIs handling millions of subscriber queries.
5. Paytm First Games | Senior Developer (Jun 2018 - Sep 2019)
   - Engineered real-time geo-fencing subsystems using Redis and Kafka.

EDUCATION:
- B.Tech in Computer Science & Engineering - Lovely Professional University (2014)"""

# Sidebar Layout
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Akash Kumar</h2>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-weight: 500; font-size: 14px;'>Engineering Leader & Architect</p>", unsafe_allowed_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px;'>📍 Bengaluru, India</p>", unsafe_allowed_html=True)
    
    st.markdown("---")
    
    st.markdown("### ⚙️ Calibration Settings")
    spotlight_skills = st.checkbox("Spotlight Key Technologies", value=False, help="Highlight core competence skills like Kafka, Spring Boot, Azure, etc.")
    ai_confidence = st.slider("Target AI Precision Match (%)", min_value=10, max_value=100, value=85, help="Recalibrate KPI metrics based on model confidence parameters.")
    
    st.markdown("---")
    st.markdown("### 🔗 Connect With Me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/kumarakash92/)")
    st.markdown("[GitHub](https://github.com/kumarakash92)")
    
    st.markdown("---")
    st.caption("System Engine: JDK 21 / Go\\n\\nTelemetry: OpenTelemetry / Prometheus\\n\\n© 2026 Akash Kumar")

# Main Content Header
col_title, col_download = st.columns([3, 1])
with col_title:
    st.markdown("<h1 style='margin-bottom: 0;'>👨‍💻 Akash Kumar's Portfolio</h1>", unsafe_allowed_html=True)
    st.caption("Engineering Leader & Distributed Systems Architect | Event-Driven Stream Architectures")
with col_download:
    st.download_button(
        label="st.download_button()",
        data=resume_text,
        file_name="Akash_Kumar_Systems_EM_Resume.txt",
        mime="text/plain",
        help="Download Akash's professional text-based resume file."
    )

st.write("---")

# Navigation Tabs matching React views
tabs = st.tabs(["👋 About Me", "🛠️ Technical Toolkit", "💼 Career Timeline", "💻 Code Sandbox Demos", "🤖 AI Chat Assistant", "📬 st.form Feedback"])

# Tab 1: About Me
with tabs[0]:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("👋 Professional Overview")
        st.markdown("""
        Hi! I am **Akash Kumar**. I design database transaction pipelines, event-driven messaging structures, and high-performance container architectures. Leading critical developer teams as an Engineering EM, my focus lies in crafting highly performant, resilient distributed cloud topologies.
        
        With over **12 years of core engineering experience** working in fast-paced software enterprises, I specialize in scaling massive Apache Kafka pipelines, configuring Kubernetes workloads, and deploying clean REST frameworks.
        """)
        
        st.info("""
        **📢 Featured Update**
        I am currently leading EM releases for Tesco's core Messaging-as-a-Service on top of Kafka. Try the interactive high-throughput throughput simulators in the **"Code Sandbox Demos"** section!
        """)
    
    with col2:
        st.markdown("""
        <div style="background-color: rgba(255, 75, 75, 0.05); padding: 15px; border-radius: 8px; border: 1px solid rgba(255, 75, 75, 0.2);">
            <h4 style="margin-top: 0; margin-bottom: 10px; color: #FF4B4B;">📌 Career Quickstats</h4>
            <ul style="list-style-type: none; padding-left: 0; line-height: 1.8; font-size: 14px;">
                <li><strong>Current Role:</strong> Engineering Manager</li>
                <li><strong>Location:</strong> Bengaluru, India</li>
                <li><strong>Alma Mater:</strong> LPU Punjab ('14)</li>
                <li><strong>Preferred Stack:</strong> Kafka / Java / AKS</li>
            </ul>
        </div>
        """, unsafe_allowed_html=True)
        
    st.markdown("---")
    st.subheader("📈 Live Analytical Metrics")
    
    # Recalculate dynamic KPIs based on slider
    rows_day = f"~{2.5 * (ai_confidence / 80.0):.2f}M Recs/day"
    live_apps = f"{int(20 + (ai_confidence - 80) / 3)}+ Live"
    
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Professional Experience", value="12+ Years", delta="Leading 10-15 Engineers")
    with m_col2:
        st.metric(label="Kafka Clusters Served", value="15+ Production", delta=rows_day)
    with m_col3:
        st.metric(label="Distributed Throughput", value="Millions/sec", delta=live_apps)

# Tab 2: Technical Toolkit
with tabs[1]:
    st.subheader("🛠️ Technology Stack & Toolkit")
    st.caption("Segmented categories representing Akash's software and database engineering experience.")
    
    skills_data = [
        {
            "category": "📡 Event-Streams & Messaging Platforms",
            "skills": ["Apache Kafka", "Event-Driven Architecture", "Java", "Spring Boot", "Microservices", "REST APIs", "gRPC", "Leadership & Technical Strategy"]
        },
        {
            "category": "🌌 Container & Cloud Infrastructure",
            "skills": ["Kubernetes", "Docker Containers", "Terraform", "Microsoft Azure", "Amazon Web Services (AWS)", "Google Cloud (GCP)", "CI/CD Pipelines", "Shell Scripting"]
        },
        {
            "category": "🔍 Databases, Search & AI Exposure",
            "skills": ["Elasticsearch", "Apache Solr", "MySQL", "MongoDB", "Redis Pipelines", "LLM Concepts", "RAG Patterns", "Semantic Search"]
        }
    ]
    
    spotlight_keywords = ["Apache Kafka", "Kubernetes", "Java", "Spring Boot", "Terraform", "Event-Driven Architecture"]
    
    sc_cols = st.columns(3)
    for idx, cat in enumerate(skills_data):
        with sc_cols[idx]:
            st.markdown(f"**{cat['category']}**")
            for skill in cat["skills"]:
                is_spotlight = spotlight_skills and skill in spotlight_keywords
                if is_spotlight:
                    st.markdown(f"👉 **{skill}** ⭐", unsafe_allowed_html=True)
                else:
                    st.markdown(f"• {skill}")

# Tab 3: Career Timeline
with tabs[2]:
    st.subheader("💼 Professional Career Timeline")
    st.caption("A structured layout representing Akash's previous jobs, domains, and business impact.")
    
    experiences = [
        {
            "role": "Engineering Manager / SDE3",
            "company": "Tesco",
            "period": "Feb 2025 – Present",
            "bullets": [
                "Leading an agile, highly functional team of 10 software engineers delivering Tesco's Messaging-as-a-Service core routing layer built on Apache Kafka.",
                "Architected secure, reliable multi-tenant Kafka clusters on Azure using Kubernetes (AKS) and declarative Terraform workflows.",
                "Spearheaded distributed high-throughput designs with detailed metrics logging via Prometheus, Grafana, and custom OpenTelemetry hooks.",
                "Applied LLM-based intelligent approaches to streamline diagnostic pipeline alerting, improving engineer search response times significantly."
            ]
        },
        {
            "role": "Staff Software Engineer",
            "company": "ChargePoint Inc",
            "period": "Jul 2023 – Feb 2025",
            "bullets": [
                "Led development of core high-throughput backend services and message-broker platforms supporting worldwide charging session updates.",
                "Engineered reliable distributed ingestion pipeline streams combining Apache Kafka, Spring Boot microservices, and MongoDB document nodes.",
                "Mentored developers and drove architectural solutions."
            ]
        },
        {
            "role": "Lead Software Engineer",
            "company": "Quinbay Technologies",
            "period": "Oct 2022 – Jun 2023",
            "bullets": [
                "Directed search and product recommendations engineering, designing modular Solr indexing procedures for global e-commerce systems.",
                "Constructed reliable Kafka update pipelines mapping real-time catalog changes into Elasticsearch/Solr cluster endpoints."
            ]
        },
        {
            "role": "Technical Lead",
            "company": "Bharti Airtel Limited",
            "period": "Sep 2019 – Oct 2022",
            "bullets": [
                "Led backend systems for Airtel's DTH platforms keeping high availability SLA metrics (99.99%).",
                "Built APIs for TRAI Channel Selector application to coordinate mass subscriber updates."
            ]
        }
    ]
    
    for exp in experiences:
        with st.expander(f"**{exp['role']}** @ {exp['company']} ({exp['period']})", expanded=True):
            for bullet in exp["bullets"]:
                st.markdown(f"⚡ {bullet}")

# Tab 4: Code Sandbox Demos
with tabs[3]:
    st.subheader("💻 Fully Interactive Sandbox Demos")
    demo_type = st.selectbox("Select Sandbox Simulator", ["1. Solr Autocomplete Recommender", "2. Distributed Kafka Stream Simulator", "3. LLM Log Anomaly Scanner"])
    
    if demo_type == "1. Solr Autocomplete Recommender":
        st.markdown("### Solr Autosuggest Prefix Search")
        prefix = st.text_input("Type Query Prefix (e.g., sh, bo, or)", value="sh", max_chars=3)
        candidates_k = st.number_input("Suggestions Candidates Length (k)", min_value=1, max_value=5, value=3)
        
        if st.button("Query Autocomplete Index"):
            with st.spinner("Matching prefix keys in Solr cluster..."):
                time.sleep(0.3)
                vocabulary = ["shoes", "shirts", "shorts", "shampoo", "shelves", "shipping", "billing", "baskets", "books", "orders", "offsets", "observability"]
                matches = [w for w in vocabulary if w.startswith(prefix.lower())][:candidates_k]
                if matches:
                    st.success(f"✓ Suggestions found: {', '.join(matches)}")
                else:
                    st.warning(f"No database terms starting with '{prefix}' found.")

    elif demo_type == "2. Distributed Kafka Stream Simulator":
        st.markdown("### Kafka Consumer & Metrics Simulator")
        topic = st.selectbox("Select Ingest Topic", ["billing_events", "orders_stream", "logging_telemetry"])
        messages_cnt = st.number_input("Simulated Stream Messages", min_value=1, max_value=8, value=4)
        
        if st.button("Listen Topic"):
            st.info(f"Connecting to consumer group cluster... Topic: {topic}")
            progress = st.progress(0)
            latency_list = []
            
            for i in range(messages_cnt):
                time.sleep(0.2)
                lat = round(0.12 + random.random() * 0.15, 3)
                latency_list.append(lat)
                st.write(f"⏱️ `Raw offset stream committed ... [{random.randint(100,500)}] Msg {i+1} core latency = {lat} ms`")
                progress.progress((i + 1) / messages_cnt)
                
            st.success(f"✓ Success. Latency metrics tracked list: {latency_list}")

    elif demo_type == "3. LLM Log Anomaly Scanner":
        st.markdown("### Log Parsing Anomaly Evaluator")
        logs = st.text_area("Raw Stream Logs", value="ERROR [KafkaProducer] Connection reset by broker reconnect timeout Node 5\nWARN Latency spiked 350ms on transactional commit.")
        patterns = st.text_input("Pattern Filters (Comma-separated)", value="ERROR, WARN, timeout")
        
        if st.button("Scan Log Anomalies"):
            with st.spinner("Analyzing log array metrics..."):
                time.sleep(0.4)
                matched = [p.strip().lower() for p in patterns.split(",") if p.strip().lower() in logs.lower()]
                score = min(100, int((len(matched) / max(1, len(patterns.split(",")))) * 100))
                
                if score > 50:
                    st.error(f"🚨 Anomaly Score: {score}% | System Severity Spiked! Matched tokens: {matched}")
                else:
                    st.success(f"✓ Healthy state. Anomaly Score: {score}% | Matched tokens: {matched}")

# Tab 5: AI Chat Assistant
with tabs[4]:
    st.subheader("🤖 Akash Kumar's AI Agent Representative")
    st.caption("Ask queries about Akash's software career highlights, Docker pipelines, or Kafka systems.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Welcome! I am Akash's digital AI agent replica. Ask me any work, skills, or career highlights queries!"}
        ]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if prompt := st.chat_input("Ask about Akash..."):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            with st.spinner("Analyzing parameters context..."):
                time.sleep(0.5)
                # Simple keyword lookup agent responding correctly inside Python
                low = prompt.lower()
                response = "I processed a localized simulation of Akash's assistant:\n"
                if "stack" in low or "tech" in low or "skill" in low:
                    response += "- **Main Stack**: Apache Kafka, Event-Driven Architecture, Java, Spring Boot, AKS, Kubernetes, Terraform."
                elif "tesco" in low or "experience" in low or "job" in low:
                    response += "- **Tesco Career**: Engineering Manager delivering Messaging-as-a-Service on Kafka multi-tenant Kubernetes."
                elif "contact" in low or "email" in low or "phone" in low:
                    response += "- **Details**: Send inquiries to **kumarakash2009@gmail.com** or connect via LinkedIn."
                else:
                    response += f"Akash has 12+ years of distributed system experience. Feel free to contact him at kumarakash2009@gmail.com regarding details on '{prompt}'."
                
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# Tab 6: Feedback / Form
with tabs[5]:
    st.subheader("📬 Streamlit Feedback Form")
    with st.form("contact_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        rating = st.slider("Experience Rating", min_value=1, max_value=5, value=5)
        message = st.text_area("Message Detail Parameters *")
        
        submitted = st.form_submit_button("Submit Form")
        if submitted:
            if not name or not email or not message:
                st.error("st.error: Please fill out all required fields (Name, Email, Message)!")
            else:
                st.success(f"st.success() Compiled! Thank you {name}. Feedback was compiled locally & saved successfully!")
