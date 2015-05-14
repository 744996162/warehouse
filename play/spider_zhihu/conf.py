__author__ = 'Administrator'
import ConfigParser
import os
import sys
sys.path.append('..')
sys.path.append('..\spider_zhihu')
sys.path.append('..\spider_zhihu\util')
path_temp=os.path.abspath('..')
conf_path=path_temp+"\zhihu.con"

class ZHIHUConf(object):
    _inst=None
    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        with open(conf_path,'r') as conf_file:
            self.config.readfp(conf_file)
        #self.config.read('zhihu.conf')

    @staticmethod
    def  get_inst():
        if not ZHIHUConf._inst:
            ZHIHUConf._inst=object.__new__(ZHIHUConf)
            ZHIHUConf._inst.__init__()
        return ZHIHUConf._inst


    def get_today(self):
        return self.config.get('zhihu','today')


    def get_before(self,date):
        url1=self.config.get('zhihu','before')
        url2=str(date)
        url=url1+url2
        return url


def test():
    t=ZHIHUConf()
    print t.get_today()
    print t.get_before(20140512)

if __name__ == '__main__':
    test()

    print os.path.abspath('..'),conf_path
    # print os.path.abspath('..\spider_zhihu')