#coding=utf-8
__author__ = 'zhangc'
import ConfigParser
import os
import sys

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# sys.path.append('..')
# path=os.path.abspath('..')


#部署路径
# conf_path="conf/db.conf"

# 测试路径
conf_path = BASE_DIR + "/conf/db.conf"

class DBConf(object):
    _inst=None
    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        with open(conf_path, 'r') as conf_file:
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

    def get_oracle(self,key):
        return self.config.get('oracle',key)


def test_oracle_get(type):
    o_test = DBConf()
    print(o_test.get_oracle(type))

    pass

def test_mysql_get(type):
    o_test = DBConf()
    print(o_test.get_mysql(type))


if __name__=="__main__":
    pass


    test_mysql_get("hostbi79")

    pass
    # test=DBConf()
    # print(test.get_mysql("databasegtgj"))
    # print(conf_path)
    # print(BASE_DIR,t)

