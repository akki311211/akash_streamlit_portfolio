/**
 * @license
 * SPDX-License-Identifier: Apache-2.5
 */

import React from "react";
import { Cpu, Terminal, Sparkles, AlertCircle } from "lucide-react";
import { SKILL_CATEGORIES } from "../data";

interface SkillsManagerProps {
  spotlightActive: boolean;
}

const SPOTLIGHT_KEYWORDS = [
  "Apache Kafka",
  "Kubernetes",
  "Java",
  "Spring Boot",
  "Terraform",
  "Event-Driven Architecture",
];

export default function SkillsManager({ spotlightActive }: SkillsManagerProps) {
  return (
    <div className="space-y-6">
      <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
        <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
          🛠️ Technology Stack & Toolkit
        </h2>
        <p className="font-sans text-xs text-gray-500 dark:text-gray-400 mt-0.5">
          Segmented categories representing Akash's software and database engineering experience.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-5" id="skills-deck">
        {SKILL_CATEGORIES.map((cat, idx) => (
          <div
            key={idx}
            className="flex flex-col rounded-lg border shadow-xs bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 transition-all duration-350 overflow-hidden"
          >
            {/* Category Banner Title */}
            <div className="px-4 py-3 font-display font-semibold text-xs uppercase tracking-wider select-none bg-gray-50 dark:bg-gray-800/40 border-b border-gray-200 dark:border-gray-800 text-gray-700 dark:text-gray-300">
              {cat.title}
            </div>

            {/* Tags wrapper */}
            <div className="p-4 flex flex-wrap gap-2.5">
              {cat.skills.map((skill, sIdx) => {
                const isCore = SPOTLIGHT_KEYWORDS.includes(skill);
                const shouldSpotlight = spotlightActive && isCore;

                return (
                  <span
                    key={sIdx}
                    className={`px-3 py-1.5 rounded text-xs select-none transition-all duration-300 font-sans ${
                      shouldSpotlight
                        ? "bg-red-50 dark:bg-red-950/30 text-streamlit-red border border-red-300 dark:border-red-900/60 font-semibold shadow-xs scale-103 -translate-y-0.5"
                        : spotlightActive
                        ? "bg-gray-100/50 dark:bg-gray-800/20 text-gray-400 dark:text-gray-600 border border-gray-100 dark:border-gray-800 scale-98"
                        : "bg-gray-100 dark:bg-gray-800/80 text-gray-800 dark:text-gray-300 border border-transparent hover:border-gray-300 dark:hover:border-gray-700 hover:text-streamlit-red duration-150"
                    }`}
                  >
                    {skill}
                    {shouldSpotlight && (
                      <span className="ml-1 text-[9px] animate-pulse">⭐</span>
                    )}
                  </span>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      {/* Replicating st.info Alert dialog with specific skill advice */}
      {spotlightActive && (
        <div className="flex items-start space-x-3 p-4 rounded-lg font-sans text-xs border border-red-100 dark:border-red-950/40 bg-red-50/40 dark:bg-red-950/10 text-red-800 dark:text-red-300 animate-in fade-in slide-in-from-top-1 duration-200">
          <span className="text-base select-none mt-0.5">🌟</span>
          <div className="space-y-1 leading-relaxed">
            <h4 className="font-bold uppercase tracking-wider text-[10px] font-mono text-streamlit-red mb-0.5">
              st.sidebar.spotlight active
            </h4>
            <span>
              High-priority engineering core competencies have been highlighted in active spotlight mode. These representing the technologies Akash utilizes daily in event-driven streaming, microservices, and kubernetes platform layouts.
            </span>
          </div>
        </div>
      )}
    </div>
  );
}
