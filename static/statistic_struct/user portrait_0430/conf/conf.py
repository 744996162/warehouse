#ecoding=utf-8
__author__ = 'zhangc'
import ConfigParser
import os

this_path = os.getcwd()
parent_path = os.path.dirname(this_path)

conf_file_name = "db.conf"

# print(base_path)

#测试路径
conf_path_test = parent_path + "/conf/" + conf_file_name

#部署路径
conf_path = "conf/" + conf_file_name
# conf_path = "conf/db.conf"
# print(conf_path_test)

conf_path_this = "G:/github/com.zc/static/statistic_struct/conf/db.conf"

class DBConf(object):
    _inst = None
    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        try:
            with open(conf_path_test, 'r') as conf_file:
                self.config.readfp(conf_file)
        except Exception as e:
            # print(e)
            try:
                with open(conf_path, 'r') as conf_file:
                    self.config.readfp(conf_file)
            except Exception as e:
                with open(conf_path_this, 'r') as conf_file:
                    self.config.readfp(conf_file)

    @staticmethod
    def getInst():
        if not DBConf._inst:
            DBConf._inst = object.__new__(DBConf)
            DBConf._inst.__init__()
        return DBConf._inst

    def get_mysql(self, key):
        return self.config.get('mysql', key)

if __name__ == "__main__":
    test = DBConf()
    print(test.get_mysql("databasegtgj89"))


