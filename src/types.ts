/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export interface Experience {
  id: string;
  role: string;
  company: string;
  location: string;
  period: string;
  description: string[];
  skills: string[];
}

export interface Project {
  id: string;
  title: string;
  category: "Machine Learning" | "NLP" | "Analytics" | "Data Visualization" | "Neural Networks" | "Search & LLMs" | "Messaging Systems";
  summary: string;
  tech: string[];
  highlights: string[];
  githubUrl: string;
  liveUrl?: string;
  hasInteractiveDemo: boolean;
}

export interface Metric {
  label: string;
  value: string;
  delta?: string;
  deltaType?: "positive" | "negative";
  emoji?: string;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  text: string;
  timestamp: Date;
}

export interface FeedbackSubmission {
  name: string;
  email: string;
  message: string;
  rating: number;
  source: string;
}
