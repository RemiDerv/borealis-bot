import requests
from datetime import datetime

url = "https://www.borealischaravoile.fr/"

try:
    r = requests.get(url, timeout=20)

    print(f"[{datetime.now()}]")
    print("Status :", r.status_code)

except Exception as e:
    print(e)
