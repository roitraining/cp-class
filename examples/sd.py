import base64
from io import BytesIO
from PIL import Image

from google.cloud import aiplatform

from config import project_id, region

def base64_to_image(image_str):
    """Convert base64 encoded string to an image."""
    image = Image.open(BytesIO(base64.b64decode(image_str)))
    return image


def get_endpoint(endpoint_id: str) -> aiplatform.Endpoint:
    """Returns a Vertex endpoint for the given endpoint_name."""


    endpoint = aiplatform.Endpoint(
        f"projects/{project_id}/locations/{region}/endpoints/{endpoint_id}"
    )

    return endpoint

comma_separated_prompt_list = "A photo of an astronaut riding a horse on mars, A stone castle in a forest by the river"
prompt_list = [x.strip() for x in comma_separated_prompt_list.split(",")]
height = 768  # @param {type:"number"}
width = 768  # @param {type:"number"}
num_inference_steps = 25  # @param {type:"number"}
guidance_scale = 7.5  # @param {type:"number"}

instances = [
    {
        "prompt": prompt,
        "negative_prompt": "",
        "height": height,
        "width": width,
        "num_inference_steps": num_inference_steps,
        "guidance_scale": 7.5,
    }
    for prompt in prompt_list
]

endpoint = get_endpoint("3023997824988610560")
response = endpoint.predict(instances=instances)
images = [base64_to_image(image) for image in response.predictions]
for image in images:
    st.image(image, use_column_width=True)