#coding=utf-8
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
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            # sql_str = "select city_code id from city_map"
            # sql_str =
            sql_str = "SELECT uid id FROM user_order_history_20150104 " \
                      "where i_status=3 " \
                      "and DATE_FORMAT(create_time,'%Y%m%d')>='20141201' " \
                      "and DATE_FORMAT(create_time,'%Y%m%d')<'20150101' "

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gt_uid()
            user.uid=row['id']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'w')
        for row in results_model_fields:
            # try:
                out_str1=str(row.uid)
                result_output.write(out_str1+'\n')
            # except Exception as e:
            #     print(e)
        return result_out_path
        pass

class QueryResultDao_3fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and  DATE_FORMAT(create_time,'%Y%m%d')='20141201'"

            sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and DATE_FORMAT(create_time,'%Y%m%d')>='20150301' "


        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gt_3fields()
            user.uid=row['uid']
            user.p_info=row['p_info']
            user.create_time=row['s_day']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'w')
        for row in results_model_fields:
            # try:
                out_str1=str(row.uid)+"\t"+str(row.p_info)+"\t"+str(row.create_time)
                result_output.write(out_str1+'\n')
            # except Exception as e:
            #     print(e)
        return result_out_path
        pass


def testQueryResultDao():
    test1=QueryResultDao()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    t=test1.query_result_to_txt(results, 'data/89_201412.txt')
    print(t)

def testQueryResultDao_3fields():
    o_test=QueryResultDao_3fields()
    results=o_test.get_users()
    t=o_test.query_result_to_txt(results,'data/result0309.txt')
    print(t)

if __name__ == '__main__':
    testQueryResultDao()

    # date_cal()
    # text_change()