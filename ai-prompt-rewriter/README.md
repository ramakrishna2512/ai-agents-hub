
# ✍️ AI Prompt Rewriter

A lightweight AI agent that **rewrites and improves prompts** while preserving their original intent, using a Large Language Model via **Ollama**.

It enhances prompts by improving **clarity, specificity, structure, and completeness**, making them more effective for LLMs.

This project is intentionally **simple**, easy to understand, and can be built in **~15 minutes**.

---

## ✨ Features

- ✨ Rewrites prompts without changing original intent  
- 🧠 Improves clarity and reduces ambiguity  
- 🎯 Adds missing but necessary context  
- 🛠️ Produces cleaner, more effective prompts for LLMs  
- 🔌 Uses Ollama for local LLM inference  
- 📁 Clean, minimal Python structure  

---

## 📂 Project Structure

```

ai-prompt-rewriter/
│
├── main.py                 # Entry point
├── prompt_rewriter.py      # Core rewriting logic
├── ollama_client.py        # Ollama model wrapper
├── rewriter_prompt.txt     # Prompt template used for rewriting
├── .gitignore
└── README.md

````

---

## ⚙️ Prerequisites

- Python **3.9+**
- **Ollama** installed and running locally  
- Any Ollama-supported model (example: `llama3`, `mistral`, etc.)

👉 Install Ollama: https://ollama.com/

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-prompt-rewriter.git
   cd ai-prompt-rewriter
````

2. Make sure Ollama is running:

   ```bash
   ollama serve
   ```

3. Run the prompt rewriter:

   ```bash
   python main.py
   ```

4. Enter the prompt you want to rewrite when prompted.

---

## 🧪 Example Output

**Input Prompt**

```
ai agents
```

**Rewritten Prompt**

```
Explain what AI agents are, including their purpose, key components,
and real-world examples, in a clear and beginner-friendly manner.
```

---

## 🎯 Use Cases

* Prompt engineering improvement
* Preparing prompts for production LLM usage
* Cleaning vague or underspecified prompts
* Learning how prompt structure affects LLM output
* Portfolio demo project for AI / GenAI roles

---

## 🛣️ Future Improvements

* Multiple rewriting styles (concise, detailed, creative)
* Prompt comparison (before vs after scoring)
* CLI arguments support
* Prompt history tracking
* Web or UI interface
* Configurable rewriting rules

---

