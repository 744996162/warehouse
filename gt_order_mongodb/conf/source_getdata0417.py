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
import model

class GtOrderDao(Mysql):
    def __init__(self, dbtype="local"):
        Mysql.__init__(self, dbtype=dbtype)

    def get_orders(self, sql, model=model.Model_Order):
        results = self.get_all(sql)
        model_list = []

        if not results:
            return []
        for row in results:
            o_model = model()
            o_model.setVale(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]))
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
            o_model = model()
            o_model.order_id = str(row[0])
            o_model.uid = str(row[1])
            o_model.account = str(row[2])
            o_model.p_info = str(row[3])
            o_model.depart_date = str(row[4])
            o_model.train_no = str(row[5])
            o_model.depart_name = str(row[6])
            o_model.arrive_name = str(row[7])
            o_model.name = str(row[8])
            o_model.card_type = str(row[9])
            o_model.card_no = str(row[10])
            o_model.phone = str(row[11])
            o_model.seat_name = str(row[12])
            o_model.ticket_type = str(row[13])
            o_model.status = str(row[14])
            o_model.price = str(row[15])
            o_model.create_time = str(row[16])

            model_list.append(o_model)
        return model_list

class QueryOrdersDao(GtOrderDao):
    def __init__(self, dbtype="gtgj89"):
        GtOrderDao.__init__(self,dbtype=dbtype)
        self.tablename = 'user_order_history'
        self.out_base_path = '/home/huolibi/data/gt_order_all/order/'

    def get_orders(self, start_day, end_day=""):
        if start_day == end_day or end_day == "":
            sql = "select uid, p_info, account, order_date, i_status, depart_date, depart_name, arrive_name, ticket_count, train_no,amount,create_time " \
              "from " + self.tablename + " " \
              "where DATE_FORMAT(create_time,'%%Y%%m%%d')='%s' " % start_day
        else:
            sql = "select uid, p_info, account, order_date, i_status, depart_date, depart_name, arrive_name, ticket_count, train_no,amount,create_time " \
                  "from " + self.tablename + " " \
                  "where DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s' " \
                  "and DATE_FORMAT(create_time,'%%Y%%m%%d')< '%s' " % (start_day, end_day)

        print(sql)
        model_result = super(QueryOrdersDao, self).get_orders(sql)
        return model_result


    def query_result_to_txt(self, start_day, end_day=""):
        out_file_name = start_day + "_" + end_day
        result_out_path = self.out_base_path + self.tablename + "_" + out_file_name
        result_output=open(result_out_path, 'a')
        model_result = self.get_orders(start_day, end_day)
        for row in model_result:
            out_str = row.getString()
            result_output.write(out_str+'\n')
        return result_out_path

class QueryOrdersSubDao(GtOrderSubDao):
    def __init__(self, dbtype="gtgj89"):
        GtOrderSubDao.__init__(self, dbtype=dbtype)
        self.tablename = 'user_sub_order'
        self.out_base_path = '/home/huolibi/data/gt_order_all/ordersub/'

    def get_orders(self, start_day, end_day=""):
        if start_day == end_day or end_day == "":
            sql = "select order_id,uid,account,p_info,depart_date,train_no,depart_name,arrive_name,name,card_type,card_no,phone,seat_name,ticket_type,status,price,create_time " \
              "from " + self.tablename + " " \
              "where DATE_FORMAT(create_time,'%%Y%%m%%d')='%s' "  % start_day
        else:
            sql = "select order_id,uid,account,p_info,depart_date,train_no,depart_name,arrive_name,name,card_type,card_no,phone,seat_name,ticket_type,status,price,create_time " \
                  "from " + self.tablename + " " \
                  "where DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s' " \
                  "and DATE_FORMAT(create_time,'%%Y%%m%%d')< '%s' " % (start_day, end_day)

        print(sql)
        model_result = super(QueryOrdersSubDao, self).get_orders(sql)
        return model_result

    def query_result_to_txt(self, start_day, end_day=""):
        out_file_name = start_day + "_" + end_day
        result_out_path = self.out_base_path + self.tablename + "_" + out_file_name
        result_output=open(result_out_path, 'a')
        model_result = self.get_orders(start_day, end_day)
        for row in model_result:
            out_str = row.getString()
            result_output.write(out_str+'\n')
        return result_out_path



def getdata(start_date="20130701", end_date="20140101",deata=10):
    date_list = []

    s_day = parse(start_date)
    end_day = parse(end_date)
    days = (end_day-s_day).days
    print(s_day, end_day,days)
    for i in range(0, days,deata):
        day1 = (s_day+datetime.timedelta(days=i)).strftime('%Y%m%d')
        day2 = (s_day+datetime.timedelta(days=i+deata)).strftime('%Y%m%d')
        date_list.append([day1,day2])
    return date_list


def test1():
    t = QueryOrdersDao()
    # tablename = t.tablename

    sql ="select uid, p_info, account, order_date, i_status, depart_date, depart_name, arrive_name, ticket_count, train_no,amount,create_time from user_order  "
    # o_object = GtOrderDao()

    results = t.query_result_to_txt("20140101", "20150101")
    print(results)


def OrderOutTest():
    date_list = getdata(start_date="20150105", end_date="20140215", deata=3)
    for date_arr in date_list:
        s_day = date_arr[0]
        end_day = date_arr[1]
        print(s_day,end_day)
        o_orderDao = QueryOrdersDao()
        results = o_orderDao.query_result_to_txt(s_day, end_day)

def OrderSubOutTest():
    date_list = getdata(start_date="20150214", end_date="20150315", deata=3)
    for date_arr in date_list:
        s_day = date_arr[0]
        end_day = date_arr[1]
        print(s_day, end_day)
        o_orderSubDao = QueryOrdersSubDao()
        results = o_orderSubDao.query_result_to_txt(s_day, end_day)

if __name__ == '__main__':
    #o_orderSubDao = QueryOrdersSubDao()
    #results = o_orderSubDao.query_result_to_txt("20130715", "20150101")
    # OrderOutTest()
    OrderSubOutTest()

    pass
