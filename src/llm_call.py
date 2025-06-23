import os
import requests
from dotenv import load_dotenv
import sys

# Add the path to the 'src' directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from prompt import PROMPT_TEMPLATE, FINAL_PROMPT_TEMPLATE

# Load environment variables
load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
API_URL = os.getenv("MISTRAL_API_URL")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_mistral_api(prompt: str) -> str:
    """
    Send prompt to Mistral API and return the response content.
    """
    data = {
        "model": "open-mistral-7b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code != 200:
        print(f"❌ Mistral API Error {response.status_code}: {response.text}")
        return "ERROR"
    
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ Error parsing Mistral response: {e}")
        return "ERROR"

def call_chunk_summary(chunk: str) -> str:
    """
    Generate metadata and summary from a single content chunk.
    """
    prompt = PROMPT_TEMPLATE.format(content_chunk=chunk)
    return call_mistral_api(prompt)

def call_combined_summary(chunk_summaries: list) -> str:
    """
    Combine multiple chunk-level summaries into one final structured output.
    """
    joined = "\n\n".join(chunk_summaries)
    prompt = FINAL_PROMPT_TEMPLATE.format(combined_summaries=joined)
    return call_mistral_api(prompt)
