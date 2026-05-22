/**
 * @license
 * SPDX-License-Identifier: Apache-2.5
 */

import React, { useState, useEffect } from "react";
import { Search, Github, Activity, Play, Sparkles, Filter } from "lucide-react";
import { PROJECTS } from "../data";
import { Project } from "../types";

export default function ProjectsGrid() {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<string>("All");
  const [activeDemoId, setActiveDemoId] = useState<string | null>(null);

  // ----------------------------------------------------
  // Interactive Simulation states for Akash Kumar
  // ----------------------------------------------------
  
  // Demo 1: Search Autosuggest / Solr & Kafka
  const [searchPrefix, setSearchPrefix] = useState<string>("sh");
  const [suggestionCandidates, setSuggestionCandidates] = useState<number>(3);
  const [isSuggesting, setIsSuggesting] = useState<boolean>(false);
  const [suggestedWords, setSuggestedWords] = useState<string[]>([]);

  // Demo 2: Distributed Kafka Consumer Stream
  const [selectedTopic, setSelectedTopic] = useState<string>("billing_events");
  const [consumerThreads, setConsumerThreads] = useState<number>(3);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const [streamLatencyMs, setStreamLatencyMs] = useState<number[]>([]);
  const [recentStreamLogs, setRecentStreamLogs] = useState<string[]>([]);

  // Demo 3: LLM Log Anomaly Screener
  const [targetLogs, setTargetLogs] = useState<string>(
    `ERROR 2026-05-22 14:10:00 [KafkaProducer] Connection reset by peer: broker reconnect timeout on Node 5.
INFO 2026-05-22 14:10:15 Reconnecting to broker:9092. Attempt 3 of 5.
WARN 2026-05-22 14:10:30 Distributed query latency spiked 350ms on AKS_Node_4 during transaction commit.`
  );
  const [targetPatterns, setTargetPatterns] = useState<string>(
    "ERROR, WARN, broker, Connection, latency, timeout, Peer"
  );
  const [isAnomalizing, setIsAnomalizing] = useState<boolean>(false);
  const [anomalyScore, setAnomalyScore] = useState<number | null>(null);
  const [foundMarkers, setFoundMarkers] = useState<string[]>([]);

  // Categories extraction
  const categories = ["All", "Messaging Systems", "Search & LLMs"];

  const filteredProjects = PROJECTS.filter((proj) => {
    const matchesSearch =
      proj.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      proj.summary.toLowerCase().includes(searchQuery.toLowerCase()) ||
      proj.tech.some((t) => t.toLowerCase().includes(searchQuery.toLowerCase()));

    const matchesCategory =
      selectedCategory === "All" || proj.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  // Demo 1: Simulate Solr Fuzzy Search Autocomplete Indexing
  const runAutocompleter = () => {
    setIsSuggesting(true);
    setTimeout(() => {
      const vocabulary = [
        "shoes", "shirts", "shorts", "shampoo", "shelves", "shipping",
        "billing", "baskets", "books", "beverages",
        "orders", "offsets", "operators", "observability"
      ];
      
      const filtered = vocabulary.filter(w => 
        w.startsWith(searchPrefix.toLowerCase())
      );
      
      // Limit to suggestion candidates count
      setSuggestedWords(filtered.slice(0, suggestionCandidates));
      setIsSuggesting(false);
    }, 400);
  };

  useEffect(() => {
    if (activeDemoId === "proj-1") {
      runAutocompleter();
    }
  }, [activeDemoId, searchPrefix, suggestionCandidates]);

  // Demo 2: Simulate Stream Consumption and Latency Tick
  const runStreamSimulator = () => {
    setIsStreaming(true);
    setRecentStreamLogs([]);
    setStreamLatencyMs([]);
    
    let currentLogCount = 0;
    const latencyHistory: number[] = [];
    const logPool = [
      `[Topic: ${selectedTopic}] [Partition 0] Received offset ${Math.floor(Math.random() * 50000)} - Processed safely`,
      `[Topic: ${selectedTopic}] [Partition 1] Received offset ${Math.floor(Math.random() * 50000)} - Processed safely`,
      `[Topic: ${selectedTopic}] Multi-thread pool worker committed offsite metadata transaction token`,
      `[Topic: ${selectedTopic}] Sub-millisecond data replication synchronizer complete`
    ];

    const logsList: string[] = [];
    const interval = setInterval(() => {
      const calculatedLatency = parseFloat((0.12 + Math.random() * 0.15).toFixed(3));
      latencyHistory.push(calculatedLatency);
      setStreamLatencyMs([...latencyHistory]);

      const logMessage = `[${new Date().toLocaleTimeString()}] ${logPool[currentLogCount % logPool.length]}`;
      logsList.unshift(logMessage); // Newest on top
      setRecentStreamLogs([...logsList]);

      currentLogCount++;
      if (currentLogCount >= consumerThreads) {
        clearInterval(interval);
        setIsStreaming(false);
      }
    }, 450);
  };

  // Demo 3: Natural Language Log Anomaly Screener Calculations
  const runLogScanner = () => {
    setIsAnomalizing(true);
    setAnomalyScore(null);
    setFoundMarkers([]);

    setTimeout(() => {
      const rules = targetPatterns
        .split(",")
        .map(p => p.trim().toLowerCase())
        .filter(p => p.length > 0);

      const logTextLower = targetLogs.toLowerCase();
      const detected: string[] = [];

      rules.forEach(rule => {
        if (logTextLower.includes(rule)) {
          detected.push(rule);
        }
      });

      // Calculate simple weight anomaly factor
      const calculatedFactor = Math.min(
        100,
        Math.round((detected.length / Math.max(1, rules.length)) * 100)
      );

      setFoundMarkers(detected);
      setAnomalyScore(calculatedFactor);
      setIsAnomalizing(false);
    }, 600);
  };

  return (
    <div className="space-y-6">
      {/* Red accent category title */}
      <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
        <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
          💻 Highly Scalable Production Systems & Demos
        </h2>
        <p className="font-sans text-xs text-gray-550 dark:text-gray-400 mt-0.5 animate-in fade-in">
          Fully interactive telemetry environments built to simulate high-throughput actions inside Streamlit UI.
        </p>
      </div>

      {/* Filter and Search Layout box */}
      <div className="flex flex-col md:flex-row gap-3 md:items-center justify-between p-4 rounded-lg border bg-gray-50/50 dark:bg-gray-800/10 border-gray-200 dark:border-gray-800">
        {/* Category Selection Tab Pills */}
        <div className="flex flex-wrap gap-1">
          {categories.map((cat, index) => (
            <button
              key={index}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded text-xs select-none font-sans font-medium transition duration-150 border ${
                selectedCategory === cat
                  ? "bg-streamlit-red border-streamlit-red text-white shadow-xs"
                  : "bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 text-gray-650 dark:text-gray-400 hover:text-streamlit-red"
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Real-time Search Box */}
        <div className="relative w-full md:w-72">
          <Search className="absolute left-3 top-2.5 h-3.5 w-3.5 text-gray-400" />
          <input
            type="text"
            placeholder="Search by technology node, keywords..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-1.5 border rounded-md text-xs font-sans focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-255"
          />
        </div>
      </div>

      {/* Grid Layout Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6" id="projects-grid">
        {filteredProjects.map((proj) => {
          const isDemoActive = activeDemoId === proj.id;

          return (
            <div
              key={proj.id}
              className="group flex flex-col rounded-lg border shadow-xs hover:shadow-md transition-all duration-300 bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 animate-in fade-in"
            >
              <div className="p-5 flex-1 flex flex-col justify-between space-y-4">
                <div className="space-y-2.5">
                  {/* Category Type Code Badge */}
                  <span className="inline-block px-2.5 py-1 rounded text-[10px] font-mono font-medium tracking-wide uppercase bg-red-50 dark:bg-red-950/20 text-streamlit-red border border-red-100 dark:border-red-900/30">
                    {proj.category}
                  </span>

                  <h3 className="font-display font-medium text-base text-gray-900 dark:text-white group-hover:text-streamlit-red transition select-none">
                    {proj.title}
                  </h3>

                  <p className="font-sans text-xs text-gray-550 dark:text-gray-300 leading-relaxed">
                    {proj.summary}
                  </p>

                  <div className="pt-2">
                    <h4 className="font-sans font-semibold text-[11px] text-gray-400 uppercase tracking-wider mb-1.5">
                      Key Capabilities
                    </h4>
                    <ul className="space-y-1 font-sans text-xs text-gray-650 dark:text-gray-400">
                      {proj.highlights.map((hlt, hIdx) => (
                        <li key={hIdx} className="flex items-start">
                          <span className="text-streamlit-red mr-1.5 mt-0.5">•</span>
                          <span>{hlt}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                {/* Tech tags list */}
                <div className="flex flex-wrap gap-1.5 pt-2">
                  {proj.tech.map((t, tIdx) => (
                    <span
                      key={tIdx}
                      className="px-2 py-1 rounded text-[10px] font-mono bg-gray-50 dark:bg-gray-800 border border-gray-150 dark:border-gray-850 text-gray-600 dark:text-gray-400"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              </div>

              {/* Card Footer utilities */}
              <div className="px-5 py-3 border-t flex flex-wrap items-center justify-between gap-3 bg-gray-50/50 dark:bg-gray-850/10 border-gray-150 dark:border-gray-850">
                <a
                  href={proj.githubUrl}
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center space-x-1.5 text-xs font-mono text-gray-500 hover:text-streamlit-red hover:underline transition"
                >
                  <Github className="w-3.5 h-3.5" />
                  <span>source_code.java</span>
                </a>

                {proj.hasInteractiveDemo ? (
                  <button
                    onClick={() => setActiveDemoId(isDemoActive ? null : proj.id)}
                    className={`px-3 py-1.5 rounded text-xs font-mono flex items-center space-x-1.5 select-none transition ${
                      isDemoActive
                        ? "bg-gray-200 dark:bg-gray-800 text-streamlit-red border border-transparent"
                        : "bg-streamlit-red text-white hover:bg-red-650 border border-transparent"
                    }`}
                    id={`btn-demo-${proj.id}`}
                  >
                    <Activity className="w-3.5 h-3.5" />
                    <span>{isDemoActive ? "Close st.sandbox" : "Run st.sandbox"}</span>
                  </button>
                ) : (
                  <span className="text-[10px] font-mono text-gray-400 select-none">
                    Documentation Only
                  </span>
                )}
              </div>

              {/* Interactive Demo Sandbox Wrapper */}
              {isDemoActive && (
                <div className="border-t p-5 bg-gray-50/80 dark:bg-gray-950/40 border-gray-200 dark:border-gray-800 hover:border-streamlit-red transition-all duration-300">
                  <div className="flex items-center justify-between mb-4 border-b pb-2 border-gray-200 dark:border-gray-850">
                    <span className="flex items-center space-x-1.5 font-mono text-[11px] font-semibold text-streamlit-red uppercase tracking-wider">
                      <Sparkles className="w-3.5 h-3.5 animate-pulse" />
                      <span>interactive_model_environment.py</span>
                    </span>
                    <span className="text-[10px] font-mono text-gray-400">Streamlit Sandbox Shell</span>
                  </div>

                  {/* Sandbox Case 1: Search Autosuggest / Solr & Kafka */}
                  {proj.id === "proj-1" && (
                    <div className="space-y-4 font-sans text-xs">
                      <div className="p-4 rounded-md border text-gray-800 dark:text-gray-300 bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {/* Selector 1 */}
                        <div className="space-y-1">
                          <label className="font-semibold">Type Query Prefix (e.g., sh, bo, or)</label>
                          <input
                            type="text"
                            maxLength={3}
                            value={searchPrefix}
                            onChange={(e) => setSearchPrefix(e.target.value)}
                            className="block w-full text-xs font-mono rounded mt-1 border-gray-200 dark:border-gray-850 bg-gray-50 dark:bg-gray-955 text-gray-850 dark:text-gray-250 p-2 border"
                            placeholder="Prefix"
                          />
                        </div>
                        {/* Selector 2 */}
                        <div className="space-y-1">
                          <label className="font-semibold">Suggestions Candidates Length (k)</label>
                          <input
                            type="number"
                            min="1"
                            max="5"
                            value={suggestionCandidates}
                            onChange={(e) => setSuggestionCandidates(Number(e.target.value))}
                            className="block w-full text-xs font-mono rounded mt-1 border-gray-200 dark:border-gray-850 bg-gray-50 dark:bg-gray-955 text-gray-850 dark:text-gray-250 p-2 border"
                          />
                        </div>
                      </div>

                      {/* Display suggestions output box */}
                      <div className="p-4 rounded-md border min-h-24 bg-gray-950 border-gray-850 space-y-3">
                        <div className="flex items-center justify-between col-span-2">
                          <span className="font-mono text-[10px] text-gray-400">st.dataframe() - Solr Autosuggest Index</span>
                        </div>

                        {isSuggesting ? (
                          <div className="flex items-center justify-center py-2 text-gray-500 font-mono text-[10px]">
                            <svg className="w-4 h-4 mr-2 animate-spin text-streamlit-red" fill="none" viewBox="0 0 24 24">
                              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                            </svg>
                            <span>Matching prefixes...</span>
                          </div>
                        ) : (
                          <div className="space-y-2">
                            <span className="block text-[10px] font-mono text-gray-400">
                              Matches Found for Prefix "{searchPrefix}":
                            </span>
                            {suggestedWords.length > 0 ? (
                              <div className="flex items-center flex-wrap gap-2 font-mono text-[11px]">
                                {suggestedWords.map((word, wIdx) => (
                                  <span key={wIdx} className="px-2.5 py-1 rounded bg-red-950/30 text-streamlit-red border border-red-900/40">
                                    ★ {word}
                                  </span>
                                ))}
                              </div>
                            ) : (
                              <span className="block text-gray-500 font-mono italic text-[10px]">
                                No vocabulary word starting with "{searchPrefix}" in database. Try "sh", "bo", or "or".
                              </span>
                            )}
                          </div>
                        )}
                      </div>
                    </div>
                  )}

                  {/* Sandbox Case 2: Kafka Stream Consumer & Throughput Simulator */}
                  {proj.id === "proj-2" && (
                    <div className="space-y-4 font-sans text-xs">
                      <div className="p-4 rounded-md border text-gray-800 dark:text-gray-300 bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {/* Selector 1 */}
                        <div className="space-y-1">
                          <label className="font-semibold">Select Ingest Topic</label>
                          <select
                            value={selectedTopic}
                            onChange={(e) => setSelectedTopic(e.target.value)}
                            className="block w-full text-xs font-mono rounded mt-1 border border-gray-200 dark:border-gray-850 bg-gray-50 dark:bg-gray-955 text-gray-850 dark:text-gray-250 p-2"
                          >
                            <option value="billing_events">billing_events</option>
                            <option value="orders_stream">orders_stream</option>
                            <option value="logging_telemetry">logging_telemetry</option>
                          </select>
                        </div>
                        {/* Selector 2 */}
                        <div className="space-y-1">
                          <label className="font-semibold">Simulated Stream Messages (Producers)</label>
                          <input
                            type="number"
                            min="2"
                            max="8"
                            value={consumerThreads}
                            onChange={(e) => setConsumerThreads(Number(e.target.value))}
                            className="block w-full text-xs font-mono rounded mt-1 border border-gray-200 dark:border-gray-850 bg-gray-50 dark:bg-gray-955 text-gray-850 dark:text-gray-250 p-2"
                          />
                        </div>
                      </div>

                      {/* Display training losses line graph */}
                      <div className="p-4 rounded-md border min-h-36 bg-gray-950 border-gray-850 space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="font-mono text-[10px] text-gray-400">st.line_chart() - Core Latency (ms)</span>
                          <button
                            disabled={isStreaming}
                            onClick={runStreamSimulator}
                            className="p-1 px-2.5 text-[10px] font-mono rounded bg-streamlit-red hover:bg-red-650 text-white flex items-center space-x-1 transition disabled:opacity-50"
                          >
                            <Play className="w-3 h-3" />
                            <span>{isStreaming ? "Simulating stream..." : "st.button('Listen Topic')"}</span>
                          </button>
                        </div>

                        {isStreaming && (
                          <div className="space-y-1 font-mono text-[10px] text-amber-500 animate-pulse">
                            <p>Kafka Broker connection accepted ... Streaming logs ...</p>
                          </div>
                        )}

                        {recentStreamLogs.length > 0 && (
                          <div className="space-y-3 font-mono text-[10px]">
                            <div className="p-2 border border-emerald-950/25 rounded bg-emerald-950/10 text-emerald-400 flex flex-col gap-1.5 max-h-24 overflow-y-auto">
                              {recentStreamLogs.map((log, lIdx) => (
                                <span key={lIdx} className="block animate-in fade-in duration-200">
                                  {log}
                                </span>
                              ))}
                            </div>

                            <div className="space-y-1">
                              <span className="block font-semibold text-[10px] text-gray-400">Tracked Consumption Latency (Sub-millisecond):</span>
                              <div className="flex items-center flex-wrap gap-1.5 text-[9px]">
                                {streamLatencyMs.map((val, eIdx) => (
                                  <span key={eIdx} className="px-1.5 py-0.5 rounded bg-gray-900 border border-gray-800 text-amber-500">
                                    Msg {eIdx + 1}: {val} ms
                                  </span>
                                ))}
                              </div>
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  )}

                  {/* Sandbox Case 3: LLM log anomaly screening */}
                  {proj.id === "proj-3" && (
                    <div className="space-y-4 font-sans text-xs">
                      {/* Grid comparison panel fields */}
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div className="space-y-1.5">
                          <label className="font-semibold block">Raw Production Systems Logs</label>
                          <textarea
                            value={targetLogs}
                            onChange={(e) => setTargetLogs(e.target.value)}
                            rows={3}
                            className="w-full text-xs p-2 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300 font-mono"
                          />
                        </div>
                        <div className="space-y-1.5">
                          <label className="font-semibold block">Target Anomaly Patterns (Comma-separated)</label>
                          <textarea
                            value={targetPatterns}
                            onChange={(e) => setTargetPatterns(e.target.value)}
                            rows={3}
                            className="w-full text-xs p-2 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300 font-mono"
                          />
                        </div>
                      </div>

                      {/* Display Similarity Percentage bar */}
                      <div className="p-4 rounded-md border min-h-24 bg-gray-950 border-gray-850 space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="font-mono text-[10px] text-gray-400">st.metric() - System Severity / Anomaly Index</span>
                          <button
                            disabled={isAnomalizing}
                            onClick={runLogScanner}
                            className="p-1.5 px-3 select-none text-[10px] font-mono rounded bg-streamlit-red hover:bg-red-650 text-white flex items-center space-x-1 transition disabled:opacity-50"
                          >
                            <span>Scan Log Anomalies</span>
                          </button>
                        </div>

                        {isAnomalizing && (
                          <div className="flex items-center justify-center py-2 text-gray-500 font-mono text-[10px]">
                            <svg className="w-4 h-4 mr-2 animate-spin text-streamlit-red" fill="none" viewBox="0 0 24 24">
                              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                            </svg>
                            <span>Parsing structural log arrays...</span>
                          </div>
                        )}

                        {!isAnomalizing && anomalyScore !== null && (
                          <div className="space-y-3 animate-in fade-in duration-200">
                            {/* Big severity gauge parameter */}
                            <div className="flex items-center space-x-4">
                              <div className={`font-display font-bold text-3xl ${anomalyScore > 50 ? "text-red-500" : "text-emerald-400"}`}>
                                {anomalyScore}% Anomaly Index
                              </div>
                              <div className="w-full bg-gray-800 rounded-full h-2.5 overflow-hidden">
                                <div
                                  className={`h-2.5 rounded-full transition-all duration-500 ${anomalyScore > 50 ? "bg-red-500" : "bg-emerald-500"}`}
                                  style={{ width: `${anomalyScore}%` }}
                                />
                              </div>
                            </div>

                            {/* Keywords detected inline lists */}
                            <div className="pt-2 border-t border-gray-850 flex items-center flex-wrap gap-2 text-[10px] text-gray-400">
                              <span className="font-mono font-semibold">Matched Tokens:</span>
                              {foundMarkers.length > 0 ? (
                                foundMarkers.map((tag, tIdx) => (
                                  <span key={tIdx} className={`px-1.5 py-0.5 rounded font-mono ${anomalyScore > 50 ? "bg-red-950/30 text-red-400 border border-red-900/40" : "bg-emerald-950/20 text-emerald-400 border border-emerald-900/30"}`}>
                                    {tag}
                                  </span>
                                ))
                              ) : (
                                <span className="font-mono italic text-[9px] text-gray-500">None detected</span>
                              )}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
