# 🚀 AI Hallucination Guard — Archestra Multi‑Agent System

## 📌 Project Overview

AI Hallucination Guard is a multi‑agent verification system built on **Archestra AI** that detects hallucinations in LLM responses. The system first generates a normal AI answer and then runs a verification agent that scores factual accuracy, risk level, and confidence.

This project was built for a hackathon to demonstrate:

* ✅ Multi‑agent orchestration
* ✅ Groq LLM integration
* ✅ Real‑time hallucination detection
* ✅ MCP‑style tool pipeline
* ✅ End‑to‑end local deployment

---

# 🎯 Problem Statement

Large Language Models often produce confident but incorrect answers (hallucinations). Users have no built‑in way to verify factual correctness in real time.

**Goal:** Build a system that automatically verifies AI responses and flags hallucinations with measurable scores.

---

# 💡 Solution Architecture

## 🔄 High‑Level Flow

User → Chat Assistant → LLM Answer → Hallucination Guard → Score → Final Output

### Agents Used

1. **Chat් Chat Assistant (Main Agent)**

   * Generates primary AI response
   * Routes output for verification

2. **🛡️ Hallucination Guard (Sub‑Agent)**

   * Verifies factual accuracy
   * Calculates confidence score
   * Assigns risk level
   * Flags hallucinations

---

# 🧰 Tech Stack

* Archestra AI Platform
* Groq LLM (OpenAI‑compatible endpoint)
* Node.js
* Docker & Docker Compose
* PostgreSQL
* Next.js (Archestra frontend)
* MCP architecture

---

# ⚙️ Local Setup Instructions

## ✅ Prerequisites (IMPORTANT)

Install the following on your machine:

### 1. Install Node.js

Download and install:
👉 [https://nodejs.org](https://nodejs.org)

Verify:

```bash
node -v
npm -v
```

---

### 2. Install pnpm

```bash
npm install -g pnpm
```

Verify:

```bash
pnpm -v
```

---

### 3. Install Docker Desktop

Download:
👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

After install:

* Start Docker Desktop
* Ensure it is running

Verify:

```bash
docker --version
docker compose version
```

---

### 4. Get Groq API Key

Go to:
👉 [https://console.groq.com/keys](https://console.groq.com/keys)

Copy your key (starts with `gsk_...`)

---

# 📥 Clone the Repository

Your teammate should run:

```bash
git clone https://github.com/YOUR_USERNAME/ai-hallucination-guard.git
cd ai-hallucination-guard
```

---

# 🔐 Environment Setup

## Step 1: Create .env file

Inside:

```
archestra/platform/.env
```

Add these **critical lines at the bottom**:

```env
ARCHESTRA_QUICKSTART=false

OPENAI_API_KEY=gsk_your_actual_groq_key
OPENAI_BASE_URL=https://api.groq.com/openai/v1
```

⚠️ Replace with your real Groq key.

---

# 🐳 Start Infrastructure

From project root:

```bash
docker compose up -d
```

This starts:

* PostgreSQL
* Supporting services

Wait until containers are healthy.

Check:

```bash
docker ps
```

---

# 🧠 Start Backend

```bash
cd archestra/platform/backend
pnpm install
pnpm dev
```

You should see:

```
Server listening at http://127.0.0.1:9000
```

---

# 🎨 Start Frontend

Open new terminal:

```bash
cd archestra/platform/frontend
pnpm install
pnpm dev
```

Open browser:

👉 [http://127.0.0.1:3000](http://127.0.0.1:3000)

---

# 🔑 Configure LLM Key in UI

Inside Archestra UI:

1. Go to **Settings → LLM API Keys**
2. Click **Add API Key**
3. Provider: **OpenAI**
4. Paste your Groq key
5. Save
6. Click **Refresh models**

---

# 🤖 Agent Configuration (IMPORTANT)

## Chat Assistant

Set:

* Model: Llama 3.1 8B Instant (or available Groq model)
* API Key: My Groq Key

---

## Hallucination Guard

Set:

* Model: same Groq model
* API Key: My Groq Key

---

## 🔗 Link Agents (CRITICAL)

Go to:

Agents → Chat Assistant → Edit

Under **Subagents**:

✅ Add Hallucination Guard

This enables the multi‑agent flow.

---

# 🧪 Test the System

Open chat and try:

```
The capital of India is Mumbai
```

Expected behavior:

* Chat Assistant generates answer
* Hallucination Guard verifies
* System shows:

  * Accuracy score
  * Risk level
  * Confidence

---

# 📊 Current Features

* Multi‑agent orchestration
* Groq integration
* Real‑time verification
* Confidence scoring
* Risk classification
* Local full‑stack deployment

---

# 🚧 Known Limitations

* Verification logic is prompt‑based (not retrieval grounded)
* No external fact database yet
* UI formatting can be improved
* Kubernetes MCP runtime not configured (safe to ignore locally)

---

# 🔮 Future Improvements

* Add web search grounding
* Add citation checking
* Add multi‑tool routing
* Add knowledge graph verification
* Production deployment

---

# 👩‍💻 Team Collaboration Workflow

## For My Teammate

After cloning, they must:

1. Install prerequisites
2. Add their own Groq key in `.env`
3. Run docker compose
4. Start backend
5. Start frontend
6. Configure API key in UI



**You are hackathon‑ready. 🚀**
