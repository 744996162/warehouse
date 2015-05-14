__author__ = 'Administrator'
import datetime
from dao.source_dao import QueryOrdersDao
from dao.source_dao import QueryOrdersSubDao
class GetData(object):
    def __init__(self, s_day):
        self.s_day = s_day
        self.order_tablename = "user_order"
        self.order_his_tablename = "user_order_history"
        self.order_sub_tablename = "user_sub_order"
        self.order_sub_his_tablename = "user_sub_order_history"

        pass

    def getOrder(self, out_base_path):
        o_query_order = QueryOrdersDao(tablename=self.order_tablename)
        out_file_path = o_query_order.query_result_to_txt(self.s_day, out_base_path=out_base_path)
        return out_file_path



    def getOrderHistory(self, out_base_path):
        o_query_order = QueryOrdersDao(tablename=self.order_his_tablename)
        out_file_path = o_query_order.query_result_to_txt(self.s_day, out_base_path=out_base_path)
        return out_file_path


    def getOrderSub(self, out_base_path):
        o_query_sub_order = QueryOrdersSubDao(tablename=self.order_sub_tablename)
        out_file_path = o_query_sub_order.query_result_to_txt(self.s_day, out_base_path=out_base_path)
        return out_file_path


    def getOrderSubHistory(self, out_base_path):
        o_query_sub_order = QueryOrdersSubDao(tablename=self.order_sub_his_tablename)
        out_file_path = o_query_sub_order.query_result_to_txt(self.s_day, out_base_path=out_base_path)
        return out_file_path


def insertData(datas, collection_name):
    pass


def getAllData(s_day):
    base_path = "/home/huolibi/data/gt_order_all"
    path_order = base_path + "/" + "order"
    path_order_his = base_path + "/" + "order_history"
    path_order_sub = base_path + "/" + "ordersub"
    path_order_sub_his = base_path + "/" + "ordersub_history"

    o_getData = GetData(s_day)
    o_getData.getOrder(path_order)
    o_getData.getOrderHistory(path_order_his)
    o_getData.getOrderSub(path_order_sub)
    o_getData.getOrderSubHistory(path_order_sub_his)


def main(s_day):
    getAllData(s_day)
    pass


if __name__ == "__main__":
    today = datetime.datetime.now()
    s_yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    print(s_yestoday)
    print("hello")