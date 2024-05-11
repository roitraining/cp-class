import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

project_id = "jwd-centerpoint-class"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.0-pro-002")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

prompt = "Hello."
print(get_chat_response(chat, prompt))

prompt = "What does Centerpoint Energy do?"
print(get_chat_response(chat, prompt))

prompt = "How long have they been in business?"
print(get_chat_response(chat, prompt))