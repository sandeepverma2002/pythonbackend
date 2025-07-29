# cards/auto_ping.py

import threading
import time
import requests

def keep_alive():
    while True:
        try:
            print("Pinging Render server...")
            requests.get("https://your-backend-url.onrender.com/ping/")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(300)  # 5 minutes
