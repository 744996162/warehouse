#coding=utf-8
__author__ = 'Administrator'

from source_mysql import *
import sys
import datetime
sys.path.append('..')
from conf import *
import hbgj_model_checkin

class QueryResultDao_4fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            sql_str="SELECT user_id id,airline_code,cabin,cert_no " \
        "from checkin " \
        "where DATE_FORMAT(create_date,'%%Y%%m%%d')>=%s " \
        "and DATE_FORMAT(create_date,'%%Y%%m%%d')<=%s" %("20140101","20141228")


        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_checkin.Model_4fields()
            user.id = row['id']
            user.airline_code=row['airline_code']
            user.cabin=row['cabin']
            user.cert_no=row['cert_no']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_4fields,result_out_path="checkin/result1.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_4fields:
            try:
                out_str=str(row.id)+"\t"+str(row.airline_code)+"\t"+str(row.cabin)+"\t"+str(row.cert_no)
                result_output.write(out_str+'\n')
            except Exception as e:
                print(row.id,e)
        pass



def test_4fields():
    test1=QueryResultDao_4fields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results,'checkin/checkin_all.txt')

if __name__ == '__main__':
    test_4fields()
    # date_cal()
    # text_change()