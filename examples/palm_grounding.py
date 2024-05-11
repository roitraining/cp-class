import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import GroundingSource

project_id = "jwd-centerpoint-class"
project_num = "[number]"
region = "us-central1"
datastore_id = "[id]"

vertexai.init(project=project_id, location=region)
model = TextGenerationModel.from_pretrained("text-bison@001")
grounding_source = GroundingSource.VertexAISearch(
    data_store_id=datastore_id, location=region, project=project_num)


prompt ="What does Centerpoint Energy do?"
response = model.predict(
    prompt,
    grounding_source=grounding_source
)
print(response.text)