import streamlit as st
from workflow import run_agent

st.set_page_config(
    page_title="L&D AI Agent",
    page_icon="🤖"
)

st.title("🤖 L&D AI Agent")

st.write(
    "Ask questions about skills, learning paths, or training documents."
)

query = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if query.strip():

        with st.spinner("Thinking..."):

            response = run_agent(query)

        st.subheader("Response")
        st.write(response)

    else:
        st.warning("Please enter a question.")