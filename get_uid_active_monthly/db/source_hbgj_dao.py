__author__ = 'zhangchao'

import sys
sys.path.append('..')

from source_hbgj_oracle import *

class Hb_uid(object):
    def __init__(self):
        self.uid = ""
        pass

    def __str__(self):
        out_str = "Hb_uid:" + "\t" + self.uid
        return out_str



class BaseUserOracleDao(object):
    def __init__(self):
        self.cursor = oracle_con()

    def query_result(self, sql, model_class):
        cursor = oracle_con()
        cursor.execute(sql)
        result=cursor.fetchall()
        users_model_list = []
        if not result:
            return False
        for row in result:
            model_object = model_class()
            model_object.uid = row[0]
            users_model_list.append(model_object)
        return users_model_list

class ActiveUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass=Hb_uid):
        self.db = DBClass()
        self.ModelClass = ModelClass

    def get_users_uid_monthly(self,querydate_str):
        sql="select distinct userid " \
            "from ACTIVE_USER_LOG where createtime>=to_date('%s', 'yyyymmdd') AND rownum<=10 " % querydate_str
        print(sql)
        result_model_list=self.db.query_result(sql, self.ModelClass)
        uid_list = []
        for model in result_model_list:
            uid_list.append(model.uid)
        return uid_list

    def get_users_uid_monthly_to_txt(self, querydate_str, data_path="data/"):
        uid_list = self.get_users_uid_monthly(querydate_str)
        file_name = "Hb_uid" + querydate_str[0:5]
        file_path = data_path + file_name
        file_out = open(file_path, "a")

        for uid in uid_list:
            file_out.write(uid + "\n")

        pass



if __name__ == '__main__':
    o_object = ActiveUsersDao()
    o_object.get_users_uid_monthly_to_txt("20120101")

    pass