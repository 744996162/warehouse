#coding=utf-8
__author__ = 'zhangchao'
from source_gtgj_mysql import *
from domain.gtgj_model import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')

class BaseUserDao(Mysql):

    def __init__(self, dbtype_dao='gtgj89'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result_by_setValue(self, sql, model_class):
        result = self.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            # print(value_list)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class TravelTimeDao(object):
    def __init__(self, DBClass=BaseUserDao, ModelClass=TravelTime):
        self.db = DBClass(dbtype_dao="gtgj89")
        self.ModelClass = ModelClass

    def get_data(self,s_day, e_day):

        sql = "SELECT uid,train_no,seat_name,price,depart_time,arrive_time " \
        "FROM user_sub_order " \
        "where status='支付成功' " \
        "and DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s'  " \
         "and DATE_FORMAT(create_time,'%%Y%%m%%d')<'%s'  "  %(s_day, e_day)
        # print(sql)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_data_to_txt(self, s_day,e_day, file_path):
        result_model_list = self.get_data(s_day, e_day)
        print(s_day, len(result_model_list))
        file_out = open(file_path, "a")
        for model in result_model_list:
            file_out.write(model.toString() + "\n")

        pass


def testMain(s_day,e_day):
    # print(s_day)
    o_object = TravelTimeDao()
    out_path = "data/" + s_day + "_" + e_day
    o_object.get_data_to_txt(s_day, e_day, out_path)
    pass


if __name__ == '__main__':
    testMain("20150402", "20150407")
    testMain("20150407", "20150412")
    testMain("20150412", "20150417")
    testMain("20150417", "20150423")
    testMain("20150423", "20150428")
    testMain("20150428", "20150501")
    pass
