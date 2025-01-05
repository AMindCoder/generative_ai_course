import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
ENDPOINT = os.getenv("ENDPOINT_URL", "https://gaurav-mls.openai.azure.com/")
DEPLOYMENT = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")

def get_azure_openai_client():
    """Initialize and return Azure OpenAI client with Entra ID authentication"""
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )
    
    return AzureOpenAI(
        azure_endpoint=ENDPOINT,
        azure_ad_token_provider=token_provider,
        api_version="2024-05-01-preview",
    )

def create_completion(client, messages, max_tokens=800, temperature=0.7):
    """Create a completion using Azure OpenAI"""
    return client.chat.completions.create(
        model=DEPLOYMENT,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )
