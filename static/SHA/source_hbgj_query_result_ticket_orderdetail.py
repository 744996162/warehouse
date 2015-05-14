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
        #     sql_str="SELECT  orderid id,BIRTHDAY,PASSENGERIDCARDNO,BASECABIN,OUTPAYPRICE,DISCOUNT, " \
        # "from TICKET_ORDERDETAIL " \
        # "where  ORDERID in " \
        # "( " \
        # "select ORDERID " \
        # "from TICKET_ORDER " \
        # "where " \
        # "ORDERSTATUE not in (2,12,21,51,75)" \
        # "and p not like '%%ios%%' " \
        # "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
        # "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<=%s " \
        # ") "   %("20140101","20141228")
            sql_str="select A.uid,A.phoneid,A.outpayprice,A.contactphone, " \
                "B.orderid,B.depcode,B.arrcode,B.basecabin,B.passengeridtype,B.passengeridcardno " \
                "from TICKET_ORDER A " \
                "join TICKET_ORDERDETAIL B " \
                "on A.ORDERID=B.ORDERID " \
                "where DATE_FORMAT(A.CREATETIME,'%%Y%%m%%d')>=%s " \
                 "and A.ORDERSTATUE NOT in (2,12,21,51,75) " \
                "AND (B.DEPCODE='PVG' OR B.DEPCODE='SHA' OR B.ARRCODE='PVG' OR  B.ARRCODE='SHA') " \
                ""   % "20140101"

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_ticket.Model_nfields()
            user.uid=row['uid']
            user.phoneid=row['phoneid']
            user.outpayprice=row['outpayprice']
            user.contactphone=row['contactphone']
            user.orderid=row['orderid']
            user.depcode=row['depcode']
            user.arrcode=row['arrcode']
            user.basecabin=row['basecabin']
            user.passengeridtype=row['passengeridtype']
            user.passengeridcardno=row['passengeridcardno']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_fields:
            try:
                out_str1=str(row.uid)+"\t"+str(row.phoneid)+"\t"+str(row.contactphone)+"\t"+str(row.passengeridcardno)
                out_str2=str(row.passengeridtype)+"\t"+str(row.basecabin)+"\t"+str(row.depcode)+"\t"+str(row.arrcode)
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
    test1.query_result_to_txt(results,'data/ticket_order_test.txt')

if __name__ == '__main__':
    test_nfields()
    # date_cal()
    # text_change()