# import urllib.request

# url = 'https://img.freepik.com/free-vector/flat-summer-background_23-2148971893.jpg?w=2000'
# savename = 'test.png'

# # 예외처리로 다운로드 안되는경우도 처리 필요
# urllib.request.urlretrieve(url, savename)


# from urllib import request

# url = 'https://www.naver.com/'
# # html 긁어온다, 한글은 유니코드로 처리(decode 필요)
# mem = request.urlopen(url).read()
# # print(mem.decode('UTF-8'))




import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.text)
print(r.status_code)
print(r.encoding)
print(r.json())




