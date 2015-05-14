#coding=utf-8
__author__ = 'Administrator'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from source_mysql import *
import sys
import datetime
import logging
import model
from tools import *
sys.path.append('..')
from conf import *

class QueryResultDao_2fields(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')
        # self._s_day = getYestoday()
        self._s_day = "20150309"

    def get_users(self,s_day, sql_str=""):
        if sql_str=="":
            # sql_str = "SELECT uid,p_info,DATE_FORMAT(create_time,'%Y%m%d') s_day FROM user_order where i_status=3 and  DATE_FORMAT(create_time,'%Y%m%d')='20141201'"
            sql_str = "SELECT uid,p_info FROM user_order where i_status=3 " \
                      "and DATE_FORMAT(create_time,'%%Y%%m%%d')=%s " % s_day

        result=self.get_all(sql_str)
        users=[]
        if not result:
            return False
        for row in result:
            user= model.Model_gt_2fields()
            user.uid=row['uid']
            user.p_info=row['p_info']
            users.append(user)
        return users

    def query_result_to_text(self,_results_model_fields,_s_result_folder="data/"):

        # s_result_output_ios_path = _s_result_folder + self._s_day + "_ios"
        # s_result_output_android_path = _s_result_folder + self._s_day + "_android"
        s_result_output_ios_path = "20150309_ios"
        s_result_output_android_path = "20150309_android"
        file_result_output_ios = open(s_result_output_ios_path,"a")
        file_result_output_android = open(s_result_output_android_path,"a")

        for row in _results_model_fields:
            uid = str(row.uid)
            p_info =  str(row.p_info)

            if "ios" in p_info:
                os_state = "ios"
                file_result_output_ios.write(uid+"\n")
            else:
                os_state = "android"
                file_result_output_android.write(uid+"\n")
        return s_result_output_ios_path,file_result_output_android

def getYestodayTxt():
    o_QueryResult=QueryResultDao_2fields()
    # s_day = o_QueryResult._s_day
    s_day = "20150309"
    results=o_QueryResult.get_users(s_day)
    path1,path2=o_QueryResult.query_result_to_text(results)
    logging.debug(path1,path2)

if __name__ == '__main__':
    getYestodayTxt()
