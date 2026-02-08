import streamlit as st
from ollama_client import OllamaClient
from prompt_rewriter import PromptRewriter

st.set_page_config(page_title="AI Prompt Rewriter", layout="centered")

st.title("✍️ AI Prompt Rewriter")

st.write("Rewrite prompts to improve clarity and reduce ambiguity.")

prompt = st.text_area("Enter a prompt to rewrite:", height=150)

if st.button("Rewrite Prompt"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        client = OllamaClient()
        rewriter = PromptRewriter(client)

        with st.spinner("Rewriting..."):
            result = rewriter.rewrite(prompt)

        st.subheader("Rewritten Output")
        st.text_area("", result, height=250)
