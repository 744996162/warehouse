__author__ = 'Administrator'
# from conf import conf
from util import pageutil,spider

def zhihu():
    url= spider.Spider.getZhihuUrl()
    zhihu_json= spider.Spider.getZhihuJson(url)
    arr,time= pageutil.ArticlepageUtil.get_article(zhihu_json)
    print arr

    pass


if __name__ == '__main__':
    zhihu()
