/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { Experience, Project, Metric } from "./types";

export const METRICS: Metric[] = [
  {
    label: "Professional Experience",
    value: "12+ Years",
    delta: "Leading 10-15 Engineers",
    deltaType: "positive",
    emoji: "⏳",
  },
  {
    label: "Kafka Clusters Served",
    value: "15+ Production",
    delta: "Messaging-as-a-Service on AKS",
    deltaType: "positive",
    emoji: "🚀",
  },
  {
    label: "Distributed Throughput",
    value: "Millions/sec",
    delta: "Sub-millisecond replications",
    deltaType: "positive",
    emoji: "💾",
  },
];

export const SKILL_CATEGORIES = [
  {
    title: "📡 Event-Streams & Messaging Platforms",
    skills: ["Apache Kafka", "Event-Driven Architecture", "Java", "Spring Boot", "Microservices", "REST APIs", "gRPC", "Leadership & Technical Strategy"],
  },
  {
    title: "🌌 Container & Cloud Infrastructure",
    skills: ["Kubernetes", "Docker Containers", "Terraform", "Microsoft Azure", "Amazon Web Services (AWS)", "Google Cloud (GCP)", "CI/CD Pipelines", "Shell Scripting"],
  },
  {
    title: "🔍 Databases, Search & AI Exposure",
    skills: ["Elasticsearch", "Apache Solr", "MySQL", "MongoDB", "Redis Pipelines", "LLM Concepts", "RAG Patterns", "Semantic Search"],
  },
];

export const EXPERIENCES: Experience[] = [
  {
    id: "exp-1",
    role: "Engineering Manager / SDE3",
    company: "Tesco",
    location: "Bengaluru, India",
    period: "Feb 2025 – Present",
    description: [
      "Leading an agile, highly functional team of 10 software engineers delivering Tesco's Messaging-as-a-Service core routing layer built on Apache Kafka.",
      "Architected secure, reliable multi-tenant Kafka clusters on Azure using Kubernetes (AKS) and declarative Terraform workflows.",
      "Spearheaded distributed high-throughput designs with detailed metrics logging via Prometheus, Grafana, and custom OpenTelemetry hooks.",
      "Applied LLM-based intelligent approaches to streamline diagnostic pipeline alerting, improving engineer search response times significantly."
    ],
    skills: ["Apache Kafka", "Kubernetes", "Azure", "Terraform", "Event-Driven Architecture", "Leadership"],
  },
  {
    id: "exp-2",
    role: "Staff Software Engineer",
    company: "ChargePoint Inc",
    location: "Gurugram, India",
    period: "Jul 2023 – Feb 2025",
    description: [
      "Led development of core high-throughput backend services and message-broker platforms supporting worldwide charging session updates.",
      "Engineered reliable distributed ingestion pipeline streams combining Apache Kafka, Spring Boot microservices, and MongoDB document nodes.",
      "Successfully tuned query execution metrics and cluster indexing targets, resulting in massive scaling efficiency boosts.",
      "Actively mentored junior developers and led code-review processes to enforce strict reliability standards across microservice pools."
    ],
    skills: ["Kafka", "Spring Boot", "MongoDB", "Event-Driven Systems", "Java", "Docker"],
  },
  {
    id: "exp-3",
    role: "Lead Software Engineer",
    company: "Quinbay Technologies",
    location: "Bengaluru, India",
    period: "Oct 2022 – Jun 2023",
    description: [
      "Directed search and product recommendations engineering, designing modular Solr indexing procedures for global e-commerce systems.",
      "Constructed reliable Kafka update pipelines mapping real-time catalog changes into Elasticsearch/Solr cluster endpoints.",
      "Built custom autocomplete suggest terms, increasing user keyword search precision and downstream click-through metrics."
    ],
    skills: ["Kafka", "Solr", "Elasticsearch", "Java", "Search Relevance", "Microservices"],
  },
  {
    id: "exp-4",
    role: "Technical Lead",
    company: "Bharti Airtel Limited",
    location: "Gurugram, India",
    period: "Sep 2019 – Oct 2022",
    description: [
      "Led backend developer modules delivering critical microservices for Airtel's massive DTH (Direct-to-Home) interactive systems.",
      "Constructed highly performant, scalable REST APIs handling channel management interactions as requested by TRAI regulations.",
      "Ensured maximum SLA uptimes exceeding 99.99% by installing robust circuit breakers, caching tiers, and cluster redundancy models."
    ],
    skills: ["Distributed Systems", "Java", "REST APIs", "High Availability", "Microservices"],
  },
  {
    id: "exp-5",
    role: "Senior Software Developer",
    company: "Paytm First Games",
    location: "Noida, India",
    period: "Jun 2018 – Sep 2019",
    description: [
      "Architected reactive microservice subsystems handling geo-fencing operations with ultra-low validation response metrics.",
      "Developed message structures and event-consumption channels using Apache Kafka and Redis to route realtime telemetry events."
    ],
    skills: ["Geo-fencing", "Redis", "Kafka", "Distributed Systems"],
  },
  {
    id: "exp-6",
    role: "Senior Software Developer",
    company: "FranConnect",
    location: "Noida, India",
    period: "Jun 2014 – Feb 2018",
    description: [
      "Built reliable backend CRM cloud micro-routines centering on high client transaction load scalability.",
      "Authored optimized database access queries, drastically reducing backend payload delivery latency."
    ],
    skills: ["Java", "Spring Boot", "Databases", "Cloud CRM"],
  },
];

export const PROJECTS: Project[] = [
  {
    id: "proj-1",
    title: "High-Throughput E-Commerce Search Suggestions",
    category: "Search & LLMs",
    summary: "An interactive autosuggestion system mapping Solr query relevance outputs using fuzzy text matching and suggestions candidate counts.",
    tech: ["Java", "Apache Solr", "Kafka", "Elasticsearch", "Spring Boot"],
    highlights: [
      "Saves custom vocabulary matrices mapped from historic inventory keyword tags.",
      "Features live customizable suggestions length (k) with dynamic distance parsing.",
      "Processes candidate matching calculations and suggests words in micro-seconds.",
    ],
    githubUrl: "https://github.com/kumarakash92/ecommerce-solr-autosuggest",
    hasInteractiveDemo: true,
  },
  {
    id: "proj-2",
    title: "Distributed Kafka Consumer Stream Simulator",
    category: "Messaging Systems",
    summary: "Simulated topic consumer demonstrating stream throughput speeds and queue processing backlogs with real-time analytics graphs.",
    tech: ["Apache Kafka", "Java", "Spring Boot", "Prometheus", "Docker"],
    highlights: [
      "Funnels real-time simulated producers into partitions to analyze cluster load limits.",
      "Allows user configuration of consumer threads (epochs) and producer stream speed.",
      "Computes dynamic partition offsets and presents consumed rates visualizers.",
    ],
    githubUrl: "https://github.com/kumarakash92/kafka-throughput-simulator",
    hasInteractiveDemo: true,
  },
  {
    id: "proj-3",
    title: "LLM Log Anomaly Screener & RAG Prototype",
    category: "Search & LLMs",
    summary: "Scans active system logs using text similarity models, highlighting errors and preparing context templates for LLM debug prompts.",
    tech: ["Kafka", "Python", "LLM Concepts", "Cosine Similarity", "RAG Patterns"],
    highlights: [
      "Tokenizes raw server logs and parses structural severity keywords.",
      "Matches telemetry logs against standard error definitions using Cosine metric calculations.",
      "Constructs beautiful debug prompt templates ready to feed standard Gemini LLM interfaces.",
    ],
    githubUrl: "https://github.com/kumarakash92/llm-log-anomaly-screener",
    hasInteractiveDemo: true,
  },
];

export const FAQ_QUESTIONS = [
  "What is Akash's technology stack?",
  "Tell me about his experience leading team sizes at Tesco.",
  "What systems did Akash build with Apache Kafka?",
  "How many years of professional experience does Akash have?",
  "What is Akash's email address and location?",
];
