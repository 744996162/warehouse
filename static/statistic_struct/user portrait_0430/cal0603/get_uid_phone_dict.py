#ecoding=utf-8
__author__ = 'Administrator'
from db import source_hbgj_mysql
from db import source_gtgj_mysql
import sys


class Uid():
    def __init__(self):
        self.uid = ""
        self.phone = ""

    def setValues(self, valueList):
        self.uid = str(valueList[0])
        self.phone = str(valueList[1])

    def getStr(self):
        out_str = str(self.uid) + "\t" + str(self.phone)
        return out_str



class HbBaseDao(source_hbgj_mysql.Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        source_hbgj_mysql.Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result_by_setValue(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class GtBaseDao(source_gtgj_mysql.Mysql):
    def __init__(self, dbtype_dao='gtgj89'):
        source_gtgj_mysql.Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result_by_setValue(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list



class Hb_uid_phone_dict():
    """
    table: phone_user
    "select phoneid,phone from phone_user"

    """

    def __init__(self, DBClass = HbBaseDao, ModelClass=Uid):
        self.db = DBClass()
        self.ModelClass = ModelClass
    def get_data(self, limit_start, limit_num):

        sql = "select phoneid, phone from phone_user LIMIT %d, %d" %(limit_start, limit_num)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_data_to_txt(self, limit_start, limit_num, file_name):
        file_out = open(file_name, "a")
        result_model_list = self.get_data(limit_start, limit_num)
        for model in result_model_list:
            file_out.write(model.getStr() + "\n")
        file_out.close()
        pass




class Gt_uid_phone_dict():
    """
    table: account_gtgj
    "select userid,uid from account_gtgj"

    """
    def __init__(self, DBClass = GtBaseDao, ModelClass=Uid):
        self.db = DBClass()
        self.ModelClass = ModelClass

    def get_data(self, limit_start, limit_num):

        sql = "select uid,gt_user_name from account_gtgj LIMIT %d, %d" %(limit_start, limit_num)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_data_to_txt(self, limit_start, limit_num, file_name):
        file_out = open(file_name, "a")
        result_model_list = self.get_data(limit_start, limit_num)
        for model in result_model_list:
            file_out.write(model.getStr() + "\n")
        file_out.close()
        pass

    pass

if __name__ == "__main__":

    # o_hb = Hb_uid_phone_dict()
    # for i in range(0, 7330150, 100000):
    #     print(i, 100000)
    #     o_hb.get_data_to_txt(i, 100000, "hb.dat")
    # print("hello")


    o_gt = Gt_uid_phone_dict()
    for i in range(0, 7442892, 100000):
        print(i, 100000)
        o_gt.get_data_to_txt(i, 100000, "gt.dat")
    # o_gt.get_data_to_txt(0, 100, "gt_test.dat")
