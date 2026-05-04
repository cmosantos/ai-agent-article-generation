import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

print("Endpoint:", endpoint)
print("Deployment:", deployment)
print("API version:", api_version)
print("Key exists:", bool(api_key))

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version=api_version,
)

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "user", "content": "Say only: Azure OpenAI connection OK"}
    ],
)

print(response.choices[0].message.content)