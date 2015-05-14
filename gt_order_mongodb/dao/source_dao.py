#ecoding=utf-8
__author__ = 'Administrator'
import sys
reload(sys)
import datetime
from dateutil.parser import parse
sys.setdefaultencoding('utf-8')
from source_mysql import *
sys.path.append('..')
from conf import *
from domain import model
import logging


class GtOrderDao(Mysql):
    def __init__(self, dbtype="local"):
        Mysql.__init__(self, dbtype=dbtype)

    def get_orders(self, sql, model=model.Model_Order):
        results = self.get_all(sql)
        model_list = []

        if not results:
            return []
        for row in results:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model()
            o_model.setValue(value_list)
            model_list.append(o_model)
        return model_list

class GtOrderSubDao(Mysql):
    def __init__(self, dbtype="local"):
        Mysql.__init__(self, dbtype=dbtype)

    def get_orders(self, sql, model=model.Model_OrderSub):
        results = self.get_all(sql)
        model_list = []

        if not results:
            return []

        for row in results:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model()
            o_model.setVale(value_list)
            model_list.append(o_model)
        return model_list


class QueryOrdersDao(object):
    def __init__(self, dbtype="gtgj89", tablename="user_order", DaoClass=GtOrderDao):
        self.dbdao =DaoClass(dbtype=dbtype)
        # self.tablename = 'user_order_history'
        self.tablename = tablename


    def get_orders(self, start_day, end_day=""):
        if start_day == end_day or end_day == "":
            sql = "select uid, p_info, account, order_date, i_status, depart_date, depart_name, arrive_name, ticket_count, train_no, amount, create_time, pay_method, pay_time " \
              "from " + self.tablename + " " \
              "where DATE_FORMAT(create_time,'%%Y%%m%%d')='%s' LIMIT 10 " % start_day
        else:
            sql = "select uid, p_info, account, order_date, i_status, depart_date, depart_name, arrive_name, ticket_count, train_no,amount,create_time, pay_method, pay_time " \
                  "from " + self.tablename + " " \
                  "where DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s' " \
                  "and DATE_FORMAT(create_time,'%%Y%%m%%d')< '%s' LIMIT 10 " % (start_day, end_day)

        logging.debug(sql)
        model_result = self.dbdao.get_orders(sql)
        return model_result


    def query_result_to_txt(self, start_day, end_day="", out_base_path=""):
        if end_day == "":
            out_file_name = start_day
        else:
            out_file_name = start_day + "_" + end_day
        result_out_path = out_base_path + "/" + self.tablename + "_" + out_file_name
        result_output=open(result_out_path, 'a')
        model_result = self.get_orders(start_day, end_day)
        for row in model_result:
            out_str = row.getString()
            result_output.write(out_str+'\n')
        return result_out_path

class QueryOrdersSubDao(object):
    def __init__(self, dbtype="gtgj89", tablename="user_sub_order", DaoClass=GtOrderSubDao):
        self.dbdao = DaoClass(dbtype=dbtype)
        self.tablename = tablename

    def get_orders(self, start_day, end_day="", ):
        if start_day == end_day or end_day == "":
            sql = "select order_id,uid,account,p_info,depart_date,train_no,depart_name,arrive_name,name,card_type,card_no,phone,seat_name,ticket_type,status,price,create_time " \
              "from " + self.tablename + " " \
              "where DATE_FORMAT(create_time,'%%Y%%m%%d')='%s' LIMIT 10 "  % start_day
        else:
            sql = "select order_id,uid,account,p_info,depart_date,train_no,depart_name,arrive_name,name,card_type,card_no,phone,seat_name,ticket_type,status,price,create_time " \
                  "from " + self.tablename + " " \
                  "where DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s' " \
                  "and DATE_FORMAT(create_time,'%%Y%%m%%d')< '%s' LIMIT 10 " % (start_day, end_day)

        logging.debug(sql)
        model_result = self.dbdao.get_orders(sql)
        return model_result

    def query_result_to_txt(self, start_day, end_day="", out_base_path=""):
        if end_day == "":
            out_file_name = start_day
        else:
            out_file_name = start_day + "_" + end_day

        result_out_path = out_base_path + "/" + self.tablename + "_" + out_file_name
        result_output=open(result_out_path, 'a')
        model_result = self.get_orders(start_day, end_day)
        for row in model_result:
            out_str = row.getString()
            result_output.write(out_str+'\n')
        return result_out_path



def getdata(start_date="20130701", end_date="20140101", deata=10):
    date_list = []

    s_day = parse(start_date)
    end_day = parse(end_date)
    days = (end_day-s_day).days
    print(s_day, end_day, days)
    for i in range(0, days, deata):
        day1 = (s_day+datetime.timedelta(days=i)).strftime('%Y%m%d')
        day2 = (s_day+datetime.timedelta(days=i+deata)).strftime('%Y%m%d')
        date_list.append([day1, day2])
    return date_list


def test_order(tablename="user_order"):
    t = QueryOrdersDao(tablename=tablename)
    # results = t.query_result_to_txt("20140101", "20150518", out_base_path="G:")
    results = t.query_result_to_txt("20150312", out_base_path="G:")
    print(results)

def test_suborder(tablename="user_sub_order"):
    t = QueryOrdersSubDao(tablename=tablename)
    # results = t.query_result_to_txt("20140101", "20150518", out_base_path="G:")
    results = t.query_result_to_txt("20150312", out_base_path="G:")
    print(results)


def OrderOutTest():
    date_list = getdata(start_date="20150218", end_date="20150222", deata=1)
    for date_arr in date_list:
        s_day = date_arr[0]
        end_day = date_arr[1]
        print(s_day,end_day)
        o_orderDao = QueryOrdersDao()
        results = o_orderDao.query_result_to_txt(s_day, end_day)

def OrderSubOutTest():
    date_list = getdata(start_date="20130715", end_date="20131001", deata=10)
    for date_arr in date_list:
        s_day = date_arr[0]
        end_day = date_arr[1]
        print(s_day, end_day)
        o_orderSubDao = QueryOrdersSubDao()
        results = o_orderSubDao.query_result_to_txt(s_day, end_day)

if __name__ == '__main__':
    # o_orderSubDao = QueryOrdersSubDao()
    # results = o_orderSubDao.query_result_to_txt("20130715", "20150101")
    # test_suborder()
    # OrderOutTest()
    # test_order()
    # OrderOutTest()


    test_order(tablename="user_order")
    # test_order(tablename="user_order_history")
    test_suborder(tablename="user_sub_order")
    # test_suborder(tablename="user_sub_order_history")