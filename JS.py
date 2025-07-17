from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

url = 'https://example.com/js-content'
driver.get(url)
time.sleep(5)  # Allow JS to render

content = driver.page_source
print(content[:500])
driver.quit()
