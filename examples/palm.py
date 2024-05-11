import vertexai
from vertexai.language_models import TextGenerationModel

project_id = "jwd-centerpoint-class"
region = "us-central1"
vertexai.init(project=project_id, location=region)
model = TextGenerationModel.from_pretrained("text-bison@001")

prompt ="What does Centerpoint Energy do?"
response = model.predict(prompt)
print(response)