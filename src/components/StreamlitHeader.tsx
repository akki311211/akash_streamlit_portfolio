/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from "react";
import { Play, Settings, ExternalLink, HelpCircle, Heart, Moon, Sun, Monitor } from "lucide-react";

interface StreamlitHeaderProps {
  isRunning: boolean;
  theme: "light" | "dark";
  onToggleTheme: () => void;
  statusText?: string;
}

export default function StreamlitHeader({
  isRunning,
  theme,
  onToggleTheme,
  statusText = "Running...",
}: StreamlitHeaderProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [systemTime, setSystemTime] = useState("");

  useEffect(() => {
    // Standard real-time timestamp like in Streamlit analytics logs
    const updateTime = () => {
      const now = new Date();
      setSystemTime(now.toUTCString().replace("GMT", "UTC"));
    };
    updateTime();
    const timer = setInterval(updateTime, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="relative sticky top-0 z-40 flex items-center justify-between w-full h-12 px-4 shadow-sm border-b backdrop-blur-md bg-opacity-95 select-none transition-colors duration-200 border-gray-200 dark:border-gray-800 bg-white dark:bg-streamlit-dark-bg text-gray-700 dark:text-gray-300">
      {/* Streamlit Top Decorator Strip (Iconic Red-to-Orange Line) */}
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-streamlit-red via-[#ff7c7c] to-[#ffaa7c]" />

      {/* Left side: App Details and Port Indicator */}
      <div className="flex items-center space-x-3 text-xs font-mono">
        <span className="flex items-center space-x-1 px-1.5 py-0.5 rounded text-gray-500  bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
          <span>Localhost:3000</span>
        </span>
        <span className="hidden sm:inline-block text-gray-400">|</span>
        <span className="hidden sm:inline-block text-gray-500">{systemTime}</span>
      </div>

      {/* Right side: Running Server Spinner, Theme Switcher, and st.menu dropdown */}
      <div className="flex items-center space-x-4">
        {/* Streamlit-style execution spinner */}
        <div className="flex items-center space-x-1.5">
          {isRunning ? (
            <div className="flex items-center space-x-1.5 text-xs text-streamlit-red">
              <svg
                className="w-4 h-4 animate-spin text-streamlit-red"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                />
              </svg>
              <span className="text-[11px] font-mono tracking-wider font-semibold uppercase animate-pulse">
                {statusText}
              </span>
            </div>
          ) : (
            <div className="flex items-center space-x-1 text-[11px] font-mono font-medium text-emerald-600 dark:text-emerald-500">
              <span className="w-2 h-2 rounded-full bg-emerald-600 dark:bg-emerald-500" />
              <span className="uppercase tracking-wider">Ready</span>
            </div>
          )}
        </div>

        {/* Quick Theme Toggle */}
        <button
          onClick={onToggleTheme}
          className="p-1 px-1.5 rounded text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-streamlit-red transition-all"
          title={`Switch to ${theme === "light" ? "Dark" : "Light"} Theme`}
          id="btn-quick-theme"
        >
          {theme === "light" ? (
            <Moon className="w-4 h-4 cursor-pointer" />
          ) : (
            <Sun className="w-4 h-4 cursor-pointer" />
          )}
        </button>

        {/* Icon 3-dots Streamlit Core Menu */}
        <div className="relative">
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="p-1 rounded text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-streamlit-red transition-all"
            title="Streamlit Main Menu"
            id="btn-streamlit-menu"
          >
            <Settings className="w-4 h-4 cursor-pointer" />
          </button>

          {isMenuOpen && (
            <>
              {/* Overlay back-drop to close */}
              <div
                className="fixed inset-0 z-30"
                onClick={() => setIsMenuOpen(false)}
              />

              {/* Menu items */}
              <div className="absolute right-0 mt-2 w-56 rounded-md shadow-lg border text-sm font-sans z-40 animate-in fade-in slide-in-from-top-2 duration-100 bg-white dark:bg-streamlit-dark-sidebar border-gray-200 dark:border-gray-700 text-gray-800 dark:text-gray-200">
                <div className="py-1.5 px-3 border-b text-xs font-semibold text-gray-400 dark:border-gray-700">
                  STREAMLIT UTILITIES
                </div>
                <div className="py-1">
                  <button
                    onClick={() => {
                      onToggleTheme();
                      setIsMenuOpen(false);
                    }}
                    className="flex items-center justify-between w-full px-4 py-2 text-left hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 transition-colors"
                  >
                    <span className="flex items-center space-x-2">
                      {theme === "light" ? (
                        <>
                          <Moon className="w-4 h-4 text-gray-400" />
                          <span>Use Dark Theme</span>
                        </>
                      ) : (
                        <>
                          <Sun className="w-4 h-4 text-gray-400" />
                          <span>Use Light Theme</span>
                        </>
                      )}
                    </span>
                  </button>

                  <a
                    href="https://github.com/kumarakash92"
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center justify-between px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 transition-colors"
                  >
                    <span className="flex items-center space-x-2">
                      <ExternalLink className="w-4 h-4 text-gray-400" />
                      <span>Akash's GitHub</span>
                    </span>
                  </a>

                  <a
                    href="https://streamlit.io"
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center justify-between px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 transition-colors border-t dark:border-gray-700"
                  >
                    <span className="flex items-center space-x-2">
                      <HelpCircle className="w-4 h-4 text-gray-400" />
                      <span>Streamlit Docs</span>
                    </span>
                  </a>
                </div>
                <div className="p-2 border-t text-[10px] text-center text-gray-400 font-mono bg-gray-55 dark:bg-gray-900 border-gray-200 dark:border-gray-700">
                  Made with <Heart className="inline w-3 h-3 text-streamlit-red fill-current" /> by Akash & Assistant
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
