import streamlit as st

def show_intro(logo_url):
    """
    Displays the introduction section of the GenAI Chat application.
    """
    st.image(
        logo_url,
        width=300
    )
    st.title("Generative AI Playground - Chat")
    st.divider()
