# 🧠 AI-Powered FAQ Agent for NuGenomics

This repository contains a tool-augmented AI agent for handling FAQ-based customer support queries at **NuGenomics**. It leverages local LLMs (e.g. LLaMA 3.2B via Ollama) with semantic search capabilities (via sentence transformers) to provide accurate, concise, and professional responses based on a curated FAQ dataset.

---

## 📌 Features

- 🔧 **Tool-Augmented LLM via Google ADK**
- 🤖 **Local LLM Inference** using [Ollama](https://ollama.com/)
- 🧠 **Semantic Search** using Sentence Transformers
- 🧩 **FAQ Matching Engine** with cosine similarity scoring
- 🛡️ **Non-Hallucinating Agent**: Always uses approved FAQ content

## 🖥️ How to Run LLM Locally via Ollama

Ollama allows you to run large language models (LLMs) locally on your machine, providing faster response times, greater privacy, and no API usage limits.

### Step 1: Install Ollama

- Visit [https://ollama.com/download](https://ollama.com/download) and download the installer for your OS (macOS or Windows).
- Follow the installation instructions.

### Step 2: Pull or Run a Model

Ollama hosts various LLMs you can run locally. For example, to run the **LLaMA 3.2B** model with tool support:

```bash
ollama run llama3.2

| Model Version                | Command                      | Notes                       |
|-----------------------------|------------------------------|-----------------------------|
| **DeepSeek 1.5B (smallest)** | `ollama run deepseek-r1:1.5b` | Fastest, least resource intensive |
| **DeepSeek 8B**              | `ollama run deepseek-r1:8b`   | Balanced speed and power    |
| **DeepSeek 14B**             | `ollama run deepseek-r1:14b`  | More capable, needs more RAM|
| **DeepSeek 32B**             | `ollama run deepseek-r1:32b`  | Large model, high quality   |
| **DeepSeek 70B (largest)**   | `ollama run deepseek-r1:70b`  | Most powerful, most resource heavy |