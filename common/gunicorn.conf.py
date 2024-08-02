import os

PORT = int(os.getenv("PORT", "8000"))

bind = f":{PORT}"
workers = 1 
threads = 8 
timeout = 0
