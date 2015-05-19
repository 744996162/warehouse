#ecoding=utf-8
__author__ = 'Administrator'

from db import source_hbgj_mysql
import sys
import time
from collections import defaultdict
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

class Seat_level():
    def __init__(self):
        self.uid = ""
        self.seat_name = ""
        self.discount = ""
        pass

    def setValues(self, valueList):
        self.uid = str(valueList[0])
        self.seat_name = str(valueList[1])
        self.discount = str(valueList[2])


    def __str__(self):
        out_Str = "Seat_level:" + "\t" + self.uid + "\t" + self.seat_name
        return out_Str


class BaseUserMysqlDao(object):
    def __init__(self, dbtype):
        self.db = source_hbgj_mysql.Mysql(dbtype=dbtype)
        # print(self.db._type)

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

class Flight_seat_level(object):

    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass=Seat_level):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_data(self, s_day, e_day=""):

        sql = "SELECT TICKET_ORDER.PHONEID,TICKET_ORDERDETAIL.BASECABIN,TICKET_ORDERDETAIL.DISCOUNT " \
        "FROM TICKET_ORDERDETAIL " \
        "join TICKET_ORDER " \
        "ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
        "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
        "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')>='%s' " \
        "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')<'%s'  " % (s_day, e_day)
        result_model_list = self.db.query_result_by_setValue(sql,model_class=self.ModelClass)
        return result_model_list
    pass


def getDict():
    d_seat_level = defaultdict(list)
    d_discount = defaultdict(list)

    o_Flight_seat = Flight_seat_level()
    result_model_list = o_Flight_seat.get_data("20120101", "20150401")
    count = 0
    for result_model in result_model_list:
        count += 1
        uid =result_model.uid
        seat_name = result_model.seat_name
        try:
            discount = float(result_model.discount)
        except Exception as e:
            # print(e)
            # print(result_model.discount)
            discount = 0.7

        d_seat_level[uid].append(seat_name)
        d_discount[uid].append(discount)

        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

    return d_seat_level, d_discount

def statistics():
    d_seat_level, d_discount = getDict()

    out_seat_level = open("flight_seat_level.data", "a")
    out_dictount = open("flight_discount.data", "a")

    count = 1

    seat_level = ["F", "C", "J"]


    """seat_level"""
    for key, value in d_seat_level.items():
        count += 1
        set_seat_name = set(value)
        state = 1

        for seat_name in set_seat_name:
            print(seat_name)
            if seat_name not in seat_level:
                state = 0
                break

        if state == 1:
            ticket_num = len(value)
            out_seat_level.write(key + "\t" + str(ticket_num) + "\n")

    for key, value in d_discount.items():

        set_discount = set(value)
        state = 1

        for discount in set_discount:
            if discount > 0 :
                state = 0
                break

        if state == 1:
            print(value)
            ticket_num = len(value)
            out_dictount.write(key + "\t" + str(ticket_num) + "\n")

    print(time.ctime())

def test_Flight_seat():
    o_Flight_seat = Flight_seat_level()
    result = o_Flight_seat.get_data("20120101", "20150401")
    for i in result:
        print(i)
    pass


def hb_discount_statistic(s1,s2):

    o_Flight_seat = Flight_seat_level()
    result_model_list = o_Flight_seat.get_data(s1, s2)
    discount_list = []
    count = 0
    count_all = 0
    for result_model in result_model_list:
        count_all += 1
        # uid =result_model.uid
        # seat_name = result_model.seat_name
        try:
            discount = float(result_model.discount)
        except Exception as e:
            # print(e)
            # print(result_model.discount)
            discount = 0.7
        if discount >= 0.8:
            count += 1
    return count_all, count

def hb_discount_statistic_main():
    file_out = "data/discount_result.data"

    print("20130101",hb_discount_statistic("20130101","20130401"))
    print("20130401",hb_discount_statistic("20130401","20130701"))
    print("20130701",hb_discount_statistic("20130701","20131001"))
    print("20131001",hb_discount_statistic("20131001","20140101"))

    print("20140101",hb_discount_statistic("20140101","20140401"))
    print("20140401",hb_discount_statistic("20140401","20140701"))
    print("20140701",hb_discount_statistic("20140701","20141001"))
    print("20141001",hb_discount_statistic("20141001","20150101"))

    print("20150101",hb_discount_statistic("20150101","20150401"))
    pass

if __name__ == "__main__":

    # test_Flight_seat()
    hb_discount_statistic_main()
    pass