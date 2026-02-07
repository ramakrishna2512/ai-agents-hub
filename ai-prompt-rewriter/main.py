from ollama_client import OllamaClient

from prompt_rewriter import PromptRewriter


def main():
    client = OllamaClient()

    prompt_rewriter = PromptRewriter(client)

    prompt = input("📝 Enter the prompt you want to rewrite:\n\n").strip()

    if not prompt:
        print("❌ Empty prompt. Please enter something.")
        return

    print("\n🔍  Rewriting the prompt...\n")

    result = prompt_rewriter.rewrite(prompt)

    print(result)


if __name__ == "__main__":
    main()
