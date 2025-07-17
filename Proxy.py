import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
proxies = {
    'http': 'http://your_proxy_ip:port',
    'https': 'http://your_proxy_ip:port',
}
headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers, proxies=proxies)
soup = BeautifulSoup(r.text, 'html.parser')

for tag in soup.find_all('p'):
    print(tag.text.strip())
