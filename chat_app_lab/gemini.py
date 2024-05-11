import streamlit as st

# import vertexai
# import GenerativeModel
# import generative_models

def get_response(prompt, project_id, region):

    # initialize Vertex AI

    # define a system message
    # this provides context and instructions to the model
    system_instruction = """
    """

    # define the generation config dict
    generation_config = {
    }

    # define the safety settings dict
    # set everything to block only high confidence
    safety_settings = {
    }

    if not "chat_client" in st.session_state:
        # create a generativemodel object using the GEMINI-1.0-pro-002 model
        # and the system instruction
        model = # YOUR CODE HERE

        # start a chat session
        chat_client = # YOUR CODE HERE
    else:
        chat_client = st.session_state["chat_client"]

    # send a message using the chat client
    # enable streaming
    responses = chat_client # YOUR CODE HERE

    st.session_state["chat_client"] = chat_client
    return responses
