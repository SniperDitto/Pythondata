import urllib.request
from bs4 import BeautifulSoup


url = 'https://music.bugs.co.kr/chart'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')

titlelist = []
title = soup.select('p.title a')
for item in title:
    titlelist.append(item.string)

artistlist = []
artist = soup.select('p.artist > a:nth-of-type(1)')
for item in artist:
    artistlist.append(item.string)

print(list(zip(titlelist,artistlist)))

