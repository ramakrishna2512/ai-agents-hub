from ollama_client import OllamaClient
from task_planner import TaskPlanner


def main():
    client = OllamaClient()
    planner = TaskPlanner(client)

    task = input("📝 Enter the task you want to plan:\n\n").strip()

    if not task:
        print("❌ Empty task. Please enter something.")
        return

    print("\n🧠 Planning the task...\n")
    result = planner.plan(task)

    print(result)


if __name__ == "__main__":
    main()
