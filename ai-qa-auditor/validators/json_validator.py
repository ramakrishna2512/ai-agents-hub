import json

def validate_json(output):
    try:
        parsed = json.loads(output)

        required_keys = [
            "prompt_quality_review",
            "functional_gaps",
            "security_review",
            "automated_test_cases",
            "manual_test_scenarios",
            "improved_prompt"
        ]

        for key in required_keys:
            if key not in parsed:
                return False, None

        return True, parsed

    except:
        return False, None
