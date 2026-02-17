from ollama_client import OllamaClient


class PromptEvaluator:
    def __init__(self):
        self.client = OllamaClient()

    def evaluate(self, prompt_to_evaluate: str) -> str:
        evaluation_prompt = f"""
You are a strict Prompt Engineering evaluator.

Evaluate the following prompt.

Give scores from 1 to 10 for:
1. Clarity
2. Specificity
3. Constraints
4. Expected output quality

Then provide:
- Overall score
- What is missing
- How to improve it
- A rewritten improved version of the prompt

Do NOT answer the prompt itself.

PROMPT TO EVALUATE:
\"\"\"{prompt_to_evaluate}\"\"\"

Respond in this exact format:

accuracy scores: x/10
Clarity: X/10
Specificity: X/10
Constraints: X/10
Output Quality: X/10
Overall: X/10

Issues:
- ...

Improvements:
- ...

Improved Prompt:
\"\"\"...\"\"\"
"""
        return self.client.generate(evaluation_prompt)
