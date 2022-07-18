# https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B4%91%EC%95%88%EB%A6%AC&oquery=%EB%B0%94%EB%8B%A4&tqi=hV40CwprvTVssiLzu5sssssss6w-401148

import urllib.request
import urllib.parse

url = 'https://search.naver.com/search.naver'
values = {
    'sm':'tab_hty',
    'where':'nexearch',
    'query':'광안리',
    'fbm':'1',
    'ie':'utf8'
}

param = urllib.parse.urlencode(values)
print(param)
data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)