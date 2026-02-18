import requests
from config import OLLAMA_URL, MODEL_NAME, TEMPERATURE
from utils.logger import log_error

def call_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": TEMPERATURE
                }
            }
        )

        data = response.json()

        if "response" in data:
            return data["response"]
        else:
            log_error(f"Unexpected response: {data}")
            return None

    except Exception as e:
        log_error(str(e))
        return None
