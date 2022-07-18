from unittest import result
import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/'
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
result = soup.select('strong.title')

print(result)

name = []
for item in result:
    name.append(item.text)


img = []
result = soup.select('span.thumb-image img')
for item in result:
    img.append(item['src'])

print(list(zip(name,img)))

