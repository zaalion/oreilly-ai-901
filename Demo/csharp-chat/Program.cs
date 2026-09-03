using Azure.Identity; 
using OpenAI;
using OpenAI.Responses;
using System.ClientModel.Primitives;

#pragma warning disable OPENAI001

const string deploymentName = "gpt-5.4-mini";
const string endpoint = "https://ai900-foundry-try.services.ai.azure.com/openai/v1";

BearerTokenPolicy tokenPolicy = new(
    new DefaultAzureCredential(),
    "https://ai.azure.com/.default");

ResponsesClient client = new(
    authenticationPolicy: tokenPolicy,
    options: new OpenAIClientOptions()
    {
        Endpoint = new Uri($"{endpoint}"),
    });
CreateResponseOptions options = new()
{
    Model = deploymentName,
    InputItems =
    {
        ResponseItem.CreateUserMessageItem("What's the weather like today for my current location?"),
    },
};

ResponseResult response = client.CreateResponse(options);

Console.WriteLine($"[ASSISTANT]: {response.GetOutputText()}");
