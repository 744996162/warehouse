#coding=utf-8
__author__ = 'zhangchao'
import sys
import logging
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

from source_mysql import *
import model
from conf import *
from tools import *

#First step: save everyday uid in text file,the filename is date,such as 20150309.
#2打开his UID文件和每天更新的UID，去重，得到每天消费用户数


class QueryResultDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self,s_day,sql_str=""):
        if sql_str=="":
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and  DATE_FORMAT(create_time,'%Y%m%d')='20141201'"
            #sql_str = "SELECT uid FROM user_order where i_status=3 and DATE_FORMAT(create_time,'%Y%m%d')>='20150301' "
            sql_str = "SELECT uid FROM user_order where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')=%s " %s_day
            logging.debug(sql_str)
            print(sql_str)
        # result=self.get_all(sql_str)
        # users=[]
        # if not result:
        #     return False
        # for row in result:
        #     user= model.Model_gt_uid()
        #     user.uid=row['uid']
        #     users.append(user)
        # return users

    def query_result_to_txt(self,results_model_fields,result_out_path="data/result1.txt"):
        result_output=open(result_out_path,'w')
        for row in results_model_fields:
            # try:
                result_output.write(str(row.uid)+'\n')
            # except Exception as e:
            #     print(e)
        return result_out_path
        pass


def testQueryResultDao():
    o_test=QueryResultDao()
    results=o_test.get_users("20150309")
    # t=o_test.query_result_to_txt(results,'data/result0309.txt')
    # print(t)




def gtGetToday(date=datetime.datetime.now()):
    date2=date+datetime.timedelta(days=-1)
    s_date2=date2.strftime('%Y%m%d')
    return s_date2
    pass

def main():
    # his_text = open("G:/data/uid/result_his_0308")
    his_list = file_search.get_all_file("G:/data/uid/")

    pass

if __name__ == '__main__':
    # testQueryResultDao()
    logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )
    t=gtGetToday()
    logging.debug(t)