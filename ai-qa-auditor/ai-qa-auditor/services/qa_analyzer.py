from services.ollama_client import call_ollama
from validators.json_validator import validate_json
from validators.test_case_validator import validate_test_cases
from config import MAX_RETRIES
from utils.logger import log_info

def analyze(prompt, n):

    system_prompt = f"""
You are a Senior QA Architect and Security Analyst.

Return STRICTLY valid JSON with these keys:

prompt_quality_review
functional_gaps
security_review
automated_test_cases
manual_test_scenarios
improved_prompt

Generate EXACTLY {n} pytest test cases.
"""

    full_prompt = system_prompt + "\n\nUser Prompt:\n" + prompt

    for _ in range(MAX_RETRIES):

        output = call_ollama(full_prompt)

        if not output:
            continue

        is_valid_json, parsed = validate_json(output)

        if not is_valid_json:
            continue

        if not validate_test_cases(parsed["automated_test_cases"], n):
            continue

        log_info("QA analysis successful")
        return parsed

    return None
