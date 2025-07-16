# 🧠 AI-Powered FAQ Agent for NuGenomics

This repository contains a tool-augmented AI agent for handling FAQ-based customer support queries at **NuGenomics**. It leverages local LLMs (e.g. LLaMA 3.2B via Ollama) with semantic search capabilities (via sentence transformers) to provide accurate, concise, and professional responses based on a curated FAQ dataset.

---

## 📌 Features

- 🔧 **Tool-Augmented LLM via Google ADK**
- 🤖 **Local LLM Inference** using [Ollama](https://ollama.com/)
- 🧠 **Semantic Search** using Sentence Transformers
- 🧩 **FAQ Matching Engine** with cosine similarity scoring
- 🛡️ **Non-Hallucinating Agent**: Always uses approved FAQ content

---

## 📂 Project Structure

.
├── app/
│ └── faq.json # FAQ database (question/answer pairs)
├── ai_agent.py # Main agent logic and tool definition
├── requirements.txt # Python dependencies
└── README.md # Project documentation