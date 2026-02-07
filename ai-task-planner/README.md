# 🧠 AI Task Planner Agent

A lightweight AI agent that **converts a task into a clear execution plan**, highlighting **steps, dependencies, and risks**, using a Large Language Model via **Ollama**.

This agent focuses purely on **planning and reasoning**, not execution.  
It is intentionally **simple**, easy to understand, and designed for learning how AI agents *think*.

---

## ✨ Features

- 🧩 Breaks tasks into clear, ordered steps  
- 🔗 Identifies dependencies between steps  
- ⚠️ Highlights risky or unclear areas  
- 🧠 Focuses on reasoning, not execution  
- 🔌 Uses Ollama for local LLM inference  
- 📁 Clean, minimal Python structure  

---

## 🧠 How It Works

1. A system prompt defines the agent as a **Task Planning Agent**
2. The user provides a task as input
3. The LLM generates:
   - An execution plan
   - Dependencies between steps
   - Risky or unclear areas
4. The agent **does not execute anything** — it only plans

---

## 📂 Project Structure

```

ai-task-planner/
│
├── main.py               # Entry point
├── task_planner.py       # Task planner agent logic
├── ollama_client.py      # Ollama model wrapper
├── planner_prompt.txt    # Prompt template used for planning
├── .gitignore
└── README.md

````

---

## ⚙️ Prerequisites

- Python **3.9+**
- **Ollama** installed (model invoked via Ollama CLI)
- Any Ollama-supported model (e.g. `llama3`, `mistral`)

👉 Install Ollama: https://ollama.com/

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-task-planner.git
   cd ai-task-planner
````

2. Ensure Ollama is available:

   ```bash
   ollama serve
   ```

3. Run the task planner:

   ```bash
   python main.py
   ```

4. Enter a task when prompted.

---

## 🧪 Example

**Input Task**

```
Build a local prompt evaluation tool using Ollama.
```

**Output**

```
Execution Plan:
1. Define evaluation criteria for prompt quality
2. Design the evaluator prompt
3. Set up the Ollama client
4. Implement the evaluation flow
5. Test with sample prompts
6. Document usage

Dependencies:
- Step 4 depends on steps 2 and 3
- Step 5 depends on step 4

Risky or Unclear Areas:
- Evaluation criteria may require refinement
- Model behavior may vary across runs
```

---

## 🎯 Use Cases

* Planning AI or software projects
* Breaking vague tasks into actionable steps
* Identifying risks before execution
* Learning how LLMs reason about tasks
* Portfolio demo project for AI / GenAI roles

---

## 🧠 Design Philosophy

* One agent, one responsibility
* Prompt defines behavior, not code
* No execution or automation
* Focus on reasoning over```

🛣️ Future Improvements

Execution readiness scoring (Go / No-Go)

Task complexity estimation

Planner confidence analysis

Prompt chaining (Clarifier → Planner)

JSON structured output

CLI argument support