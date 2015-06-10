__author__ = 'Administrator'

import urllib2
import time

def getStr(url):
    req_headers = {}
    req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    req_headers['Accept-Encoding'] = 'deflate'
    req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
    req_headers['Referer'] = "http://search.rsscc.cn"
    req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
    request = urllib2.Request(url, headers=req_headers)

    page_content = urllib2.urlopen(request)
    str_out = page_content.read()

    return str_out


if __name__ == "__main__":
    print(time.ctime())
    for i in range(1000000):
        url = "http://127.0.0.1:8000/monitor?p1=china&p2=2015&pageid=B2&date=2015-06-05&client=ios&source=app_store&dep=BJS&arr=SHA&loadingtime=234&uid=123456"
        getStr(url)
        if i % 10000 == 0:
            print(i, time.ctime())

    pass