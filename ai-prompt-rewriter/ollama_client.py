import subprocess
from config.ollamaconfig import MODEL_NAME




class OllamaClient:
    def __init__(self):
        self.model = MODEL_NAME

    def generate(self, prompt: str) -> str:
        process = subprocess.Popen(
            ["ollama", "run", self.model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",   # 🔥 FIX 1: force UTF-8
            errors="replace"    # 🔥 FIX 2: never crash on weird chars
        )

        stdout, stderr = process.communicate(prompt)

        if process.returncode != 0:
            raise RuntimeError(f"Ollama error:\n{stderr}")

        return stdout.strip()
