/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from "react";
import {
  Github,
  Linkedin,
  Mail,
  MapPin,
  ChevronRight,
  Sparkles,
  Sliders,
  CheckSquare,
  MessageSquareOff,
} from "lucide-react";

interface SidebarProps {
  activeSection: string;
  setActiveSection: (section: string) => void;
  spotlightSkills: boolean;
  setSpotlightSkills: (value: boolean) => void;
  aiConfidence: number;
  setAiConfidence: (value: number) => void;
  sidebarCollapsed: boolean;
  setSidebarCollapsed: (value: boolean) => void;
  onClearChat?: () => void;
}

const NAV_ITEMS = [
  { id: "about", label: "👋 About Me" },
  { id: "metrics", label: "📊 KPI METRICS" },
  { id: "skills", label: "🛠️ TECHNICAL TOOLKIT" },
  { id: "experience", label: "💼 CAREER TIMELINE" },
  { id: "projects", label: "💻 DATA PROJECTS" },
  { id: "ai-bot", label: "🤖 ASK MY AI ASSISTANT" },
  { id: "feedback", label: "📬 STREAMLIT FEEDBACK" },
];

export default function Sidebar({
  activeSection,
  setActiveSection,
  spotlightSkills,
  setSpotlightSkills,
  aiConfidence,
  setAiConfidence,
  sidebarCollapsed,
  setSidebarCollapsed,
  onClearChat,
}: SidebarProps) {
  return (
    <aside
      className={`relative select-none flex-shrink-0 flex flex-col h-full border-r border-gray-200 dark:border-gray-800 bg-streamlit-sidebar dark:bg-streamlit-dark-sidebar transition-all duration-300 ${
        sidebarCollapsed ? "w-0 overflow-hidden border-r-0 md:w-16" : "w-72 md:w-80"
      }`}
    >
      {/* Collapse/Expand Toggle Button positioned on the vertical center of the sidebar border */}
      <button
        onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
        className="absolute top-1/2 -right-3 z-50 flex items-center justify-center w-6 h-6 rounded-full border shadow bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 hover:text-streamlit-red focus:outline-none transition-transform"
        style={{ transform: "translateY(-50%)" }}
        title={sidebarCollapsed ? "Expand Sidebar" : "Collapse Sidebar"}
        id="btn-sidebar-collapse"
      >
        <ChevronRight
          className={`w-3.5 h-3.5 transition-transform duration-200 ${
            sidebarCollapsed ? "" : "rotate-180"
          }`}
        />
      </button>

      {/* Main Sidebar Wrapper */}
      <div className="flex flex-col h-full overflow-y-auto px-4 py-5 space-y-6">
        {/* Profile Card Info */}
        {!sidebarCollapsed && (
          <div className="flex flex-col items-center text-center space-y-3">
            {/* Round Avatar Initial */}
            <div className="relative group">
              <div className="absolute inset-0 rounded-full blur-sm bg-gradient-to-r from-streamlit-red to-orange-400 opacity-60 group-hover:opacity-90 transition-opacity" />
              <div className="relative flex items-center justify-center w-24 h-24 rounded-full font-display font-bold text-3xl shadow-md border-3 border-streamlit-red bg-gradient-to-br from-gray-900 to-gray-800 text-white dark:from-gray-800 dark:to-gray-700">
                AK
                <span className="absolute bottom-1 right-2 block h-3 w-3 rounded-full bg-emerald-500 ring-2 ring-white dark:ring-gray-800" />
              </div>
            </div>

            <div>
              <h1 className="font-display font-bold text-xl tracking-tight text-gray-900 dark:text-white">
                Akash Kumar
              </h1>
              <p className="font-sans font-medium text-xs py-0.5 text-streamlit-red">
                Engineering Leader & Architect
              </p>
              <div className="flex items-center justify-center space-x-1.5 mt-2.5 text-xs text-gray-500 dark:text-gray-400">
                <MapPin className="w-3.5 h-3.5 text-gray-400" />
                <span className="font-mono">Bengaluru, India</span>
              </div>
            </div>

            {/* Social badges replicating streamlit st.sidebar markup buttons */}
            <div className="flex items-center justify-center gap-2.5 mt-2">
              <a
                href="https://github.com/kumarakash92"
                target="_blank"
                rel="noreferrer"
                className="p-1 px-2.5 rounded border text-xs font-mono flex items-center space-x-1 hover:border-streamlit-red hover:text-streamlit-red transition bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300"
                title="Akash Kumar's GitHub"
              >
                <Github className="w-3.5 h-3.5" />
                <span>GitHub</span>
              </a>
              <a
                href="https://www.linkedin.com/in/kumarakash92"
                target="_blank"
                rel="noreferrer"
                className="p-1 px-2.5 rounded border text-xs font-mono flex items-center space-x-1 hover:border-streamlit-red hover:text-streamlit-red transition bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300"
                title="Akash Kumar's LinkedIn"
              >
                <Linkedin className="w-3.5 h-3.5" />
                <span>LinkedIn</span>
              </a>
            </div>
          </div>
        )}

        {/* Collapsed Icon-Only Mode */}
        {sidebarCollapsed && (
          <div className="flex flex-col items-center space-y-6">
            <div className="flex items-center justify-center w-10 h-10 rounded-full font-display font-semibold text-sm bg-gray-900 text-white dark:bg-gray-800">
              AK
            </div>
            
            <div className="flex flex-col space-y-3.5">
              {NAV_ITEMS.map((item) => (
                <button
                  key={item.id}
                  onClick={() => setActiveSection(item.id)}
                  className={`p-2.5 rounded-lg text-center hover:text-streamlit-red flex items-center justify-center relative transition ${
                    activeSection === item.id
                      ? "bg-white dark:bg-gray-800 text-streamlit-red shadow-sm"
                      : "text-gray-500"
                  }`}
                  title={item.label}
                  id={`btn-collapsed-${item.id}`}
                >
                  <span className="text-lg">{item.label.split(" ")[0]}</span>
                  {activeSection === item.id && (
                    <span className="absolute left-0 top-1.5 bottom-1.5 w-1 rounded-r-md bg-streamlit-red" />
                  )}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Navigation Selector (Replicating st.sidebar.radio) */}
        {!sidebarCollapsed && (
          <div className="space-y-2">
            <p className="font-mono text-[10px] tracking-wider uppercase font-bold text-gray-400 dark:text-gray-500">
              st.sidebar.navigation
            </p>
            <nav className="flex flex-col space-y-1">
              {NAV_ITEMS.map((item) => (
                <button
                  key={item.id}
                  onClick={() => setActiveSection(item.id)}
                  className={`group relative flex items-center px-3 py-2 text-left rounded-md text-xs font-sans font-medium transition duration-150 ${
                    activeSection === item.id
                      ? "bg-white dark:bg-gray-800 text-streamlit-red shadow-sm border-l-4 border-l-streamlit-red"
                      : "text-gray-600 dark:text-gray-400 hover:bg-gray-200/50 dark:hover:bg-gray-800/30 hover:text-gray-900 dark:hover:text-white"
                  }`}
                  id={`btn-nav-${item.id}`}
                >
                  <span>{item.label}</span>
                </button>
              ))}
            </nav>
          </div>
        )}

        {/* Dynamic Python Widgets Sidebar Frame (Replicating st.sidebar.slider / st.sidebar.checkbox) */}
        {!sidebarCollapsed && (
          <div className="pt-4 border-t border-gray-200/60 dark:border-gray-800/60 space-y-5">
            <p className="flex items-center space-x-1 font-mono text-[10px] tracking-wider uppercase font-bold text-gray-400 dark:text-gray-500">
              <Sliders className="w-3.5 h-3.5 text-gray-400" />
              <span>st.sidebar.widgets</span>
            </p>

            {/* Widget 1: Dynamic Spotlighter Checkbox */}
            <div className="p-3.5 rounded-lg border border-gray-250/70 dark:border-gray-800/80 bg-white/50 dark:bg-gray-900/40 text-xs text-gray-700 dark:text-gray-300 space-y-2.5">
              <div className="flex items-center justify-between font-mono font-medium text-[11px] text-gray-400">
                <span>st.checkbox()</span>
                <span className="text-streamlit-red">active</span>
              </div>
              <label className="flex items-start space-x-2.5 cursor-pointer group select-none">
                <input
                  type="checkbox"
                  checked={spotlightSkills}
                  onChange={(e) => setSpotlightSkills(e.target.checked)}
                  className="mt-0.5 rounded border-gray-300 text-streamlit-red focus:ring-streamlit-red h-3.5 w-3.5 accent-streamlit-red"
                  id="chk-spotlight"
                />
                <span className="font-sans leading-relaxed group-hover:text-streamlit-red transition">
                  Spotlight Key Technologies (Kafka, Spring Boot, Azure AKS)
                </span>
              </label>
            </div>

            {/* Widget 2: Slider to change AI parameters dynamically */}
            <div className="p-3.5 rounded-lg border border-gray-250/70 dark:border-gray-800/80 bg-white/50 dark:bg-gray-900/40 text-xs text-gray-700 dark:text-gray-300 space-y-2.5">
              <div className="flex items-center justify-between font-mono font-medium text-[11px] text-gray-400">
                <span>st.slider()</span>
                <span className="text-streamlit-red">{aiConfidence}%</span>
              </div>
              <div className="space-y-1.5">
                <span className="block font-sans font-medium text-gray-600 dark:text-gray-300">
                  Target AI Precision Match
                </span>
                <input
                  type="range"
                  min="50"
                  max="100"
                  value={aiConfidence}
                  onChange={(e) => setAiConfidence(Number(e.target.value))}
                  className="w-full h-1.5 bg-gray-200 dark:bg-gray-700 rounded-lg appearance-none cursor-pointer accent-streamlit-red focus:outline-none"
                  id="rng-ai-precision"
                />
                <div className="flex items-center justify-between text-[10px] font-mono text-gray-400">
                  <span>50% Balanced</span>
                  <span>100% Focused</span>
                </div>
              </div>
            </div>

            {/* Widget 3: Clear Chat Cache button */}
            {activeSection === "ai-bot" && (
              <button
                onClick={onClearChat}
                className="w-full py-2 px-3 border border-dashed rounded text-xs font-mono flex items-center justify-center space-x-1.5 hover:bg-red-50 hover:text-red-600 hover:border-red-300 dark:hover:bg-red-950/20 dark:hover:text-red-400 dark:hover:border-red-900/40 transition-all border-gray-300 dark:border-gray-700 text-gray-500 dark:text-gray-400"
                id="btn-clear-chat-widget"
              >
                <MessageSquareOff className="w-3.5 h-3.5" />
                <span>Reset Chat Matrix</span>
              </button>
            )}
          </div>
        )}

        {/* Footer info at the bottom of the sidebar */}
        {!sidebarCollapsed && (
          <div className="mt-auto pt-4 border-t font-mono text-[10px] text-gray-400 dark:text-gray-500 border-gray-200 dark:border-gray-800">
            <p>System Engine: JDK 21 / Go</p>
            <p>Telemetry: OpenTelemetry / Prometheus</p>
            <p>© 2026 Akash Kumar</p>
          </div>
        )}
      </div>
    </aside>
  );
}
