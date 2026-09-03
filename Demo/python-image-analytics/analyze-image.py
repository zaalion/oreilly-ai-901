import os
import base64
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key= os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = 'gpt-4o'
api_version = '2023-12-01-preview' # this might change in the future

client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    azure_endpoint=api_base.removesuffix("/openai/v1"),
    azure_deployment=deployment_name
)

image_path = os.path.join(os.path.dirname(__file__), "Albuquerque,_New_Mexico_skyline.jpg")
with open(image_path, "rb") as image_file:
    image_data_uri = f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Describe this picture:" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    "url": image_data_uri
                }
            }
        ] } 
    ],
    max_tokens=500 
)

print(response)