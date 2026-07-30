import requests
import json

print("Fetching users")
users_resp = requests.get("https://jsonplaceholder.typicode.com/users")
users_resp.raise_for_status()
users = users_resp.json()

user_map = {u["id"]: u["name"] for u in users}

print("Fetching posts")
posts_resp = requests.get("https://jsonplaceholder.typicode.com/posts")
posts_resp.raise_for_status()
posts = posts_resp.json()
enriched_data = []

for post in posts:
    post["author"] = user_map.get(post["userId"], "Unknown")
    enriched_data.append(post)

print(f"Enriched {len(enriched_data)} posts")

with open("enriched_posts.json", "w", encoding="utf-8") as f:
    json.dump(enriched_data, f, indent=2)

print("Saved to enriched_posts.json")