import requests
import json

base_url = "https://jsonplaceholder.typicode.com/posts"
page = 1
all_results = []

print("Starting")

while True:
    print(f"Fetching page {page}")
    response = requests.get(base_url, params={"_page": page, "_limit": 10})
    data = response.json()
    if not data:
        print("End reached!")
        break
        
    all_results.extend(data)
    page += 1

print(f"\nTotal fetched posts: {len(all_results)}")

with open("paginated_results.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2)

print("Data successfully saved")
