import requests
# import re
from bs4 import BeautifulSoup
import time
# import os

runing_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Cookie': '***'
}

url = 'https://www.smzdm.com'

r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()
html = r.text
soup = BeautifulSoup(html, "html.parser")
for name in soup.find_all("li", class_="feed-row-wide"):
    link = name.find('h5').find('a').attrs['href']
    name1 = name.find_all('a')[1].text	#.lstrip()
    price = name.find_all('a')[2].text	#.lstrip()
    print(link, name1, price, "\n")
