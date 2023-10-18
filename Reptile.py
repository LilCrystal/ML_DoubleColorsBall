from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import requests
import json
from bs4 import BeautifulSoup


class SingleResult(object):
    def __init__(self, num: int, date: str, red: str, blue: int):
        self.num = num
        self.date = date
        self.red = red
        self.blue = blue


def json_to_object(result: dict) -> SingleResult:
    obj = SingleResult(
        num=result['code'],
        date=result['date'],
        red=result['red'],
        blue=result['blue']
    )
    return obj


url = f'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=30&week=&systemType=PC'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
params = {"show_ram": 1}

response = requests.get(url, headers=headers)
rawJson = response.content.decode('utf-8')

json_data = json.loads(rawJson)

result = []
for resultTmp in json_data['result']:
    result.append(resultTmp)

print(result)

objectList = []

for singleResult in result:
    objectList.append(json_to_object(singleResult))

for single in objectList:
    print('期号为：', single.num)
    print('日期为：', single.date)
    print('红球为：', single.red)
    print('蓝球为：', single.blue)
    print('\n')







