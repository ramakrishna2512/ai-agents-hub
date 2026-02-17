from ollama_client import OllamaClient


class TaskPlanner:
    def __init__(self, client: OllamaClient):
        self.client = client

        with open("planner_prompt.txt", "r") as f:
            self.system_prompt = f.read()

    def plan(self, task: str) -> str:
        return self.client.generate(
            system_prompt=self.system_prompt,
            user_prompt=task
        )
