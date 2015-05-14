#coding=utf-8
__author__ = 'Administrator'

from source_mysql import *
import sys
import datetime
import hbgj_model_ticket_orderdetail
sys.path.append('..')
from conf import *


class QueryResultDao_2fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self):

        # sql_os= "SELECT count(DISTINCT PHONEID) new_consumers, " \
        #         "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) new_consumers_ios " \
        #         "from ( " \
        #         "SELECT createtime,phoneid,p " \
        #         "from gift_order " \
        #         "where PRODUCTID=12 " \
        #         "and DATE_FORMAT(createtime,'%%Y%%m%%d')= %s " \
        #         "UNION " \
        #         "SELECT createtime,phoneid,p " \
        #         "from TICKET_ORDER " \
        #         "where ORDERSTATUE not in (2,12,21,51,75) " \
        #         "and DATE_FORMAT(createtime,'%%Y%%m%%d')= %s "\
        #         ") as A " \
        #         "where PHONEID not in " \
        #         "( " \
        #         "SELECT phoneid " \
        #         "from gift_order " \
        #         "where PRODUCTID=12 " \
        #         "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s " \
        #         "UNION " \
        #         "SELECT phoneid " \
        #         "from TICKET_ORDER " \
        #         "where ORDERSTATUE not in (2,12,21,51,75) " \
        #         "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s " \
        #         ") " %(date_str,date_str,date_str,date_str)

        sql_str="SELECT  orderid id,BIRTHDAY " \
        "from TICKET_ORDERDETAIL " \
        "where  ORDERID in " \
        "( " \
        "select ORDERID " \
        "from TICKET_ORDER " \
        "where " \
        "ORDERSTATUE not in (2,12,21,51,75)" \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<=%s " \
        ") "   %("20140101","20141228")


        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_ticket_orderdetail.Model_2fields()
            user.id = row['id']
            user.birthday=row['BIRTHDAY']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_2fields,result_out_path="result1.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_2fields:
            out_str=str(row.id)+","+str(row.birthday)
            result_output.write(out_str+'\n')
        pass

class QueryResultDao_6fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            sql_str="SELECT  orderid id,BIRTHDAY,PASSENGERIDCARDNO,BASECABIN,OUTPAYPRICE,DISCOUNT " \
        "from TICKET_ORDERDETAIL " \
        "where  ORDERID in " \
        "( " \
        "select ORDERID " \
        "from TICKET_ORDER " \
        "where " \
        "ORDERSTATUE not in (2,12,21,51,75)" \
        "and p not like '%%ios%%' " \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<=%s " \
        ") "   %("20140101","20141231")

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_ticket_orderdetail.Model_6fields()
            user.id = row['id']
            user.birthday=row['BIRTHDAY']
            user.passengeridcardno=row['PASSENGERIDCARDNO']
            user.basecabin=row['BASECABIN']
            user.outpayprice=row['OUTPAYPRICE']
            user.discount=row['DISCOUNT']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_6fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_6fields:
            try:
                out_str=str(row.id)+"\t"+str(row.birthday)+"\t"+str(row.passengeridcardno)+"\t"+str(row.basecabin)+"\t"+str(row.outpayprice)+"\t"+str(row.discount)
                result_output.write(out_str+'\n')
            except Exception as e:
                print(row.id,e)
        pass

class QueryResultDao_8fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            sql_str="SELECT  orderid id,BIRTHDAY,PASSENGERIDCARDNO,BASECABIN,OUTPAYPRICE,DISCOUNT,DEPCODE,ARRCODE " \
        "from TICKET_ORDERDETAIL " \
        "where  ORDERID in " \
        "( " \
        "select ORDERID " \
        "from TICKET_ORDER " \
        "where " \
        "ORDERSTATUE not in (2,12,21,51,75)" \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
        "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<=%s " \
        ") "   %("20140101","20141231")

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_model_ticket_orderdetail.Model_8fields()
            user.id = row['id']
            user.birthday=row['BIRTHDAY']
            user.passengeridcardno=row['PASSENGERIDCARDNO']
            user.basecabin=row['BASECABIN']
            user.outpayprice=row['OUTPAYPRICE']
            user.discount=row['DISCOUNT']
            user.depcode = row['DEPCODE']
            user.arrcode = row['ARRCODE']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_8fields,result_out_path="data0303/result1.txt"):
        result_output=open(result_out_path,'a')
        for row in results_model_8fields:
            try:
                out_str=str(row.id)+"\t"+str(row.birthday)+"\t"+str(row.passengeridcardno)+"\t"+str(row.basecabin)+"\t"+str(row.outpayprice)+"\t"+str(row.discount)+"\t"+str(row.depcode)+"\t"+str(row.arrcode)
                result_output.write(out_str+'\n')
            except Exception as e:
                print(row.id,e)
        pass

def test_2fields():
    test1=QueryResultDao_2fields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results)

def test_6fields():
    test1=QueryResultDao_6fields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results,'data/ticket_orderdetail_android.txt')


def test_8fields():
    test1=QueryResultDao_8fields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    test1.query_result_to_txt(results,'data0303/ticket_orderdetail_all.txt')


if __name__ == '__main__':
    # test_6fields()

    test_8fields()
    # date_cal()
    # text_change()