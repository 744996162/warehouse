#ecoding=utf-8
__author__ = 'Administrator'

import sys

from db import source_hbgj_mysql
from domain import hb_model
from domain import model
from collections import defaultdict
from collections import Counter
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class Discount():
    def __init__(self):
        self.phoneid = ""
        self.discount = ""

    def setValues(self, valueList):
        self.phoneid = str(valueList[0])
        self.discount = str(valueList[1])
        pass
    pass


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


class OrderDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = Discount):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_data(self):
        sql="select TICKET_ORDER.PHONEID,TICKET_ORDERDETAIL.DISCOUNT  " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150401' "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list


def hb_high_level_discount():
    o_object = OrderDao()
    result_model_list = o_object.get_data()

    d = defaultdict(list)
    count = 1

    print(str(0) + "\t" + str(time.ctime()))
    for model in result_model_list:
        count += 1
        phoneid = str(model.phoneid)

        try:
            discount = float(model.discount)
        except Exception as e:
            # print(e)
            # print(result_model.discount)
            discount = 0.7
        d[phoneid].append(discount)
    print(count)
    result_dict = {}

    out_discount_level = open("discount_level(0.8+).data","a")

    ###乘客数，存储
    phoneid_list = []

    for key, value in d.items():
        count += 1
        set_value = set(value)
        state = 1
        for discount in set_value:
            if float(discount) < 0.8:
                state = 0
                break
        if state == 1:
            ticket_num = len(value)
            phoneid_list.append(key)
            out_discount_level.write(str(key) + "\t" + str(ticket_num) + "\n")
    print(len(phoneid_list))


if __name__ == "__main__":
    hb_high_level_discount()
    # testOrderPhone()
    # phoneDictTest()
    # testPhoneDictDao()
    # testOrderPhoneDao()
    # testPhoneDictDao()

    pass