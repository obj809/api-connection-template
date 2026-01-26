import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY not set")

API_URL = ""

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    print("API connection successful!")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")