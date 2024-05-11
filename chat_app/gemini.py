import streamlit as st

import vertexai
import vertexai.preview.generative_models as generative_models
from vertexai.generative_models import GenerativeModel

def get_response(prompt, project_id, region):

    vertexai.init(project=project_id, location=region)

    system_instruction = """
        You are an Generative AI Chatbot. You provide responses
        that are clear, professional, detailed, and accurate. When asked
        questions, you provide the answer first and then provide additional
        information or context. When specifically prompted to do step-by-step
        reasoning, you do so (as opposed to keeping explanation until the end).
        Your responses should be kept to fewer than 2000 tokens.
    """

    generation_config = {
        "max_output_tokens": 2048,
        "temperature": 0.5,
        "top_p": 1,
        "candidate_count": 1,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    if not "chat_client" in st.session_state:
        model = GenerativeModel(
            "gemini-1.0-pro-002",
            system_instruction=[system_instruction]
        )
        chat_client = model.start_chat()
    else:
        chat_client = st.session_state["chat_client"]

    responses = chat_client.send_message(
        [prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True
    )

    st.session_state["chat_client"] = chat_client
    return responses
