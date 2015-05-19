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

class BuyTimes():
    def __init__(self):
        self.phoneid = ""
        self.passengerno = ""

    def setValues(self, valueList):
        self.phoneid = str(valueList[0])
        self.passengerno = str(valueList[1])
        pass
    pass

class ConsumersId():
    def __init__(self):
        self.phoneid = ""

    def setValues(self, valueList):
        self.phoneid = str(valueList[0])
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
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = BuyTimes):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_user_identity(self):
        sql="select TICKET_ORDER.PHONEID,TICKET_ORDERDETAIL.PASSENGERIDCARDNO  " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150401' "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_phoneid(self):
        sql="select TICKET_ORDER.PHONEID  " \
            "from TICKET_ORDER " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150401' "
        result_model_list = self.db.query_result_by_setValue(sql, ConsumersId)
        return result_model_list


def helo_others_num_main():
    o_object = OrderDao()
    result_model_list = o_object.get_user_identity()

    d = defaultdict(list)
    count = 1

    print(str(0) + "\t" + str(time.ctime()))
    for model in result_model_list:
        count += 1
        phoneid = str(model.phoneid)
        passengerno = str(model.passengerno)
        d[phoneid].append(passengerno)
    print(count)
    result_dict = {}

    ###乘客数，存储
    passenger_num_list = []

    for key, value in d.items():
        count += 1
        list_num = len(value)
        set_num = len(set(value))
        result_dict[key] = set_num
        passenger_num_list.append(set_num)
        if set_num > 20:
            print(key,set_num)
        # out_file.write(str(key) + "\t" + str(list_num) + "\t" + str(set_num) + "\n")

    ##给多少乘客买过票
    out_file = open("passenger_num.data","a")
    counter = Counter(passenger_num_list)
    for key,value in counter.items():
        print(key,value)
        out_file.write(str(key) + "\t" + str(value) + "\n")


    pass


def consumers_buy_times():
    o_object = OrderDao()
    result_model_list = o_object.get_phoneid()

    """存储所有订单的phoneid"""
    phoneid_list = []

    for model in result_model_list:
        phoneid = str(model.phoneid)
        phoneid_list.append(phoneid)

    counter = Counter(phoneid_list)

    file_out = open("buy_times.data","a")

    """存储购买次数"""
    value_list = []
    for key,value in counter.items():
        value_list.append(value)

    for key, value in Counter(value_list).items():
        print(key,value)
        file_out.write(str(key) + "\t" + str(value) + "\n")
        pass
    pass

if __name__ == "__main__":
    consumers_buy_times()
    # testOrderPhone()
    # phoneDictTest()
    # testPhoneDictDao()
    # testOrderPhoneDao()
    # testPhoneDictDao()

    pass