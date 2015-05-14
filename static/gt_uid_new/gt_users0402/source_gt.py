__author__ = 'Administrator'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from source_mysql import *
from model import model

class GtBaseDao(Mysql):
    def __init__(self, dbtype="gtgj89"):
        Mysql.__init__(self, dbtype=dbtype)

    def get_users(self, s_day, model=model.OrderModel, sql=""):
        arg = [s_day]
        result = self.get_all(sql, arg)
        # logging.DEBUG(str(sql))
        users_list = []
        if not result:
            return  False
        for row in result:
            o_user_model = model()
            o_user_model.setValue(row[0], int(row[1]), int(row[2]), int(row[3]))
            users_list.append(o_user_model)
        return users_list


class QueryResultDao(Mysql):
    def __init__(self):
        Mysql.__init__(self, dbtype='gtgj89')
        self.dbname = "user_order"

    def get_users(self, s_day_start, s_day_end, sql_str=""):
        file_out_path = "G:/data/gt0402/uid201502new"
        file_out = open(file_out_path, "a")
        if sql_str == "":
            sql_str = "SELECT uid FROM " + self.dbname + " " \
                      "where i_status=3 " \
                      "and DATE_FORMAT(create_time,'%%Y%%m%%d')>='%s' " \
                      "and DATE_FORMAT(create_time,'%%Y%%m%%d')<'%s' " % (s_day_start, s_day_end)
            result = self.get_all(sql_str)
            print(sql_str)
            # users=[]
            if not result:
                return False
            for row in result:
                try:
                    t = row['uid']
                    file_out.write(t+"\n")
                except Exception as e:
                    print(e)

if __name__ == "__main__":

    o_Query = QueryResultDao()
    o_Query.get_users("20150201", "20150301")
    pass



