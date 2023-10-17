from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import requests
from bs4 import BeautifulSoup

url = f'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=30&week=&systemType=PC'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
params = {"show_ram": 1}

resp = requests.get(url, headers=headers).json()
print(resp)
