import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"


def analyze_prompt(prompt, n):
    system_prompt = """
You are a Senior QA Architect, Security Analyst, and Autonomous Test Engineer.

Your role is to function as a complete testing authority for users who do not have a QA team.
Audit the user's input and generate a comprehensive QA and testing report that ensures the system is clear, secure, testable, and production-ready.

OBJECTIVES

Perform a full audit of the user’s prompt, specification, or feature description.

1. Prompt Quality Analysis

Evaluate:

clarity and readability

ambiguity and contradictions

completeness of requirements

testability and measurable outcomes

2. Functional Gap Analysis

Identify:

missing requirements

undefined behaviors

edge cases and boundary conditions

failure scenarios and exception handling

assumptions that need validation

3. Security & Risk Review

Check for:

OWASP risks (injection, XSS, CSRF, auth flaws)

insecure data handling and storage

PII exposure risks

misuse or abuse scenarios

access control & authorization concerns

4. Automated Testing Strategy (No Code)

Design a robust automated testing approach:

key test scenarios and coverage areas

priority and risk-based testing focus

how tests ensure reliability and regression safety

where automation provides the most value

5. Manual Testing Scenarios

Provide step-by-step manual tests including:

positive flows

negative cases

boundary conditions

real-world user behavior scenarios

usability and failure recovery checks

6. Prompt Improvement

Rewrite the original prompt to be:

clear and unambiguous

complete and testable

secure by design

production-ready

RESPONSE FORMAT

Return a SINGLE valid JSON object.
Do not include markdown formatting (such as ```json).

{
"prompt_quality_review": "Detailed assessment of clarity, ambiguity, and completeness.",
"functional_gaps": "Missing requirements, undefined behaviors, assumptions, and edge cases.",
"security_review": "Security risks, OWASP concerns, and data protection issues.",
"automated_test_cases": "Text descriptions of key automated test scenarios, coverage scope, priorities, and how they ensure reliability.",
"manual_test_scenarios": "Step-by-step manual test cases covering positive, negative, boundary, and real-world scenarios.",
"improved_prompt": "A refined, professional, and testable version of the user's prompt."
}

RULES

automated_test_cases must contain descriptions only (NO code).

Do not include explanations outside the JSON.

Ensure the JSON is valid and parsable.

Be thorough and practical — the user relies on this output as their primary QA process.

Prioritize risks that could cause production failures, security breaches, or poor user experience.
"""
    final_prompt = system_prompt + "\n\nUser Prompt:\n" + prompt

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": final_prompt,
            "format": "json",
            "stream": False
        }
     )

    if response.status_code != 200:
        return f"Error: Ollama API failed with status {response.status_code}. {response.text}"

    return response.json().get("response", "Error: Unexpected response format (missing 'response' key).")


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="AI QA Auditor Agent", layout="wide")

st.title("🔎 AI QA Auditor Agent (Local + Ollama)")
st.markdown("Analyze prompts, detect missing cases, review security, and generate automated + manual tests.")

user_prompt = st.text_area(
    "Enter your feature description or prompt:",
    height=200
)

num_tests = st.number_input(
    "How many automated test cases do you want?",
    min_value=1,
    max_value=50,
    value=5
)

if st.button("Run QA Analysis"):

    if not user_prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Running full QA audit..."):
            result = analyze_prompt(user_prompt, num_tests)

        try:
            # Attempt to extract JSON if the model included extra text
            cleaned_result = result.strip()
            if "{" in cleaned_result and "}" in cleaned_result:
                start_index = cleaned_result.find("{")
                end_index = cleaned_result.rfind("}") + 1
                cleaned_result = cleaned_result[start_index:end_index]

            parsed = json.loads(cleaned_result)

            st.subheader("📋 Prompt Quality Review")
            st.write(parsed["prompt_quality_review"])

            st.subheader("⚠️ Functional Gaps")
            st.write(parsed["functional_gaps"])

            st.subheader("🔐 Security Review")
            st.write(parsed["security_review"])

            st.subheader("🧪 Automated Test Cases")
            st.write(parsed["automated_test_cases"])

            st.subheader("🖐 Manual Test Scenarios")
            st.write(parsed["manual_test_scenarios"])

            st.subheader("✨ Improved Prompt Suggestion")
            st.write(parsed["improved_prompt"])

        except:
            st.error("Model output was not valid JSON. Showing raw output below:")
            st.code(result)
