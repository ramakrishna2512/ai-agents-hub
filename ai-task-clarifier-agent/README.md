
# AI Task Clarifier Agent 🤖

A lightweight AI agent that converts vague ideas into clear goals, defined audiences, and actionable steps — running locally with Ollama.

---

## What It Does

- Clarifies the **goal**
- Identifies the **audience**
- Breaks tasks into **step-by-step actions**

Returns structured output every time.

---

## Tech

- Python  
- Ollama (local LLM)  
- LLaMA 3.2  

---

## Setup

1. Install Ollama → https://ollama.com  
2. Install dependency:
   ```bash
   pip install ollama
````

3. Pull model:

   ```bash
   ollama pull llama3.2:latest
   ```

---

## Run

Ensure the Ollama app is running, then:

```bash
python agent.py
```

---

## Output

```text
Goal:
Audience:
Steps:
```

---
