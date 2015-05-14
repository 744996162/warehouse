#coding=utf-8
__author__ = 'Administrator'

from source_mysql import *
import sys
import datetime

sys.path.append('..')
from conf import *

import gtgj_model_1fields


class QueryResultDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self):#
        # sql_str="SELECT  orderid id,BIRTHDAY " \
        # "from TICKET_ORDERDETAIL " \
        # "where  ORDERID in " \
        # "( " \
        # "select ORDERID " \
        # "from TICKET_ORDER " \
        # "where " \
        # "ORDERSTATUE not in (2,12,21,51,75)" \
        # "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
        # "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<=%s " \
        # ") "   %("20140101","20141228")

        sql_str="select userid " \
        "from user_order " \
        "where i_status=3  " \
        "and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s " \
        "and userid is not NULL"  %("20141229")

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= gtgj_model_1fields.Model_1fields()
            user.userid = row['userid']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_1fields,result_out_path="result_gt_userid.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_1fields:
            out_str=str(row.userid)
            result_output.write(out_str+'\n')
        pass

def test():
    test1=QueryResultDao()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results)


# def date_cal():
#
#     test1=QueryResultDao()
#     results=test1.get_users()
#
#     for i in range(730):
#         try:
#             result_output=open("out.txt",'a')
#             date2=base_date+datetime.timedelta(days=i)
#             date2_str=date2.strftime('%Y%m%d')
#             # print(base_date,type(base_date))
#             results=test1.get_users(date2_str)
#             for t in results:
#                 out_str=t.s_day+","+str(t.new_consumers)+","+str(t.new_consumers_ios)+","+str(t.new_consumers_android)
#                 result_output.write(out_str+'\n')
#                 print(out_str,datetime.datetime.now())
#             result_output.close()
#         except Exception as e:
#             print e
#         # result_output.write(+'\n')
#         # print(date2_str,type(date2_str))
#     pass


def text_change():
    # 整理输出数据
    fr_in=open("out.txt")
    result_output=open("out_new.txt",'a')
    for line in fr_in.readlines():
        stringArr=line.strip().split(",")
        date=stringArr[0]
        total=stringArr[1]
        ios=stringArr[2]
        android=stringArr[3]
        new_date=date[0:4]+"-"+date[4:6]+"-"+date[6:8]
        out_str=new_date+","+total+","+ios+","+android
        result_output.write(out_str+'\n')
        print(new_date,type(new_date),total,ios,android,type(total))
    pass

if __name__ == '__main__':
    test()
    # date_cal()
    # text_change()