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


class QueryResultDao_nfields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')

    def get_users(self,sql_str=""):
        if sql_str=="":
            # sql_str="select A.uid,A.phoneid,A.outpayprice,A.contactphone, " \
            #     "B.orderid,B.depcode,B.arrcode,B.basecabin,B.passengeridtype,B.passengeridcardno " \
            #     "from TICKET_ORDER A " \
            #     "join TICKET_ORDERDETAIL B " \
            #     "on A.ORDERID=B.ORDERID " \
            #     "where DATE_FORMAT(A.CREATETIME,'%%Y%%m%%d')>=%s " \
            #      "and A.ORDERSTATUE NOT in (2,12,21,51,75) " \
            #     "AND (B.DEPCODE='PVG' OR B.DEPCODE='SHA' OR B.ARRCODE='PVG' OR  B.ARRCODE='SHA') " \
            #     ""   % "20140101"
            sql_str="SELECT orderid,phoneid,extdata,createtime FROM gift_order WHERE TYPE = 16 "

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gift_order()
            user.orderid=row['orderid']
            user.phoneid=row['phoneid']
            user.extdata=row['extdata']
            user.createtime=row['createtime']
            users.append(user)
        return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'w')
        for row in results_model_fields:
            # try:
                out_str1=str(row.orderid)+"\t"+str(row.phoneid)+"\t"+row.extdata+"\t"+str(row.createtime)
                result_output.write(out_str1+'\n')
            # except Exception as e:
            #     print(e)
        return result_out_path
        pass


def test_nfields():
    test1=QueryResultDao_nfields()
    results=test1.get_users()
    # results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    # print(results)
    t=test1.query_result_to_txt(results,'data/gift_order_0126.txt')
    print(t)

if __name__ == '__main__':
    test_nfields()
    # date_cal()
    # text_change()