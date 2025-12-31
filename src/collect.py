import json
import time
from pathlib import Path
import requests

URL = "https://remoteok.io/api"  

response = requests.get(URL, timeout=30)
response.raise_for_status()
data = response.json()

jobs = [item for item in data if isinstance(item, dict) and "id" in item]

Path("data/raw").mkdir(parents=True, exist_ok=True)

timestamp = time.strftime("%Y%m%d_%H%M%S")
out_path = f"data/raw/remoteok_jobs_{timestamp}.json"

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2)

print("Saved:", out_path)
print("Jobs collected:", len(jobs))