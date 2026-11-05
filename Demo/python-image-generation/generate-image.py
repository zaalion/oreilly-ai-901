import base64
import requests
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-mai-image

# Use the resource endpoint, without /api/projects/<project-name>.
endpoint = "https://ai901-ordemo-foundry.services.ai.azure.com"
deployment_name = "MAI-Image-2.5"
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

response = requests.post(
    f"{endpoint}/mai/v1/images/generations",
    headers={"Authorization": f"Bearer {token_provider()}"},
    json={
        "model": deployment_name,
        "prompt": "A cute puppy",
        "width": 1024,
        "height": 1024,
    },
    timeout=300,
)
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    raise requests.HTTPError(
        f"{exc}\nAzure response: {response.text}", response=response
    ) from exc

images = response.json().get("data")
if not images or not images[0].get("b64_json"):
    raise RuntimeError("MAI returned no image data.")

image_bytes = base64.b64decode(images[0]["b64_json"], validate=True)
with open("output.png", "wb") as f:
    f.write(image_bytes)

print("Image saved to output.png")
