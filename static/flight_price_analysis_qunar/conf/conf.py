#coding=utf-8
__author__ = 'zhangc'
import ConfigParser
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#测试路径
# conf_path=path+"/conf/db.conf"
# conf_path=path+"/conf/db3.conf"
#部署路径
# conf_path="conf/db3.conf"
# conf_path="db.conf"
conf_path=BASE_DIR+"/conf/db.conf"
class DBConf(object):
    _inst=None
    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        with open(conf_path,'r') as conf_file:
        # with open(conf_path,'r') as conf_file:
            self.config.readfp(conf_file)

    @staticmethod
    def getInst():
        if not DBConf._inst:
            DBConf._inst = object.__new__(DBConf)
            DBConf._inst.__init__()
        return DBConf._inst

    def get_mysql(self, key):
        return self.config.get('mysql', key)

if __name__=="__main__":
    pass
    test=DBConf()
    # print(test.get_mysql("databasegtgj"))
    print(test.get_mysql("databasebi"))

