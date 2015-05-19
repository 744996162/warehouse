#ecoding=utf-8
__author__ = 'Administrator'

import sys

from db import source_hbgj_mysql
from domain import hb_model
from domain import model

reload(sys)
sys.setdefaultencoding('utf-8')

class BaseUserMysqlDao(object):
    def __init__(self, dbtype):
        self.db = source_hbgj_mysql.Mysql(dbtype=dbtype)
        print(self.db._type)

    def query_result_by_setValue(self, sql, model_class):
        result=self.db.get_all(sql)
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


class OrderPhoneDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = hb_model.CardNo):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_user_identity(self, s_day, e_day):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select TICKET_ORDERDETAIL.PASSENGERIDCARDNO  " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')>='%s' " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')<'%s' " \
            "AND PASSENGERIDTYPE=0 " % (s_day, e_day)
        print(sql)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        print(len(result_model_list))
        return result_model_list




if __name__ == "__main__":

    pass

    pass