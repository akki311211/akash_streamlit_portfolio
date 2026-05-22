import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(express.json());

const PORT = 3000;

// Initialize Gemini Client safely using the modern SDK
let ai: GoogleGenAI | null = null;
try {
  const apiKey = process.env.GEMINI_API_KEY;
  if (apiKey) {
    ai = new GoogleGenAI({
      apiKey,
      httpOptions: {
        headers: {
          "User-Agent": "aistudio-build",
        },
      },
    });
  } else {
    console.warn("GEMINI_API_KEY environment variable is not defined. AI Chat features will be disabled.");
  }
} catch (error) {
  console.error("Failed to initialize GoogleGenAI client:", error);
}

// Akash's Detailed Biography & Prompt Context
const AKASH_BIOS_PROMPT = `
You are the personal AI Assistant of Akash Kumar, a highly skilled Engineering Leader and Software Architect with 12+ years of experience.
Your goal is to answer questions from visitors of Akash's portfolio website in a friendly, conversational, and helpful tone, just like Akash's own digital representative.

Here are the facts about Akash Kumar that you must use to answer questions:

About Akash:
- An Engineering Leader with 12+ years of experience building and scaling high-throughput distributed systems.
- He has deep expertise in Apache Kafka, event-driven architectures, and cloud-native platforms.
- Growing experience under AI/LLM paradigms applying semantic search, embeddings, prompt designs, and RAG architectures in logging / message broker flows.
- Proven track record of leading software engineering teams (10-15 engineers), driving technical scale strategy, and delivering robust systems.
- Based in: India (Bengaluru / Delhi NCR).
- Email: kumarakash2009@gmail.com
- LinkedIn: linkedin.com/in/kumarakash92

Work Experience:
1. Tesco @ Bengaluru (Feb 2025 - Present) - Engineering Manager / SDE3
   - Leading an agile team of 10 engineers delivering Tesco's Messaging-as-a-Service platform on Apache Kafka.
   - Architecting Kafka clusters on Microsoft Azure using Kubernetes and Terraform.
   - Designing high-throughput event-driven systems with robust observability.
   - Improved debugging workflows using AI-assisted approaches and LLM patterns for log screening.
2. ChargePoint Inc @ Gurugram (Jul 2023 - Feb 2025) - Staff Software Engineer
   - Led development of scalable backend systems and transaction routing platforms.
   - Designed event-driven systems using Kafka, Spring Boot, and MongoDB.
   - Mentored developers and drove architectural solutions.
3. Quinbay Technologies @ Bengaluru (Oct 2022 - Jun 2023) - Lead Software Engineer
   - Led e-commerce search & recommendation platform backend.
   - Constructed inventory search indexing pipelines using Kafka and Apache Solr.
   - Authored autosuggestion features and optimized relevance rankings beyond keyword scoring.
4. Bharti Airtel Limited @ Gurugram (Sep 2019 - Oct 2022) - Technical Lead
   - Led backend systems for Airtels DTH entertainment streaming platform.
   - Designed distributed systems integrating multiple channels while maintaining 99.99% availability.
   - Built TRAI Channel Selector application APIs to process massive customer query traffic.
5. Paytm First Games @ Noida (Jun 2018 - Sep 2019) - Senior Software Developer
   - Designed a geo-fencing platform system boundary detector.
   - Built real-time customer lifecycle event collectors with Redis and Kafka topics.
6. FranConnect @ Noida (Jun 2014 - Feb 2018) - Senior Software Developer
   - Worked on scalable cloud-based CRM systems delivering performant modular code.

Education:
- Bachelor of Technology (B.Tech.) in Computer Science & Engineering — Lovely Professional University, Punjab (Graduated 2014)

Core Tech Stack:
- Event-Streams & Messaging: Apache Kafka, Event-Driven Architecture, REST APIs, Microservices, gRPC
- Cloud & Infrastructure: Kubernetes, Docker, Terraform, Microsoft Azure, AWS, GCP, CI/CD, Shell Scripting
- Databases & Search: MySQL, MongoDB, Redis, Elasticsearch, Apache Solr, PostgreSQL, Cassandra
- Observability: Prometheus, Grafana, OpenTelemetry, ELK Stack
- AI Concepts: LLM concepts, RAG pipelines, Semantic Search, embeddings, Prompt engineering

Key Portfolio Projects:
1. High-Throughput Search Suggestion Optimizer: Auto-suggest application leveraging Kafka and Solr metrics, simulating index candidates retrieval dynamically based on fuzzy matching.
2. Distributed Kafka Stream Consumer Simulator: Stream scheduler allowing users to configure input speed rates and consumer threads to map live topic offset delivery rates.
3. LLM Log Anomaly Screener: Text parser checking server exceptions and log files, outputting RAG prompt instructions ready for Gemini evaluation.

Personal Traits and Hobbies:
- Passionate about system optimization, clean code reviews, and high SLA availability metrics.
- Enjoys lecturing on system design, hiking, and studying LLM efficiency configurations.

Guidelines for your responses:
- Speak as Akash's representative, e.g., "Akash is currently managing a team at Tesco..." or "Akash has 12+ years of software design experience...".
- Be professional, humble, tech-focused, and highly organized in your replies.
- Keep answers concise, clear, and highly structured (use lists or bold terms where appropriate).
- Do not mention or fabricate details that are not in the facts above. If a question is asked about something outside this scope, answer gracefully: "I don't have that information on hand, but feel free to reach out to Akash directly via his email at kumarakash2009@gmail.com or on LinkedIn!"
- You may use a friendly emoji here and there, mimicking Streamlit's charming style.
`;

// API routes FIRST
app.post("/api/chat", async (req, res) => {
  try {
    const { message, history } = req.body;

    if (!message) {
      return res.status(400).json({ error: "Message is required." });
    }

    if (!ai) {
      return res.status(503).json({
        text: "My apologies, but Rohit's AI assistant is currently offline because the AI Service credentials are not configured. You can still browse Rohit's experience, skills, and projects listed on the website!",
      });
    }

    // Format chat contents
    const contents: any[] = [];
    
    // Add history if any
    if (history && Array.isArray(history)) {
      history.forEach((msg: any) => {
        contents.push({
          role: msg.role === "user" ? "user" : "model",
          parts: [{ text: msg.text }],
        });
      });
    }

    // Append current user prompt
    contents.push({
      role: "user",
      parts: [{ text: message }],
    });

    // Generate content using gemini-3.5-flash
    const response = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents,
      config: {
        systemInstruction: AKASH_BIOS_PROMPT,
        temperature: 0.7,
      },
    });

    const reply = response.text || "I was unable to formulate a response. Please tray again!";
    res.json({ text: reply });
  } catch (error: any) {
    console.error("AI Assistant API Error:", error);
    res.status(500).json({
      error: "An error occurred while contacting the AI Assistant.",
      details: error.message,
    });
  }
});

// Feedback / Contact Form API endpoint
app.post("/api/feedback", (req, res) => {
  const { name, email, message, rating, source } = req.body;
  
  if (!name || !email || !message) {
    return res.status(400).json({ error: "Please map all required variables." });
  }

  console.log(`[Form Submission] Name: ${name}, Email: ${email}, Message: ${message}, Rating: ${rating || 'None'}, Found via: ${source || 'None'}`);
  
  return res.json({
    success: true,
    message: "Thank you for getting in touch! Rohit will receive your message and respond shortly.",
  });
});

// Serve frontend assets using Vite middleware or static files
async function startApp() {
  if (process.env.NODE_ENV !== "production") {
    const { createServer: createViteServer } = await import("vite");
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), "dist");
    app.use(express.static(distPath));
    app.get("*", (req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Express dev server running on http://localhost:${PORT}`);
  });
}

startApp().catch((err) => {
  console.error("Failed to start the Express-Vite backend app server:", err);
});
