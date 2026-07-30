import os
import json
import requests

cache_file = "cache.json"
url = "https://jsonplaceholder.typicode.com/todos/1"

if os.path.exists(cache_file):
    print("Loading from cache...")
    with open(cache_file, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    print("Fetching from API...")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved to cache.")

print(f"Data: {data['title']}")
