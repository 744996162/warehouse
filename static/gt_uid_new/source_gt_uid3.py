#ecoding=utf-8
__author__ = 'Administrator'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from source_mysql import *
import sys
import datetime
import model
sys.path.append('..')
from conf import *


class QueryResultDao(Mysql):
    def __init__(self):
        Mysql.__init__(self, dbtype='gtgj102')

    @staticmethod
    def getDate():
        pass

    def get_users_one(self, sql_str=""):
        if sql_str=="":
            # sql_str = "select city_code id from city_map"
            # sql_str = "SELECT DISTINCT uid id FROM user_order_history where i_status=3 "

            sql_str = "SELECT account id FROM user_order " \
                      "where i_status=3 " \
                      "and DATE_FORMAT(create_time,'%Y%m%d')>='20140101' " \
                      "and uid='20c27fb772000217b' "

            # sql_str ="SELECT account id FROM user_order " \
            #          "where uid='20c27fb772000217b' " \
            #          "and i_status=3 " \
            #           "LIMIT 2920 "

        result = self.get_all(sql_str)
        users = []
        if not result:
            return False
        for row in result:
            user= model.Model_gt_uid()
            user.uid=row['id']
            users.append(user)
        return users

    def get_users(self, s_day_start, s_day_end, sql_str=""):
        if sql_str=="":
            # sql_str = "select city_code id from city_map"
            # sql_str = "SELECT DISTINCT uid id FROM user_order_history where i_status=3 "
            # sql_str = "SELECT uid id FROM user_order_history " \
            #           "where i_status=3 " \
            #           "and DATE_FORMAT(create_time,'%Y%m%d')>='20140901' " \
            #           "and DATE_FORMAT(create_time,'%Y%m%d')<'20141001'"
            sql_str = "SELECT account id FROM user_order_history " \
                      "where i_status=3 " \
                      "and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s " \
                      "and DATE_FORMAT(create_time,'%%Y%%m%%d')<%s " \
                      "and uid='20c27fb772000217b' " % (s_day_start, s_day_end)

        result = self.get_all(sql_str)
        users = []
        if not result:
            return False
        for row in result:
            user= model.Model_gt_uid()
            user.uid=row['id']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields, result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'w')
        for row in results_model_fields:
            # try:
                out_str1=str(row.uid)
                result_output.write(out_str1+'\n')
            # except Exception as e:
            #     print(e)
        return result_out_path
        pass

def getdate(month):
    if month < 10:
        s_day_start = "20140"+str(month)+"01"
        s_day_end = "20140"+str(month+1)+"01"
    else:   #month >= 10:
        s_day_start = "2014"+str(month)+"01"
        s_day_end = "2014"+str(month+1)+"01"

    return s_day_start, s_day_end


def testQueryResultDao(s_day_start, s_day_end):

    test1=QueryResultDao()
    results=test1.get_users(s_day_start, s_day_end)
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    file_path = "data0319/"+str(s_day_start)+".txt"
    t = test1.query_result_to_txt(results, file_path)
    print(t)

def testQueryResultDao_one():

    test1=QueryResultDao()
    results=test1.get_users_one()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    file_path = "data0319/ios_break/102his3_1217.txt"
    t = test1.query_result_to_txt(results, file_path)
    print(t)


if __name__ == '__main__':
    testQueryResultDao_one()
    # testQueryResultDao_3fields()
    # testQueryResultDao(t1,t2)
    # for i in range(5, 9):
    #     t1, t2 = getdate(i)
    #     testQueryResultDao(t1,t2)
    #     print(t1, t2)
    # date_cal()
    # text_change()