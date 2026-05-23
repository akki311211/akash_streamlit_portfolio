"""
Industry / work experience.
EDIT THIS FILE to add, remove, or modify roles.
Each role is a dict; order is preserved on the page (top → bottom).
"""

INDUSTRY = [

    # ---------------- Tesco ----------------
    {
        "company": "Tesco",
        "logo": "assets/images/tesco.png",
        "role": "Engineering Leader / SDE3",
        "location": "Bengaluru, India",
        "dates": "Feb 2025 – Present",
        "type": "Full-time",

        "summary": (
            "Leading development of scalable Messaging-as-a-Service platforms "
            "and high-throughput distributed systems on Apache Kafka."
        ),

        "highlights": [
            "Leading a team of 10 engineers delivering Messaging-as-a-Service platform",
            "Architecting Kafka clusters on Azure using Kubernetes and Terraform",
            "Designed high-throughput event-driven systems with strong observability",
            "Improved debugging workflows using AI-assisted approaches",
            "Defined best practices for security, scalability, and reliability",
            "Mentored engineers and aligned roadmap with business goals",
        ],

        "tags": [
            "Apache Kafka",
            "Java",
            "Spring Boot",
            "Kubernetes",
            "Terraform",
            "Azure",
            "Distributed Systems",
            "Observability",
        ],

        "subprojects": [
            {
                "name": "Messaging-as-a-Service Platform",
                "description": (
                    "Leading development of centralized Messaging-as-a-Service platform "
                    "on Apache Kafka enabling scalable event streaming, topic governance, "
                    "ACL management, and platform automation for internal teams."
                ),

                "tags": [
                    "Kafka",
                    "Platform Engineering",
                    "Kubernetes",
                    "Terraform",
                ],
            },

            {
                "name": "AI-assisted Observability",
                "description": (
                    "Explored AI-assisted approaches for improving debugging workflows, "
                    "log summarization, and operational observability for distributed systems."
                ),

                "tags": [
                    "LLM",
                    "Observability",
                    "Semantic Search",
                    "AI-assisted Engineering",
                ],
            },
        ],
    },

    # ---------------- ChargePoint ----------------
    {
        "company": "ChargePoint Inc",
        "logo": "assets/images/chargepoint.png",
        "role": "Staff Software Engineer",
        "location": "Gurugram, India",
        "dates": "Jul 2023 – Feb 2025",
        "type": "Full-time",

        "summary": (
            "Led development of scalable backend systems and distributed platforms "
            "for EV charging infrastructure."
        ),

        "highlights": [
            "Led development of scalable backend systems and platforms",
            "Designed event-driven systems using Kafka, Spring Boot, and MongoDB",
            "Improved scalability and performance of distributed services",
            "Mentored engineers and contributed to architecture decisions",
        ],

        "tags": [
            "Java",
            "Kafka",
            "Spring Boot",
            "MongoDB",
            "Microservices",
            "Distributed Systems",
        ],

        "subprojects": [],
    },

    # ---------------- Quinbay ----------------
    {
        "company": "Quinbay Technologies",
        "logo": "assets/images/quinbay.png",
        "role": "Lead Software Engineer",
        "location": "Bengaluru, India",
        "dates": "Oct 2022 – Jun 2023",
        "type": "Full-time",

        "summary": (
            "Led development of e-commerce search and recommendation systems "
            "for high-scale retail platforms."
        ),

        "highlights": [
            "Led e-commerce search and recommendation system",
            "Built indexing pipelines using Kafka and Solr",
            "Developed autosuggestion features",
            "Enhanced search relevance beyond keyword ranking",
        ],

        "tags": [
            "Kafka",
            "Solr",
            "Search",
            "Recommendation Systems",
            "Java",
        ],

        "subprojects": [],
    },

    # ---------------- Airtel ----------------
    {
        "company": "Bharti Airtel Limited",
        "logo": "assets/images/airtel.png",
        "role": "Technical Lead",
        "location": "Gurugram, India",
        "dates": "Sep 2019 – Oct 2022",
        "type": "Full-time",

        "summary": (
            "Led backend systems and distributed platform integrations "
            "for Airtel DTH ecosystem."
        ),

        "highlights": [
            "Led backend systems for DTH platform",
            "Built APIs for TRAI Channel Selector application",
            "Designed distributed systems integrating multiple channels",
            "Ensured high availability and performance",
        ],

        "tags": [
            "Java",
            "Spring Boot",
            "Distributed Systems",
            "Microservices",
            "Kafka",
        ],

        "subprojects": [],
    },

    # ---------------- Paytm First Games ----------------
    {
        "company": "Paytm First Games",
        "logo": "assets/images/paytm.png",
        "role": "Senior Software Developer",
        "location": "Noida, India",
        "dates": "Jun 2018 – Sep 2019",
        "type": "Full-time",

        "summary": (
            "Built scalable backend systems and real-time event-driven pipelines "
            "for gaming platform infrastructure."
        ),

        "highlights": [
            "Designed geo-fencing system",
            "Built customer lifecycle systems",
            "Developed Kafka and Redis pipelines",
        ],

        "tags": [
            "Kafka",
            "Redis",
            "Java",
            "Distributed Systems",
        ],

        "subprojects": [],
    },

    # ---------------- FranConnect ----------------
    {
        "company": "FranConnect",
        "logo": "assets/images/franconnect.png",
        "role": "Senior Software Developer",
        "location": "Noida, India",
        "dates": "Jun 2014 – Feb 2018",
        "type": "Full-time",

        "summary": (
            "Worked on cloud-based CRM platform with focus on backend systems "
            "and performance optimization."
        ),

        "highlights": [
            "Worked on cloud-based CRM platform",
            "Delivered backend modules with strong performance focus",
        ],

        "tags": [
            "Java",
            "Spring",
            "MySQL",
            "Backend Engineering",
        ],

        "subprojects": [],
    },
]