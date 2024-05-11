import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.generative_models as generative_models

project_id = "jwd-centerpoint-class"
region = "us-central1"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.0-pro-002")
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

prompt = "What does Centerpoint Energy do?"
response = model.generate_content(
    prompt,
    safety_settings=safety_settings,
)
print(response.text)
