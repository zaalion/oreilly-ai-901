# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://ai900-foundry-try.services.ai.azure.com/api/projects/proj-default"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "ai901-ordemo-agent01"
my_version = "2"

openai_client = project_client.get_openai_client()

previous_response_id = None

while True:
    user_input = input("You: ")
    if user_input.strip().upper() == "EXIT":
        break

    request_kwargs = {
        "input": [{"role": "user", "content": user_input}],
        "extra_body": {"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    }
    if previous_response_id:
        request_kwargs["previous_response_id"] = previous_response_id

    response = openai_client.responses.create(**request_kwargs)

    previous_response_id = response.id
    print(f"Agent: {response.output_text}")