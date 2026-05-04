import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

print("Endpoint:", endpoint)
print("Deployment:", deployment)
print("Key exists:", bool(api_key))

llm = ChatOpenAI(
    model=deployment,
    base_url=endpoint,
    api_key=api_key,
    temperature=0.2,
)

response = llm.invoke("Say only: Azure OpenAI connection OK")

print(response.content)