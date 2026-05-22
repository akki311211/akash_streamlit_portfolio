/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from "react";
import { Download, ArrowRight } from "lucide-react";

// Types
import { ChatMessage } from "./types";

// Data
import { METRICS } from "./data";

// Components
import StreamlitHeader from "./components/StreamlitHeader";
import Sidebar from "./components/Sidebar";
import MetricsBoard from "./components/MetricsBoard";
import SkillsManager from "./components/SkillsManager";
import TimelineSection from "./components/TimelineSection";
import ProjectsGrid from "./components/ProjectsGrid";
import AIChatbot from "./components/AIChatbot";
import ContactFeedback from "./components/ContactFeedback";

export default function App() {
  const [activeSection, setActiveSection] = useState<string>("about");
  const [theme, setTheme] = useState<"light" | "dark">("light");
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(false);
  
  // Widget states (Streamlit state-binding)
  const [spotlightSkills, setSpotlightSkills] = useState<boolean>(false);
  const [aiConfidence, setAiConfidence] = useState<number>(85);

  // Core execution states
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [statusText, setStatusText] = useState<string>("Running...");

  // Chat message state
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    {
      id: "initial-msg",
      role: "assistant",
      text: "👋 Welcome to my portfolio! I am Akash's AI assistant. Ask me questions like: \n- *'What is Akash's technology stack?'* \n- *'Tell me about his experience leading teams at Tesco.'* \n- *'What systems did he build with Apache Kafka?'*",
      timestamp: new Date(),
    },
  ]);
  const [isChatLoading, setIsChatLoading] = useState<boolean>(false);

  // Initialize theme tracking
  useEffect(() => {
    const isDark = document.documentElement.classList.contains("dark");
    setTheme(isDark ? "dark" : "light");
  }, []);

  const handleToggleTheme = () => {
    const nextTheme = theme === "light" ? "dark" : "light";
    setTheme(nextTheme);
    if (nextTheme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  };

  // Safe AI Chat integration
  const handleSendChat = async (prompt: string) => {
    if (isChatLoading) return;
    
    setIsRunning(true);
    setStatusText("eval_prompt()...");
    setIsChatLoading(true);

    const userMessage: ChatMessage = {
      id: `usr-msg-${Date.now()}`,
      role: "user",
      text: prompt,
      timestamp: new Date(),
    };

    setChatMessages((prev) => [...prev, userMessage]);

    try {
      // Map history without initial greeting
      const chatHistory = chatMessages
        .filter((cm) => cm.id !== "initial-msg")
        .map((cm) => ({
          role: cm.role,
          text: cm.text,
        }));

      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: prompt,
          history: chatHistory,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        const botReply: ChatMessage = {
          id: `bot-msg-${Date.now()}`,
          role: "assistant",
          text: data.text,
          timestamp: new Date(),
        };
        setChatMessages((prev) => [...prev, botReply]);
      } else {
        throw new Error(data.error || "Server response error.");
      }
    } catch (err: any) {
      console.warn("Failed back-end chatbot link callback:", err);
      // Offline fallback matching bio parameters
      setTimeout(() => {
        const fallbacks: { [key: string]: string } = {
          tech: "Akash is an expert in **Apache Kafka, Event-Driven Architecture, Java, Spring Boot, Microservices, Kubernetes, and Terraform**. He specializes in high-throughput pipelines and Azure cloud nodes.",
          exp: "Akash has **12+ years of software experience** building scalable backend systems. He currently serves as an **Engineering Manager / SDE3 at Tesco** overseeing Messaging-as-a-Service on Kafka.",
          edu: "Akash completed his **Bachelor of Tech (B.Tech.) in Computer Science** from Lovely Professional University, Punjab in 2014.",
        };

        let responseText = `I processed a localized simulation of Akash's assistant:
- **Location**: Bengaluru, India.
- **Main Toolset**: Apache Kafka, Event-Driven Architecture, Java, Kubernetes, Go.
- **Current Position**: EM / SDE3 @ Tesco.
- **Academics**: B.Tech in Computer Science & Engineering.

To reach Akash directly, please contact him via email at **kumarakash2009@gmail.com** or connect on LinkedIn at https://www.linkedin.com/in/kumarakash92/`;

        const queryLower = prompt.toLowerCase();
        if (queryLower.includes("stack") || queryLower.includes("skill") || queryLower.includes("tech")) {
          responseText = `${fallbacks.tech}\n\nFeel free to explore the **Technical Toolkit** section for full listings!`;
        } else if (queryLower.includes("experience") || queryLower.includes("job") || queryLower.includes("work") || queryLower.includes("tesco")) {
          responseText = `${fallbacks.exp}\n\nDetailed milestones regarding team leadership and scaling are hosted under the **Career Timeline** tab!`;
        } else if (queryLower.includes("education") || queryLower.includes("college") || queryLower.includes("study") || queryLower.includes("lpu")) {
          responseText = `${fallbacks.edu}\n\nAkash graduated with a strong focus in distributed algorithm design, network protocols, and SQL optimization.`;
        }

        const botReply: ChatMessage = {
          id: `bot-msg-fallback-${Date.now()}`,
          role: "assistant",
          text: responseText,
          timestamp: new Date(),
        };
        setChatMessages((prev) => [...prev, botReply]);
      }, 500);
    } finally {
      setIsChatLoading(false);
      setIsRunning(false);
    }
  };

  const clearChatHistory = () => {
    setIsRunning(true);
    setStatusText("clear_cache()...");
    setTimeout(() => {
      setChatMessages([
        {
          id: "initial-msg",
          role: "assistant",
          text: "💬 Chat workspace cache purged. Feel free to submit fresh parameters details or hiring queries!",
          timestamp: new Date(),
        },
      ]);
      setIsRunning(false);
    }, 400);
  };

  // Safe Resume Download function
  const triggerResumeDownload = () => {
    setIsRunning(true);
    setStatusText("download_pdf()...");
    setTimeout(() => {
      const txtContent = `AKASH KUMAR - SYSTEM DESIGN & ENGINEERING LEADER RESUME
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
   - Engineered real-time geo-fencing subsystems usingRedis and Kafka.

EDUCATION:
- B.Tech in Computer Science & Engineering - Lovely Professional University (2014)`;

      const blob = new Blob([txtContent], { type: "text/plain" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "Akash_Kumar_Systems_EM_Resume.txt";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      setIsRunning(false);
    }, 500);
  };

  return (
    <div className={`flex flex-col h-screen overflow-hidden ${theme === "dark" ? "dark bg-streamlit-dark-bg text-gray-200" : "bg-white text-gray-800"}`}>
      {/* Streamlit Top Header Decorator Strip */}
      <StreamlitHeader
        isRunning={isRunning}
        statusText={statusText}
        theme={theme}
        onToggleTheme={handleToggleTheme}
      />

      {/* Full layout splits */}
      <div className="flex flex-1 overflow-hidden">
        {/* Left Sidebar emulating st.sidebar */}
        <Sidebar
          activeSection={activeSection}
          setActiveSection={setActiveSection}
          spotlightSkills={spotlightSkills}
          setSpotlightSkills={setSpotlightSkills}
          aiConfidence={aiConfidence}
          setAiConfidence={setAiConfidence}
          sidebarCollapsed={sidebarCollapsed}
          setSidebarCollapsed={setSidebarCollapsed}
          onClearChat={clearChatHistory}
        />

        {/* Main Content Pane */}
        <main className="flex-1 overflow-y-auto p-4 md:p-8 space-y-8 select-text">
          {/* Main Title Banner resembling st.title */}
          <section className="space-y-4 max-w-5xl">
            {/* Typing prompt simulation status bar */}
            <div className="flex items-center space-x-2 text-xs font-mono text-gray-400 dark:text-gray-500 font-medium">
              <span className="text-streamlit-red">import</span>
              <span>streamlit</span>
              <span className="text-streamlit-red">as</span>
              <span>st</span>
            </div>

            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="space-y-1">
                <h1 className="font-display font-medium text-3xl md:text-4xl tracking-tight text-gray-900 dark:text-white flex items-center gap-2">
                  <span>👨‍💻 Akash Kumar's Interactive Portfolio</span>
                  <span className="animate-pulse">🚀</span>
                </h1>
                <p className="font-sans font-medium text-xs sm:text-sm text-gray-555 dark:text-gray-405">
                  Engineering Leader & Distributed Systems Architect • Event-Driven Stream Architectures
                </p>
              </div>

              {/* Download Resume matching standard streamlit print/download triggers */}
              <button
                onClick={triggerResumeDownload}
                className="flex items-center justify-center space-x-2 p-2 px-4 rounded border font-mono text-xs font-semibold hover:border-streamlit-red hover:text-streamlit-red bg-white hover:bg-red-50/10 dark:bg-gray-900 border-gray-255 dark:border-gray-800 cursor-pointer shadow-xs transition duration-150"
                id="btn-resume-download"
              >
                <Download className="w-4 h-4" />
                <span>st.download_button()</span>
              </button>
            </div>
            
            <div className="h-0.5 w-full bg-gray-100 dark:bg-gray-800" />
          </section>

          {/* Section 1: About Me */}
          {activeSection === "about" && (
            <div className="space-y-6 max-w-5xl animate-in fade-in duration-200">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* Introduction column */}
                <div className="md:col-span-2 space-y-4">
                  <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
                    <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
                      👋 Professional Overview
                    </h2>
                  </div>

                  <p className="font-sans text-xs sm:text-sm leading-relaxed text-gray-650 dark:text-gray-300">
                    Hi! I am <strong>Akash Kumar</strong>. I design database transaction pipelines, event-driven messaging structures, and high-performance container architectures. Leading critical developer teams as an Engineering EM, my focus lies in crafting highly performant, resilient distributed cloud topologies.
                  </p>

                  <p className="font-sans text-xs sm:text-sm leading-relaxed text-gray-650 dark:text-gray-300">
                    With over <strong>12 years of core engineering experience</strong> working in fast-paced software enterprises, I specialize in scaling massive Apache Kafka pipelines, configuring Kubernetes workloads, and deploying clean REST frameworks.
                  </p>

                  <div className="p-4 rounded-md border text-xs leading-relaxed border-amber-100 dark:border-amber-950/40 bg-amber-50/20 dark:bg-amber-955/10 text-amber-900 dark:text-amber-400">
                    <span className="font-semibold block uppercase tracking-wider text-[10px] font-mono text-amber-600 dark:text-amber-500 mb-1">
                      📢 Featured Update
                    </span>
                    I am currently leading EM releases for Tesco's core Messaging-as-a-Service on top of Kafka. Try the interactive high-throughput throughput simulators in the <strong>"Core Projects"</strong> section!
                  </div>
                </div>

                {/* Sub-column sidebar detail cards: Brief stats info */}
                <div className="space-y-4">
                  <div className="p-4 rounded-lg border bg-gray-50/40 dark:bg-gray-900 border-gray-200 dark:border-gray-805">
                    <h3 className="font-display font-medium text-xs uppercase tracking-wider text-gray-450 dark:text-gray-500 mb-3 select-none">
                      📌 Career Quickstats
                    </h3>
                    
                    <ul className="space-y-3 pt-1 text-xs font-sans text-gray-750 dark:text-gray-300 leading-relaxed">
                      <li className="flex items-center justify-between">
                        <span>Current Role:</span>
                        <strong className="text-streamlit-red">Engineering Manager</strong>
                      </li>
                      <li className="flex items-center justify-between">
                        <span>Location:</span>
                        <strong className="font-mono">Bengaluru, India</strong>
                      </li>
                      <li className="flex items-center justify-between">
                        <span>Alma Mater:</span>
                        <strong className="text-gray-900 dark:text-white">LPU Punjab ('14)</strong>
                      </li>
                      <li className="flex items-center justify-between">
                        <span>Preferred Stack:</span>
                        <strong className="font-mono">Kafka / Java / Kubernetes</strong>
                      </li>
                    </ul>
                  </div>

                  <button
                    onClick={() => setActiveSection("ai-bot")}
                    className="w-full flex items-center justify-center space-x-2 py-3.5 px-3 rounded-lg border-2 border-dashed font-sans text-xs font-semibold text-streamlit-red hover:bg-red-50/40 dark:hover:bg-red-955/10 border-red-200 dark:border-red-900/40 hover:border-streamlit-red shadow-xs transition duration-150"
                  >
                    <span>Talk to Akash's AI assistant replica</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              {/* Display basic Metrics list */}
              <div className="pt-4 border-t dark:border-gray-805">
                <MetricsBoard metrics={METRICS} aiConfidenceValue={aiConfidence} />
              </div>
            </div>
          )}

          {/* Section 2: Metrics */}
          {activeSection === "metrics" && (
            <div className="max-w-5xl animate-in fade-in duration-200">
              <MetricsBoard metrics={METRICS} aiConfidenceValue={aiConfidence} />
            </div>
          )}

          {/* Section 3: Technical Toolkit */}
          {activeSection === "skills" && (
            <div className="max-w-5xl animate-in fade-in duration-200">
              <SkillsManager spotlightActive={spotlightSkills} />
            </div>
          )}

          {/* Section 4: Experience Timeline */}
          {activeSection === "experience" && (
            <div className="max-w-4xl animate-in fade-in duration-200">
              <TimelineSection />
            </div>
          )}

          {/* Section 5: Core Projects Grid */}
          {activeSection === "projects" && (
            <div className="max-w-5xl animate-in fade-in duration-200">
              <ProjectsGrid />
            </div>
          )}

          {/* Section 6: AI Chatbot */}
          {activeSection === "ai-bot" && (
            <div className="max-w-5xl animate-in fade-in duration-200">
              <AIChatbot
                messages={chatMessages}
                onSendMessage={handleSendChat}
                isLoading={isChatLoading}
                onClearChat={clearChatHistory}
              />
            </div>
          )}

          {/* Section 7: Feedback / Contact Form */}
          {activeSection === "feedback" && (
            <div className="max-w-3xl animate-in fade-in duration-200">
              <ContactFeedback />
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
