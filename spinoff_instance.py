import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv("SOVERNSTACK_TOKEN")
url = f"https://api.sovernstack.com/v1/notebooks"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
}

payload = {
    "node_id": "kl-1",
    "num_gpus": 1,
    "vram_slices": 4,
    "notebook_name": "Fine-tuning Qwen",
}
try:
  response = requests.post(url, headers=headers, json=payload)

  print(f"Status Code: {response.status_code}")
  print("Response:")
  print(json.dumps(response.json(), indent=2))

except requests.exceptions.RequestException as e:
  print(f"❌ An error occurred: {e}")