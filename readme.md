# 🧠 AI-Powered FAQ Agent for NuGenomics

This repository contains a tool-augmented AI agent for handling FAQ-based customer support queries at **NuGenomics**. It leverages local LLMs (e.g. LLaMA 3.2B via Ollama) with semantic search capabilities (via sentence transformers) to provide accurate, concise, and professional responses based on a curated FAQ dataset.

---
## 📖 Table of Contents
- [Features](#-features)
- [Getting Started](#getting-started)
  - [Step 1: Clone the repository](#step-1-clone-the-repository)
  - [Step 2: Set up Python environment](#step-2-set-up-python-environment)
  - [Step 3: Install dependencies](#step-3-install-dependencies)
- [Running LLM Locally](#-how-to-run-llm-locally-via-ollama)
  - [Step 1: Install Ollama](#step-1-install-ollama)
  - [Step 2: Pull or Run a Model](#step-2-pull-or-run-a-model)
  - [Step 3: Integrate with Your AI Agent](#step-3-integrate-with-your-ai-agent)
- [FAQ Semantic Search Tool](#faq-semantic-search-tool)





## 📌 Features

- 🔧 **Tool-Augmented LLM via Google ADK**
- 🤖 **Local LLM Inference** using [Ollama](https://ollama.com/)
- 🧠 **Semantic Search** using Sentence Transformers
- 🧩 **FAQ Matching Engine** with cosine similarity scoring
- 🛡️ **Non-Hallucinating Agent**: Always uses approved FAQ content


## Getting Started

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/nugenomics-faq-agent.git
cd nugenomics-faq-agent
```
### Step 2: Set up Python environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```


## 🖥️ How to Run LLM Locally via Ollama

Ollama allows you to run large language models (LLMs) locally on your machine, providing faster response times, greater privacy, and no API usage limits.

### Step 1: Install Ollama

- Visit [https://ollama.com/download](https://ollama.com/download) and download the installer for your OS (macOS or Windows).
- Follow the installation instructions.

### Step 2: Pull or Run a Model

Ollama hosts various LLMs you can run locally. For example, to run the **LLaMA 3.2B** model with tool support:

```bash
ollama run llama3.2
```
### Step 3: Integrate with Your AI Agent
In your Python agent code, connect to the locally running model like this:


```bash
from your_agent_library import LiteLlm

# For LLaMA 3.2B model
model = LiteLlm(model="ollama_chat/llama3.2:latest")

# Or, for DeepSeek models, replace version accordingly:
model = LiteLlm(model="ollama_chat/deepseek-r1:1.5b")
```


### FAQ Semantic Search Tool
This tool uses semantic search to find the best matching answer from a list of FAQs based on a user’s question.
It works as follows:

1. Loads FAQ questions and answers from a JSON file.  
2. Converts each question and answer into a vector embedding using the all-MiniLM-L6-v2 sentence transformer model.  
3. When a user asks a question, the tool converts it into an embedding and calculates similarity scores with all FAQ questions.  
4. If a close enough match is found, the corresponding answer is returned.  
5. If no question matches well, it compares the user query to FAQ answers directly.  
6. If still no good match is found, it returns a fallback message indicating it doesn’t know the answer.

This approach ensures accurate, context-aware matching between user queries and FAQ content using vector similarity, improving answer relevance over simple keyword matching.