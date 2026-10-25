# 🦙 Ollama Studio & AI Skill Knowledge Base

A self-contained local LLM engineering hub and automated synchronization pipeline that compiles distributed agent skills and engineering workflows into structured JSON knowledge bases, custom Modelfiles, and scheduled background daemons.

## 🚀 Key Features

* **Automated Runbook Indexing:** `sync_skills_to_ollama.py` parses markdown operational skills, extracts schemas, and formats them into a structured knowledge base (`skills_knowledge_base.json`).
* **Custom Modelfile Compiler:** Injects curated engineering system prompts, context parameters, and tool definitions into local Ollama models (`qwen2.5-coder`, `llama3`).
* **Dual Operational Interfaces:**
  - **Ollama Studio Web UI:** Lightweight dark-mode browser interface (`index.html`) served by `serve_and_launch.py`.
  - **Headless Terminal Chat:** Rapid-fire CLI chat utility (`Launch_Ollama_Terminal_Chat.bat`) for fast command-line debugging.
* **Scheduled Synchronization:** Automated Windows Task Scheduler runner (`schedule_daily_windows_task.bat`) for scheduled skill ingestion.

## 🛠️ Tech Stack
* **Python 3.12**
* **Ollama Local LLM Runtime** (Qwen 2.5 Coder / Llama 3)
* **REST APIs & Vanilla HTML5/CSS3**
* **Windows Task Scheduler & Batch Automation**

## 💻 Quick Start

### 1. Synchronize Skills into Ollama Modelfile
```powershell
python sync_skills_to_ollama.py
```

### 2. Launch Ollama Studio Web Interface
```powershell
python serve_and_launch.py
```
Or double-click `Launch_Ollama_Studio.bat`.
