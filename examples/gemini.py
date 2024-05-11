import vertexai
from vertexai.generative_models import GenerativeModel

project_id = "jwd-centerpoint-class"
region = "us-central1"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.0-pro-002")

prompt = "What does Centerpoint Energy do?"
response = model.generate_content(prompt)
print(response.text)
