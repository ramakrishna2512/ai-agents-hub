import subprocess


class OllamaClient:
    def __init__(self, model: str = "llama3"):
        self.model = model

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        full_prompt = f"""
SYSTEM:
{system_prompt}

USER:
{user_prompt}
"""

        result = subprocess.run(
            ["ollama", "run", self.model],
            input=full_prompt,
            text=True,
            capture_output=True,
            check=True
        )

        return result.stdout.strip()
