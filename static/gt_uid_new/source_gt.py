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
        Mysql.__init__(self, dbtype='gtgj')

    def get_users(self, sql_str=""):
        if sql_str == "":
            # sql_str = "select city_code id from city_map"
            sql_str = "SELECT uid id FROM user_order_history where i_status=3 and　DATE_FORMAT(create_time,'%Y%m%d')>='20140101' "

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

            sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3"

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


class QueryResultDao_9fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj102')

    def get_users(self,sql_str=""):
        if sql_str=="":
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and  DATE_FORMAT(create_time,'%Y%m%d')='20141201'"
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3"
            sql_str = "SELECT uid,train_no,depart_name,arrive_name,card_type,card_no,seat_name,status,DATE_FORMAT(create_time,'%Y%m%d') s_day " \
                    "FROM user_sub_order_history_20140825 " \
                    "where status not in ('取消订单','已退票','未支付') " \
                    "and DATE_FORMAT(create_time,'%Y%m%d')='20140101' "

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gt_9fields()
            user.uid = row['uid']
            user.train_no = row['train_no']
            user.depart_name = row['depart_name']
            user.arrive_name = row['arrive_name']
            user.card_type = row['card_type']
            user.card_no = row['card_no']
            user.seat_name = row['seat_name']
            user.status = row['status']
            user.s_day = row['s_day']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="user_sub_order.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_fields:
            out_str1 = str(row.uid) + "\t" + str(row.train_no) + "\t" + str(row.depart_name) + "\t" + str(row.arrive_name) + "\t" + str(row.card_type)
            out_str2 = str(row.card_no) + "\t" + str(row.seat_name) + "\t" + str(row.status) + "\t" + str(row.s_day)
            try:
                out_str=out_str1 + "\t" + out_str2
                result_output.write(out_str+'\n')
            except Exception as e:
                print(e)
        return result_out_path


class QueryResultDao_8fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and  DATE_FORMAT(create_time,'%Y%m%d')='20141201'"
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3"
            sql_str = "SELECT train_no,depart_name,arrive_name,card_no,seat_name,status,DATE_FORMAT(create_time,'%Y%m%d') s_day " \
                    "FROM user_sub_order_history_20140825 " \
                    "where status not in ('取消订单','已退票','未支付') " \
                    "and DATE_FORMAT(create_time,'%Y%m%d')>='20140101' "

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gt_9fields()
            user.train_no = row['train_no']
            user.depart_name = row['depart_name']
            user.arrive_name = row['arrive_name']
            user.card_no = row['card_no']
            user.seat_name = row['seat_name']
            user.status = row['status']
            user.s_day = row['s_day']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="user_sub_order.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_fields:
            out_str1 = str(row.train_no) + "\t" + str(row.depart_name) + "\t" + str(row.arrive_name) + "\t" + str(row.card_type)
            out_str2 = str(row.card_no) + "\t" + str(row.seat_name) + "\t" + str(row.status) + "\t" + str(row.s_day)
            try:
                out_str=out_str1 + "\t" + out_str2
                result_output.write(out_str+'\n')
            except Exception as e:
                print(e)
        return result_out_path

def testQueryResultDao():
    test1=QueryResultDao()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    t=test1.query_result_to_txt(results, 'data/89his.txt')
    print(t)

def testQueryResultDao_3fields():
    o_test=QueryResultDao_3fields()
    results=o_test.get_users()
    t=o_test.query_result_to_txt(results,'data/result.txt')
    print(t)

def testQueryResultDao_9fields():
    o_test = QueryResultDao_9fields()
    result = o_test.get_users()
    t = o_test.query_result_to_txt(result,"data0305/user_sub_order_history_20140825.txt")
    print(t)

def testQueryResultDao_7fields():
    o_test = QueryResultDao_7fields()
    result = o_test.get_users()
    t = o_test.query_result_to_txt(result,"data0305/user_sub_order_history_20140825.txt")
    print(t)

if __name__ == '__main__':
    # testQueryResultDao_3fields()
    testQueryResultDao_9fields()
    # date_cal()
    # text_change()