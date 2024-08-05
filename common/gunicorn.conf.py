import os

PORT = int(os.getenv("PORT", "8000"))
DEBUG = bool(os.getenv("DEBUG", "False"))

bind = f":{PORT}"
workers = 1 
threads = 8 
timeout = 0
accesslog = "-" if DEBUG else None
