🛡️ AI Hallucination Guard (MCP Multi-Agent System)

A multi-agent verification system built using Archestra AI, designed to:

Extract claims

Verify facts

Detect hallucinations

Score confidence

Built for the 2 Fast 2 MCP Hackathon.

🧰 Prerequisites (VERY IMPORTANT)

Install these before running:

1️⃣ Node.js

Install:

Node.js >= 18

Check:

node -v

2️⃣ pnpm

Install globally:

npm install -g pnpm


Check:

pnpm -v

3️⃣ Docker

Install Docker Desktop and ensure it is running.

Check:

docker ps

4️⃣ Git

Check:

git --version

📥 Clone the Repository
git clone https://github.com/yasminshaik125/ai-hallucination-guard.git
cd ai-hallucination-guard

🔐 Environment Setup (IMPORTANT)
Backend env

Create file:

archestra/.env


Add:

OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here

Frontend env

Create file:

archestra/platform/frontend/.env


Add (if needed):

NEXT_PUBLIC_API_URL=http://localhost:9000

🐘 Start Postgres (Docker)
docker start archestra-postgres


If container not present, create it (first time only).

📦 Install Dependencies

From project root:

pnpm install

▶️ Run the Platform
cd archestra/platform
pnpm dev

🌐 Open the UI

Open browser:

http://127.0.0.1:3000


If port busy, check terminal — it may switch to 3001.

✅ Expected Workflow

When working correctly:

Claim Extractor runs

Fact Verification runs

Hallucination Agent runs

Confidence score appears
