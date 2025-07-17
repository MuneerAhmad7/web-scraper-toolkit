import requests
import re
from bs4 import BeautifulSoup

url = 'https://example.com'
headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))

for email in emails:
    print(email)
