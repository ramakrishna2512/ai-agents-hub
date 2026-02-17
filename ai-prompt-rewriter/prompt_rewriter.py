from ollama_client import OllamaClient


class PromptRewriter:
    def __init__(self, client: OllamaClient):
        self.client = client

    def rewrite(self, prompt_to_rewrite: str) -> str:
        final_prompt = f"""
You are a Prompt Rewriting Agent.

Your task is to improve the given prompt while preserving its original intent.

Rewrite the prompt to:
- Increase clarity
- Reduce ambiguity
- Add missing but necessary context
- Make the task easier for an AI model to understand and execute

Rules:
- Do NOT change the core intent of the prompt
- Do NOT add assumptions that are not implied
- If important context is missing, make it explicit in the rewritten prompt

Output exactly in this structure:

Rewritten Prompt:
<the improved prompt>

What Changed:
- Bullet list explaining the improvements made

Original Prompt:
{prompt_to_rewrite}
"""

        return self.client.generate(final_prompt)
