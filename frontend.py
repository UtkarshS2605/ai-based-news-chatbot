import streamlit as st
import requests

st.set_page_config(page_title="AI News Chatbot", page_icon="🤖")

st.title("🤖 Free AI News Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call backend
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"prompt": prompt}
    )

    ai_response = response.json()["response"]

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.markdown(ai_response)