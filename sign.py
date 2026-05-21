import requests
import os

COOKIE = os.environ["COOKIE"]

url = "https://www.ablesci.com/user/sign"

headers = {
    "Cookie": COOKIE,
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.text)
