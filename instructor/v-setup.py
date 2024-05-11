import os
from vertexai.preview.language_models import TextEmbeddingModel
import numpy as np

INITIALS = os.getenv('INITIALS')
PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION="us-central1"

from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# create IndexEndpoint
my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
  display_name = f"{INITIALS}_endpoint",
  public_endpoint_enabled = True,
)

indexes = aiplatform.MatchingEngineIndex.list()
for index in indexes:
    pass

# deploy the Index to the Index Endpoint
my_index_endpoint.deploy_index(
  index = index, deployed_index_id = f"{INITIALS}_deploy"
)

print (f"endpoint_id: {my_index_endpoint.name}")
print (f"deployed_index_id: {my_index_endpoint.deployed_indexes[0].id}")
