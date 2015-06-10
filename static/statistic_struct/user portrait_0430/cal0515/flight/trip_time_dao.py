#ecoding=utf-8
__author__ = 'Administrator'
from db import source_hbgj_mysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter

error_out = open("data/error.data", "a")

class TripTime():
    def __init__(self):
        self.orderid = ""
        self.departtime = ""
        self.arrtime = ""

    def setValues(self, valueList):
        self.orderid = str(valueList[0])
        self.departtime = str(valueList[1])
        self.arrtime = str(valueList[2])

    def getTimeFrameMinute(self):
        if (len(self.departtime) != 5) or (len(self.arrtime) != 5):
            # print(self.departtime, self.arrtime)
            # return 0
            pass
        # else:
        depart_h = int(self.departtime[0:2])
        depart_m = int(self.departtime[3:5])
        depart_minute = depart_h*60 + depart_m

        arrive_h = int(self.arrtime[0:2])
        arrive_m = int(self.arrtime[3:5])
        arrive_minute = arrive_h*60 + arrive_m
            # print(depart_minute,arrive_minute)
        if arrive_minute < depart_minute:
            arrive_minute += 1440
            diff_minute = arrive_minute - depart_minute
        else:
            diff_minute = arrive_minute - depart_minute
        # print(diff_minute)
        # if diff_minute > 1400:
            # print(self.departtime, self.arrtime, diff_minute)

        if diff_minute < 10:
            print(str(self.orderid), str(self.departtime), str(self.arrtime),diff_minute)
            # error_out.write(str(self.orderid) + "\t" + str(self.departtime) + "\t" + str(self.arrtime) + "\n")
        return diff_minute


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


class TripTimeDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = TripTime):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_time(self):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select TICKET_ORDERDETAIL.ORDERID,DEPTIME,ARRTIME " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')>='20140101' " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150101'  "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list



def main_hb_trip_time():
    out_file1 = open("data/trip_time_detail_new.data", "a")
    # out_file2 = open("data/trip_time_result.data", "a")

    o_go_times = TripTimeDao()
    result_model_list = o_go_times.get_time()
    # departtime_list = [result_model.departtime for result_model in result_model_list]
    # arrivetime_list = [result_model.arrtime for result_model in result_model_list]
    diff_list = [result_model.getTimeFrameMinute() for result_model in result_model_list]
    print(len(diff_list))

    value_list = []

    for key, value in Counter(diff_list).items():
        out_file1.write(str(key) + "\t" + str(value) + "\n")
        value_list.append(value)

    # for key,value in Counter(value_list).items():
    #     out_file2.write(str(key) + "\t" + str(value) + "\n")
    # pass


if __name__ == "__main__":
    main_hb_trip_time()

    pass