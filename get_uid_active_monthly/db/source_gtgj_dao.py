__author__ = 'zhangchao'
from source_gtgj_mysql import *

import sys
sys.path.append('..')

class Gt_uid(object):
    def __init__(self):
        self.uid =  ""
        pass

    def __str__(self):
        out_str = "Gt_uid:" + "\t" + self.uid
        return out_str

class BaseUserDao(Mysql):
    def __init__(self, dbtype_dao='gtgj89'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result(self, sql, model_class):
        results = self.get_all(sql)
        users_model_list=[]
        if not results:
            return False
        for row in results:
            model_object = model_class()
            model_object.uid = row[0]
            users_model_list.append(model_object)
        return users_model_list


class ActiveUsersDao(object):
    def __init__(self, DBClass=BaseUserDao, ModelClass=Gt_uid):
        self.db = DBClass(dbtype_dao="gtgj89")
        self.ModelClass = ModelClass
# client_info


    def get_users_uid_monthly(self, querydate_str):

        sql="SELECT uid " \
            "FROM client_info where DATE_FORMAT(update_time,'%%Y%%m%%d')>=%s  LIMIT 10 " % querydate_str
        print(sql)
        result_model_list = self.db.query_result(sql, self.ModelClass)
        uid_list = []
        for model in result_model_list:
            uid_list.append(model.uid)
        return uid_list

    def get_users_uid_monthly_to_txt(self, querydate_str, data_path="data/"):

        uid_list = self.get_users_uid_monthly(querydate_str)
        file_name = "Gt_uid" + querydate_str[0:5]
        file_path = data_path + file_name
        file_out = open(file_path, "a")

        for uid in uid_list:
            file_out.write(uid + "\n")
        pass

if __name__ == '__main__':
    # activeUsersDaoTest()
    # newUsersDaoTest()
    # consumersDaoTest()
    o_object = ActiveUsersDao()
    o_object.get_users_uid_monthly_to_txt("20120101")
    pass
