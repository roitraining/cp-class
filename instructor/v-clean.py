import os
import vertexai
from vertexai.preview.language_models import TextEmbeddingModel

PROJECT_ID=env_var = os.getenv('PROJECT_ID')
LOCATION="us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)
from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID, location=LOCATION)
for e in aiplatform.MatchingEngineIndexEndpoint.list():
    e.undeploy_all()
    e.delete(force=True)