import requests
import time

url = "https://httpstat.us/503"
max_retries = 3
backoff_time = 2

for attempt in range(1, max_retries + 1):
    print(f"Try {attempt}/{max_retries}: {url}")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        print("Success!")
        break
    except requests.exceptions.RequestException as e:
        print(f"Failed: {e}")
        if attempt < max_retries:
            print(f"Wait {backoff_time}s...\n")
            time.sleep(backoff_time)
            backoff_time *= 2
        else:
            print("\nAPI is down.")