import streamlit as st
from services.qa_analyzer import analyze

st.set_page_config(page_title="Enterprise AI QA Auditor", layout="wide")

st.title("🏢 Enterprise AI QA Auditor")

prompt = st.text_area("Enter your feature description:", height=200)
num_tests = st.number_input("Number of automated test cases:", min_value=1, max_value=50, value=5)

if st.button("Run QA Audit"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Running enterprise QA analysis..."):
            result = analyze(prompt, num_tests)

        if result:
            st.subheader("Prompt Quality Review")
            st.write(result["prompt_quality_review"])

            st.subheader("Functional Gaps")
            st.write(result["functional_gaps"])

            st.subheader("Security Review")
            st.write(result["security_review"])

            st.subheader("Automated Test Cases")
            st.code(result["automated_test_cases"], language="python")

            st.subheader("Manual Test Scenarios")
            st.write(result["manual_test_scenarios"])

            st.subheader("Improved Prompt")
            st.write(result["improved_prompt"])

        else:
            st.error("Analysis failed after retries. Check logs.")
