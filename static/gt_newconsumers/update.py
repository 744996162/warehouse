#coding=utf-8
__author__ = 'zhangchao'
import sys
import logging
import datetime
reload(sys)
sys.setdefaultencoding("utf-8")

from source_mysql import *
import model
from conf import *
# from tools import *
import tools

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



def test():
    # print("test")
    logging.debug("log 测试")
    pass

def getYestoday(date=datetime.datetime.now()):
    date2=date+datetime.timedelta(days=-1)
    s_date2=date2.strftime('%Y%m%d')
    return s_date2
    pass

def getYestodayNewConsumers(s_day=getYestoday()):
    s_his_uid_filename = "result_his_0308"
    s_folder = "data/"
    s_yestoday = s_day

    file_path_list = tools.file_search.getAllFile(s_folder)
    file_path_his_everyday_list = []
    for file_path in file_path_list:
        if s_his_uid_filename in file_path:
            pass
        elif s_yestoday in file_path:
            pass
        else:
            file_path_his_everyday_list.append(file_path)

    logging.debug(file_path_list)
    logging.debug(file_path_his_everyday_list)
    str_his_file_path = s_folder + s_his_uid_filename
    logging.debug(str_his_file_path)

    list_his_uid_0308 = tools.getTxtList(str_his_file_path)

    list_his_uid_everyday = []
    for str_file_path in file_path_his_everyday_list:
        uid_temp = tools.getTxtList(str_file_path)
        list_his_uid_everyday = tools.listMerge(list_his_uid_everyday,uid_temp)
        pass

    list_his_uid = tools.listMerge(list_his_uid_0308,list_his_uid_everyday)

    i_his_uid_num=len(list_his_uid)

    str_yestoday_ios_path = s_folder + s_yestoday + "_ios"
    str_yestoday_android_path = s_folder + s_yestoday + "_android"

    list_yestoday_uid_ios = tools.getTxtList(str_yestoday_ios_path)
    list_yestoday_uid_android = tools.getTxtList(str_yestoday_android_path)

    i_yestoday_uid_ios_num = len(list_yestoday_uid_ios)
    i_i_yestoday_uid_android_num = len(list_yestoday_uid_android)

    logging.info(s_yestoday)
    logging.info(s_yestoday + "\t" + "ios_consumers" + "\t" + str(i_yestoday_uid_ios_num))
    logging.info(s_yestoday + "\t" + "android_consumers" + "\t" + str(i_i_yestoday_uid_android_num))

    list_all_ios = tools.listMerge(list_his_uid,list_yestoday_uid_ios)
    list_all_android = tools.listMerge(list_his_uid,list_yestoday_uid_android)

    i_yestoday_ios_newconsumers_count = len(list_all_ios) - i_his_uid_num
    i_yestoday_android_newconsumers_count = len(list_all_android) - i_his_uid_num

    logging.info(s_yestoday + "\t" + "ios_new_consumers" +"\t" + str(i_yestoday_ios_newconsumers_count))
    logging.info(s_yestoday + "\t" + "android_new_consumers" +"\t" + str(i_yestoday_android_newconsumers_count))
    return i_yestoday_ios_newconsumers_count,i_yestoday_android_newconsumers_count
    pass

def log_test():
    # import logging
    import logging.handlers
    LOG_FILE = "../log.log"
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 20*1024*1024, backupCount = 10) # 实例化handler
    fmt = "%(asctime)s \t %(name)s \t %(levelname)s \t %(message)s \t [%(filename)s:%(lineno)s]"
    formatter = logging.Formatter(fmt)   # 实例化formatter
    handler.setFormatter(formatter)      # 为handler添加formatter

    logger = logging.getLogger('xzs')    # 获取名为xzs的logger
    logger.addHandler(handler)           # 为logger添加handler
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s",
    filename='myapp.log',
    filemode='a'
    )

    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

if __name__ == '__main__':
    log_test()
    getYestodayNewConsumers()
