import vertexai
from vertexai.generative_models import GenerativeModel

project_id = "jwd-centerpoint-class"
region = "us-central1"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.0-pro-002")
config = {
    "temperature": 0.2,
    "max_output_tokens": 300,
    "top_p": 1.0,
    "candidate_count": 2
}

prompt = "What does Centerpoint Energy do?"
response = model.generate_content(
    prompt,
    generation_config=config)
print(response.text)
