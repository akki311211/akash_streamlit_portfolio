/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from "react";
import { Briefcase, Calendar, MapPin, ChevronDown, Award } from "lucide-react";
import { EXPERIENCES } from "../data";

export default function TimelineSection() {
  // Set all experience details expanded by default, matching st.expander(expanded=True)
  const [expandedNodes, setExpandedNodes] = useState<{ [key: string]: boolean }>({
    "exp-1": true,
    "exp-2": true,
  });

  const toggleNode = (id: string) => {
    setExpandedNodes((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  return (
    <div className="space-y-6">
      <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
        <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
          💼 Professional Career Timeline
        </h2>
        <p className="font-sans text-xs text-gray-500 dark:text-gray-400 mt-0.5">
          A structured layout representing Akash's previous jobs, domains, and business impact.
        </p>
      </div>

      <div className="relative pl-6 border-l border-gray-200 dark:border-gray-800 space-y-8" id="experience-timeline">
        {EXPERIENCES.map((exp) => {
          const isOpen = expandedNodes[exp.id] ?? false;

          return (
            <div key={exp.id} className="relative group">
              {/* Chronological Vertical Dot Marker */}
              <span className="absolute -left-[31px] top-1.5 flex items-center justify-center w-4 h-4 rounded-full ring-4 ring-white dark:ring-streamlit-dark-bg bg-streamlit-red group-hover:scale-110 duration-200">
                <span className="w-1.5 h-1.5 rounded-full bg-white" />
              </span>

              {/* Expander Shell mapping st.expander() */}
              <div className="rounded-lg border shadow-xs bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 overflow-hidden transition-all duration-300">
                {/* Expander Title Header Button */}
                <button
                  onClick={() => toggleNode(exp.id)}
                  className="flex items-center justify-between w-full p-4 text-left select-none text-gray-800 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-800/20 transition duration-150 focus:outline-none"
                >
                  <div className="space-y-1">
                    <div className="flex flex-col sm:flex-row sm:items-center sm:space-x-2">
                      <span className="font-display font-medium text-sm md:text-md text-gray-900 dark:text-white">
                        {exp.role}
                      </span>
                      <span className="hidden sm:inline text-gray-400">@</span>
                      <span className="font-sans font-medium text-xs text-streamlit-red uppercase tracking-wider">
                        {exp.company}
                      </span>
                    </div>

                    <div className="flex items-center space-x-4 text-xs font-mono text-gray-500 dark:text-gray-400">
                      <span className="flex items-center space-x-1">
                        <Calendar className="w-3.5 h-3.5 text-gray-400" />
                        <span>{exp.period}</span>
                      </span>
                      <span className="flex items-center space-x-1">
                        <MapPin className="w-3.5 h-3.5 text-gray-400" />
                        <span>{exp.location}</span>
                      </span>
                    </div>
                  </div>

                  <div className="flex items-center space-x-3 text-gray-400">
                    <span className="hidden sm:inline-block font-mono text-[10px] uppercase font-semibold text-gray-400 dark:text-gray-500">
                      st.expander()
                    </span>
                    <ChevronDown
                      className={`w-4 h-4 transform transition-transform duration-200 ${
                        isOpen ? "rotate-0" : "-rotate-90"
                      }`}
                    />
                  </div>
                </button>

                {/* Expander Expanded Content Box */}
                <div
                  className={`border-t border-gray-150 dark:border-gray-800/80 transition-all duration-300 ${
                    isOpen ? "block max-h-screen p-5 opacity-100" : "hidden max-h-0 opacity-0 overflow-hidden"
                  }`}
                >
                  <div className="space-y-4">
                    {/* Bullet Achievements */}
                    <ul className="space-y-3 font-sans text-xs md:text-sm text-gray-650 dark:text-gray-300 leading-relaxed list-none pl-1">
                      {exp.description.map((bullet, bIdx) => (
                        <li key={bIdx} className="flex items-start">
                          <span className="mr-2 text-streamlit-red mt-0.5 select-none">⚡</span>
                          <span>{bullet}</span>
                        </li>
                      ))}
                    </ul>

                    {/* Skill Tags Associated */}
                    <div className="pt-2 border-t border-gray-100 dark:border-gray-800/50 flex flex-wrap gap-2">
                      {exp.skills.map((skill, sIdx) => (
                        <span
                          key={sIdx}
                          className="px-2 py-1 rounded text-[11px] font-mono bg-amber-50 dark:bg-amber-950/20 border border-amber-200/50 dark:border-amber-900/30 text-amber-700 dark:text-amber-400"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
