from ollama import Client
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env (if present)
load_dotenv()

# Read Ollama host from environment using sentinel detection.
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "__SET_OLLAMA_HOST_IN_ENV__")

if OLLAMA_HOST == "__SET_OLLAMA_HOST_IN_ENV__":
    print("❌ Configuration error:")
    print("OLLAMA_HOST is not set.")
    print("Please configure the Ollama host in a .env file.")
    print("Refer to the README for setup instructions.")
    sys.exit(1)

# Create Ollama client
client = Client(host=OLLAMA_HOST)

# Verified working model
MODEL = "llama3.2:latest"

SYSTEM_PROMPT = """
You are an AI task clarification agent.
Your job is to clarify goals and break tasks into steps.

Respond ONLY in this format:

Goal:
Audience:
Steps:
"""

def main():
    task = input("Enter a task to clarify: ").strip()

    if not task:
        print("Task cannot be empty.")
        sys.exit(0)

    print(f"\nUsing model: {MODEL}")
    print("----- Agent Output -----\n")

    try:
        stream = client.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": task}
            ],
            stream=True
        )

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)

        print("\n\n----- Done -----")

    except Exception as e:
        print("\n❌ Runtime error:")
        print(str(e))
        print("\nTroubleshooting:")
        print("- Ensure the Ollama application is running")
        print("- Ensure the configured model is available")
        print("- Verify environment configuration")

if __name__ == "__main__":
    main()
