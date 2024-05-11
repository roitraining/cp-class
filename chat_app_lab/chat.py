import os
import streamlit as st
import utils, gemini

# Set page config
st.set_page_config(
    page_title='ROI GenAI Playground',
)

project_id = os.environ['GOOGLE_CLOUD_PROJECT']
region = os.environ['GOOGLE_CLOUD_REGION']
logo_url = os.environ['LOGO']

utils.show_intro(logo_url)

with st.chat_message("assistant"):
    st.markdown("Hi! I'm the ROI Chatbot. How can I help you?")

if "chat_client" in st.session_state:
    chat_client = st.session_state["chat_client"]
    message_history = chat_client.history

    for msg in message_history:
        if msg.role == "model":
            msg.role = "assistant"
        st.chat_message(msg.role).markdown(
            msg.text, unsafe_allow_html=True)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        container = st.empty()
        answer = ""
        responses = gemini.get_response(
            prompt,
            project_id,
            region
        )
        for part in responses:
            answer += part.text
            container.markdown(answer, unsafe_allow_html=True)
