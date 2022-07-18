import urllib.request
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/point/af/list.naver?&page=2'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')

titlelist = []
title = soup.select('a.movie.color_b')
for item in title:
    titlelist.append(item.string)

ratelist = []
rate = soup.select('td.title em')
for item in rate:
    ratelist.append(item.string)
    
msglist = []
msg = soup.select('td.title')
for item in msg:
    msglist.append(item.get_text().replace('\n','').replace('\t',''))
    
print(msglist)

print(list(zip(titlelist, ratelist, msglist)))



table = soup.find('table',class_='list_netizen')
for i,r in enumerate(table.select('tbody tr')):
    for j,c in enumerate(r.find_all('td')):
        if j==0:
            rec = int(c.text.strip())
            print('글번호 : ',rec)
        elif j==1:
            rec1 = c.select_one('a').text.strip()
            print('영화제목 : ',rec1)
            rec2 = c.select_one('em').text
            print('영화평점 : ',rec2)
            rec3 = c.text
            rec3 = rec3.replace(rec1,'')
            rec3 = rec3.replace('신고','')
            rec3 = re.sub()