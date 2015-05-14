#coding=utf-8
__author__ = 'Administrator'

from source_mysql import *
import sys
import datetime
import hbgj_model_ticket
sys.path.append('..')
from conf import *

class QueryResultDao_nfields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            sql_str="select user_id,depart_city,arrive_city,mobile,cabin,cert_no,cert_type  " \
                    "from checkin  " \
                    " where DATE_FORMAT(create_date,'%%Y%%m%%d')>=%s " \
                    "and (depart_city='PVG' or depart_city='SHA' or arrive_city='PVG' or arrive_city='SHA') "  % "20140101"

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_ticket.Model_check_in()

            user.user_id=row['user_id']
            user.depart_city=row['depart_city']
            user.arrive_city=row['arrive_city']
            user.mobile=row['mobile']
            user.cabin=row['cabin']
            user.cert_no=row['cert_no']
            user.cert_type=row['cert_type']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result_checkin.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_fields:
            try:
                out_str1=str(row.user_id)+"\t"+str(row.depart_city)+"\t"+str(row.arrive_city)+"\t"+str(row.mobile)
                out_str2=str(row.cabin)+"\t"+str(row.cert_no)+"\t"+str(row.cert_type)
                out_str=out_str1+"\t"+out_str2
                result_output.write(out_str+'\n')
            except Exception as e:
                print(e)
        pass

def test_2fields():
    test1=QueryResultDao_nfields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results)

def test_nfields():
    test1=QueryResultDao_nfields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results,'data/checkin_result.txt')

if __name__ == '__main__':
    test_nfields()
    # date_cal()
    # text_change()