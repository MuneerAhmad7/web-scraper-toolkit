import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.find_all('h2')
for title in titles:
    print(title.text.strip())
