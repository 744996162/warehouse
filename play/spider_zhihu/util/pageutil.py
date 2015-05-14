#encoding=utf-8
__author__ = 'Administrator'
import json
import sys
# import urllib2
sys.path.append('..')
from util import spider
import articledomain
sys.path.append('..')
class ArticlepageUtil:

    @staticmethod
    def get_article(article_json):
        article_array = []
        data = json.loads(article_json)
        article_date=data['date']
        article_json= data['stories']
        article_dumps = json.dumps(article_json)
        article_list=json.loads(article_dumps)
        for i in article_list:
            article=articledomain.Article()
            article.title=i['title']
            article.shareurl=i['share_url']
            article.ga_prefix=i['ga_prefix']
            article.images=i['images']
            article.type=i['type']
            article.id=i['id']
            article_array.append(article)
        return article_array

if __name__ == '__main__':
    url1="http://news-at.zhihu.com/api/3/stories/latest"
    url2='http://221.235.53.172:8080/data.json'

    article_json=spider.Spider.getZhihuJson(url1)
    t=ArticlepageUtil()
    arr=t.get_article(article_json)
    #arr,time=ArticlepageUtil.get_article(article_json)
    print  arr[0].title



