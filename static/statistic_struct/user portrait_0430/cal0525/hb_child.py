#ecoding=utf-8
__author__ = 'Administrator'

from db import source_hbgj_mysql
import sys
import time
from collections import defaultdict
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

class Child_Price():
    def __init__(self):
        self.cardno = ""
        self.price = ""
        pass

    def setValues(self, valueList):
        self.cardno = str(valueList[0])
        self.price = str(valueList[1])

    def __str__(self):
        out_Str = "Child_Price:" + "\t" + self.cardno + "\t" + self.price
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

class Flight_child_price(object):

    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass=Child_Price):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_data(self, s_day, e_day):

        sql = "SELECT TICKET_ORDERDETAIL.PASSENGERIDCARDNO,TICKET_ORDERDETAIL.price " \
        "FROM TICKET_ORDERDETAIL " \
        "join TICKET_ORDER " \
        "ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
        "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
        "and TICKET_ORDERDETAIL.PASSENGERTYPE='CHD'" \
        "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')>='%s' " \
        "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')<'%s'  " % (s_day, e_day)
        result_model_list = self.db.query_result_by_setValue(sql,model_class=self.ModelClass)
        return result_model_list
    pass


    def average_cal(self, s_day, e_day):
        result_model_list = self.get_data(s_day, e_day)
        sum = 0
        count = 0

        # 420984199010083651
        for model in result_model_list:
            cardno = model.cardno
            if len(cardno) != 18:
                continue
            year = int(cardno[6:14])
            if 20030525 <= year <= 20130525:
                price = float(model.price)
                count += 1
                sum += price
        if count == 0:
            average = 0
        else:
            average = sum/count
        print(s_day, e_day,count,sum,average)



    def average_cal_all(self, s_day, e_day):
        result_model_list = self.get_data(s_day, e_day)
        sum = 0
        count = 0

        # 420984199010083651
        for model in result_model_list:
            cardno = model.cardno
            price = float(model.price)
            count += 1
            sum += price
        if count == 0:
            average = 0
        else:
            average = sum/count
        print(s_day, e_day, count, sum, average)
        pass


def test_Flight_child_price():
    o_Flight_seat = Flight_child_price()
    result = o_Flight_seat.average_cal("20140601", "20140701")
    result = o_Flight_seat.average_cal("20140701", "20140801")
    result = o_Flight_seat.average_cal("20140801", "20140901")
    result = o_Flight_seat.average_cal("20140601", "20140901")

    result = o_Flight_seat.average_cal_all("20140601", "20140701")
    result = o_Flight_seat.average_cal_all("20140701", "20140801")
    result = o_Flight_seat.average_cal_all("20140801", "20140901")
    result = o_Flight_seat.average_cal_all("20140601", "20140901")

if __name__ == "__main__":

    # test_Flight_seat()
    test_Flight_child_price()
    pass