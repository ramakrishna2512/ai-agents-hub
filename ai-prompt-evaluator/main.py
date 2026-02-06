from prompt_evaluator import PromptEvaluator


def main():
    evaluator = PromptEvaluator()

    prompt = input("📝 Enter the prompt you want to evaluate:\n\n").strip()

    if not prompt:
        print("❌ Empty prompt. Please enter something.")
        return

    print("\n🔍 Evaluating prompt...\n")

    result = evaluator.evaluate(prompt)

    print(result)


if __name__ == "__main__":
    main()
