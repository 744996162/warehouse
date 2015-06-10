#ecoding=utf-8
__author__ = 'Administrator'
from db import source_hbgj_mysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter

class Passengeridcardno():
    def __init__(self):
        self.passengerno = ""

    def setValues(self, valueList):
        self.passengerno = str(valueList[0])


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


class GoTimesDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = Passengeridcardno):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_no(self):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select PASSENGERIDCARDNO " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')>='20140101' " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150101'   " \
            "and TICKET_ORDERDETAIL.PASSENGERTYPE='CHD' "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

class CityDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = Passengeridcardno):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_no(self):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select ARRCODE " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')>='20140101' " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150101'   " \
            "and TICKET_ORDERDETAIL.PASSENGERTYPE='CHD' "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

def main_hb_go_times():
    out_file1 = open("data/hb_go_times_child_details.data", "a")
    out_file2 = open("data/hb_child_go_times.data", "a")
    o_go_times = GoTimesDao()
    result_model_list = o_go_times.get_no()
    no_list = [result_model.passengerno for result_model in result_model_list]
    print(len(no_list))

    value_list = []

    for key, value in Counter(no_list).items():
        out_file1.write(str(key) + "\t" + str(value) + "\n")
        value_list.append(value)

    for key, value in Counter(value_list).items():
        out_file2.write(str(key) + "\t" + str(value) + "\n")
    pass


def child_gender_percent():
    file_path = "data/hb_go_times_child_details.data"
    file_in = open(file_path)

    num = 0
    male = 0
    female = 0

    for line in file_in:
        (cardno, times) = line.strip().split("\t")[0:2]
        if len(cardno) != 18:
            continue
        gender = int(cardno[-2])
        num += 1
        if gender % 2 == 1:
            male += 1
        elif gender % 2 == 0:
            female += 1
    print("num", num)
    print("male", male)
    print("female", female)


def main_hb_child_arrcode():
    out_file1 = open("data/hb_arrcode_child_details.data", "a")
    out_file2 = open("data/hb_child_arrcode.data", "a")
    o_city = CityDao()
    result_model_list = o_city.get_no()
    no_list = [result_model.passengerno for result_model in result_model_list]
    print(len(no_list))

    value_list = []

    for key, value in sorted(Counter(no_list).items(), key=lambda d: d[1], reverse=True):
        out_file1.write(str(key) + "\t" + str(value) + "\n")
        value_list.append(value)

    for key, value in sorted(Counter(value_list).items(), key=lambda d: d[1], reverse=True):
        out_file2.write(str(key) + "\t" + str(value) + "\n")
    pass

if __name__ == "__main__":
    # main_hb_go_times()
    # child_gender_percent()
    main_hb_child_arrcode()
    pass