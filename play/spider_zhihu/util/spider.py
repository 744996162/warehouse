#encoding=utf-8
__author__ = 'Administrator'
import urllib2
# from BeautifulSoup import BeautifulSoup
# import json
# from conf import *
import sys,os
sys.path.append('..')
import conf


class Spider():
    @staticmethod
    def getZhihuUrl(date=""):
        if date=="":
            t=conf.ZHIHUConf()
            return t.get_today()
        else:
            t=conf.ZHIHUConf()
            return t.get_before(date)
            pass

    '''获取网页内容'''
    @staticmethod
    def getZhihuJson(url):
        #提取出json
        req_headers = {}
        req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        req_headers['Accept-Encoding'] = 'deflate'
        req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
        req_headers['Connection'] = 'keep-alive'
        req_headers['Cookie'] = 'Hm_lvt_339d749938744acd9bea875d1d494696=1402974179,1403052976,1403086979,1403139829; Hm_lpvt_339d749938744acd9bea875d1d494696=1403165411'
        req_headers['DNT'] = 1
        #req_headers['Host'] = 'hm.baidu.com'
        req_headers['Referer'] = 'http://www.zhihudaily.com/'
        req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        request=urllib2.Request(url,headers=req_headers)
        page_content=urllib2.urlopen(request)
        #page_charset=page_content.info().getparam('charset')
        article_json=page_content.read()

        #article_json=BeautifulSoup(html_doc,fromEncoding=page_charset)
        return article_json


if __name__ == '__main__':
    url="http://news-at.zhihu.com/api/3/stories/latest"
    #print Spider.getZhihuContent(url)

    t=conf.ZHIHUConf()
    t_url=t.get_today()
    zhihuContent=Spider.getZhihuContent(t_url)
    print t_url
    print t.get_today()
    print t.get_before(20131102)
    print zhihuContent
    print os.path.abspath('..')




