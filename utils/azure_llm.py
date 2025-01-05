import os
from openai import AzureOpenAI

def get_answer(system_prompt, user_prompt):
    """Get response from Azure OpenAI"""
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    
    client = AzureOpenAI(
        api_key=api_key,
        api_version="2024-08-01-preview",
        azure_endpoint=endpoint
    )

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"