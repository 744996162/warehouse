#encoding=utf-8
__author__ = 'Administrator'
import urllib2
import json
from domain import articledomain
url1='http://api.douban.com/v2/book/isbn/9787218087351'
url2=u"http://news-at.zhihu.com/api/3/stories/latest"
html = urllib2.urlopen(url2)
hjson=json.loads(html.read())
date=hjson['date']
#提取出文章
article_json= hjson['stories']
article_dumps = json.dumps(article_json)
article_list=json.loads(article_dumps)
article_array=[]
for i in article_list:
    article=articledomain.Article()
    article.title=i['title']
    article.shareurl=i['share_url']
    article.ga_prefix=i['ga_prefix']
    article.images=i['images']
    article.type=i['type']
    article.id=i['id']
    article_array.append(article)
    #print i['title']

print len(article_array)








#print article
