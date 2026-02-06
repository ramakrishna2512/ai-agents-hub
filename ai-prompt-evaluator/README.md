
# 🧠 AI Prompt Evaluator

A simple AI agent that **evaluates the quality of prompts** using a Large Language Model (via **Ollama**).  
It scores prompts on clarity, specificity, constraints, and overall effectiveness — and suggests improvements.

This project is intentionally **minimal**, easy to understand, and can be built in **~15 minutes**.

---

## ✨ Features

- 📊 Scores prompts on multiple quality dimensions  
- 🧪 Identifies issues in weak prompts  
- 🛠️ Suggests an improved version of the prompt  
- 🔌 Uses Ollama for local LLM inference  
- 📁 Clean, modular Python structure  

---

## 📂 Project Structure

```

ai-prompt-evaluator/
│
├── main.py                 # Entry point
├── prompt_evaluator.py     # Core evaluation logic
├── ollama_client.py        # Ollama model wrapper
├── evaluation_prompt.txt   # Prompt template used for evaluation
├── config/                 # Reserved for future configurations
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
   git clone https://github.com/your-username/ai-prompt-evaluator.git
   cd ai-prompt-evaluator
````

2. Make sure Ollama is running:

   ```bash
   ollama serve
   ```

3. Run the evaluator:

   ```bash
   python main.py
   ```

4. Enter the prompt you want to evaluate when prompted.

---

## 🧪 Example Output

```
Accuracy: 7/10
Clarity: 6/10
Specificity: 5/10
Constraints: 4/10
Output Quality: 6/10
Overall: 6/10

Issues:
- Prompt lacks clear constraints
- Output expectations are vague

Improvements:
- Specify target audience
- Define output format clearly

Improved Prompt:
"""
Write a clear and concise explanation of AI agents for beginners,
using simple language and real-world examples.
"""
```

---

## 🎯 Use Cases

* Prompt engineering practice
* Evaluating prompts before production use
* Learning how LLMs interpret instructions
* Demo project for AI / GenAI portfolios

---

## 🛣️ Future Improvements

* CLI arguments support
* Prompt history tracking
* Multiple evaluator agents
* Web or UI interface
* Configurable scoring weights

---

## 📜 License

This project is open-source and free to use for learning and experimentation.
