/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useRef, useEffect } from "react";
import { Send, Sparkles, MessageSquare, CornerDownLeft, RefreshCcw } from "lucide-react";
import { ChatMessage } from "../types";
import { FAQ_QUESTIONS } from "../data";

interface AIChatbotProps {
  messages: ChatMessage[];
  onSendMessage: (text: string) => void;
  isLoading: boolean;
  onClearChat?: () => void;
}

// Custom simple parser to transform markdown fragments safely to react elements
function parseBasicMarkdown(text: string) {
  if (!text) return null;
  
  const lines = text.split("\n");
  return lines.map((line, idx) => {
    let cleanLine = line;

    // Check for unordered lists e.g., "- bullet text" or "* bullet text"
    const isList = line.trim().startsWith("- ") || line.trim().startsWith("* ");
    if (isList) {
      cleanLine = line.trim().substring(2);
    }

    // Process bold segments e.g. **bold text**
    const boldRegex = /\*\*(.*?)\*\*/g;
    const parts = [];
    let lastIndex = 0;
    let match;

    while ((match = boldRegex.exec(cleanLine)) !== null) {
      const matchIndex = match.index;
      if (matchIndex > lastIndex) {
        parts.push(cleanLine.substring(lastIndex, matchIndex));
      }
      parts.push(
        <strong key={matchIndex} className="font-semibold text-gray-900 dark:text-white">
          {match[1]}
        </strong>
      );
      lastIndex = boldRegex.lastIndex;
    }
    
    if (lastIndex < cleanLine.length) {
      parts.push(cleanLine.substring(lastIndex));
    }

    if (isList) {
      return (
        <li key={idx} className="flex items-start ml-4 list-disc text-xs sm:text-sm pl-0.5 leading-relaxed">
          <span>{parts.length > 0 ? parts : cleanLine}</span>
        </li>
      );
    }

    return (
      <p key={idx} className="text-xs sm:text-sm leading-relaxed mb-2.5">
        {parts.length > 0 ? parts : cleanLine}
      </p>
    );
  });
}

export default function AIChatbot({ messages, onSendMessage, isLoading, onClearChat }: AIChatbotProps) {
  const [inputText, setInputText] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to the bottom of the conversation window
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim() || isLoading) return;
    onSendMessage(inputText.trim());
    setInputText("");
  };

  const handleSuggestionClick = (query: string) => {
    if (isLoading) return;
    onSendMessage(query);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-12rem)] min-h-[450px] rounded-lg border shadow-xs bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 overflow-hidden" id="chatbot-container">
      {/* Dynamic Header */}
      <div className="px-4 py-3 border-b flex items-center justify-between bg-gray-50 dark:bg-gray-800/20 border-gray-200 dark:border-gray-800">
        <div className="flex items-center space-x-2.5">
          <div className="flex items-center justify-center p-1.5 rounded-md bg-red-50 dark:bg-red-950/20 text-streamlit-red">
            <Sparkles className="w-4 h-4 animate-pulse" />
          </div>
          <div>
            <h3 className="font-display font-medium text-xs sm:text-sm text-gray-900 dark:text-white select-none">
              st.chat_interface() - Akash's AI Assistant
            </h3>
            <p className="font-sans text-[10px] text-gray-400 select-none">
              Powered by Google Gemini 3.5 Flash Model.
            </p>
          </div>
        </div>

        {onClearChat && (
          <button
            onClick={onClearChat}
            className="p-1 px-2.5 rounded text-[10px] font-mono flex items-center space-x-1.5 border hover:bg-red-50 hover:text-red-600 hover:border-red-250 dark:hover:bg-red-950/20 dark:hover:text-red-400 dark:hover:border-red-900/35 transition border-gray-250 dark:border-gray-800 text-gray-400"
            title="Reset active chat memory context"
            id="btn-clear-chat-top"
          >
            <RefreshCcw className="w-3 h-3" />
            <span className="hidden sm:inline">Reset Workspace</span>
          </button>
        )}
      </div>

      {/* Suggested prompting FAQ quick pins - Only show if conversation has just begun */}
      {messages.length <= 1 && (
        <div className="p-4 border-b bg-amber-50/20 dark:bg-amber-950/5 border-gray-200 dark:border-gray-805 space-y-2 select-none">
          <p className="font-mono text-[10px] uppercase font-bold text-gray-400 dark:text-gray-500">
            Suggested st.info queries:
          </p>
          <div className="flex flex-wrap gap-2">
            {FAQ_QUESTIONS.map((faq, idx) => (
              <button
                key={idx}
                onClick={() => handleSuggestionClick(faq)}
                disabled={isLoading}
                className="px-2.5 py-1 text-left rounded-md border text-xs font-sans transition-all duration-150 border-gray-200 dark:border-gray-750 bg-white dark:bg-gray-950 hover:border-streamlit-red hover:text-streamlit-red text-gray-600 dark:text-gray-400 disabled:opacity-50 disabled:pointer-events-none"
              >
                {faq}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Message Output Frame */}
      <div className="flex-1 overflow-y-auto p-4 space-y-5 bg-gray-50/10 dark:bg-gray-950/3">
        {messages.map((msg) => {
          const isUser = msg.role === "user";

          return (
            <div
              key={msg.id}
              className={`flex items-start gap-3 max-w-4xl animate-in fade-in duration-200 ${
                isUser ? "flex-row-reverse ml-auto" : "mr-auto"
              }`}
            >
              {/* Profile Avatar icons */}
              <div
                className={`flex-shrink-0 flex items-center justify-center w-8 h-8 rounded-full shadow-xs text-xs select-none ${
                  isUser
                    ? "bg-slate-600 text-white font-semibold font-mono"
                    : "bg-streamlit-red text-white"
                }`}
              >
                {isUser ? "👨" : "🤖"}
              </div>

              {/* Speech bubble shell (classic Streamlit st.chat_message style layout) */}
              <div
                className={`flex flex-col p-4 rounded-lg text-gray-855 dark:text-gray-200 ${
                  isUser
                    ? "bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 font-sans rounded-tr-none"
                    : "bg-white dark:bg-gray-900 border border-gray-250 dark:border-gray-850 shadow-xs rounded-tl-none border-l-3 border-l-streamlit-red"
                }`}
              >
                {/* Bubble message body */}
                <div className="prose prose-sm dark:prose-invert break-words">
                  {parseBasicMarkdown(msg.text)}
                </div>

                {/* Timestamp tag */}
                <span className="self-end mt-1 text-[9px] font-mono text-gray-400">
                  {msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </span>
              </div>
            </div>
          );
        })}

        {/* Dynamic Generating/Typing Cursor bubble */}
        {isLoading && (
          <div className="flex items-start gap-3 mr-auto max-w-lg">
            <div className="flex-shrink-0 flex items-center justify-center w-8 h-8 rounded-full text-xs select-none bg-streamlit-red text-white animate-pulse">
              🤖
            </div>

            <div className="flex flex-col p-4 rounded-lg bg-white dark:bg-gray-900 border border-gray-250 dark:border-gray-850 shadow-xs rounded-tl-none border-l-3 border-l-streamlit-red">
              <div className="flex items-center space-x-2 font-mono text-xs text-streamlit-red">
                <span className="cursor-blink">AI Assistant is studying parameters</span>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input Submit form */}
      <form onSubmit={handleSubmit} className="p-3 border-t bg-gray-50/50 dark:bg-gray-900 border-gray-250 dark:border-gray-850 select-none">
        <div className="relative flex items-center rounded-lg border focus-within:ring-1 focus-within:ring-streamlit-red focus-within:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800">
          <input
            type="text"
            placeholder="Ask Akash's AI (e.g., 'What is Akash's email?', 'Tell me about his Kafka cluster designs')"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            disabled={isLoading}
            className="flex-1 pl-4 pr-12 py-3 rounded-l-lg border-0 bg-transparent text-xs sm:text-sm text-gray-850 dark:text-gray-250 focus:outline-none"
            id="txt-chat-prompt"
          />

          <div className="absolute right-2 flex items-center space-x-1.5 text-gray-400">
            <span className="hidden sm:inline font-mono text-[9px] text-gray-400 uppercase tracking-widest bg-gray-50 dark:bg-gray-900 border px-1.5 py-0.5 rounded">
              Enter
            </span>
            <button
              type="submit"
              disabled={!inputText.trim() || isLoading}
              className="p-1.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800 text-streamlit-red hover:scale-105 disabled:opacity-30 disabled:scale-100 transition duration-150 focus:outline-none"
              id="btn-chat-submit"
            >
              <Send className="w-4 h-4 cursor-pointer" />
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
