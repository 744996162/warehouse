#ecoding=utf-8
__author__ = 'Administrator'
from db import source_hbgj_mysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter

class ConsumersId():
    def __init__(self):
        self.uid = ""

    def setValues(self, valueList):
        self.uid = str(valueList[0])


class BaseUserMysqlDao(object):
    def __init__(self, dbtype):
        self.db = source_hbgj_mysql.Mysql(dbtype=dbtype)
        print(self.db._type)

    def query_result_by_setValue(self, sql, model_class):
        result=self.db.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class ConsumerTimesDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = ConsumersId):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_uid(self, s_day, e_day):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select uid " \
            "from TICKET_ORDER  " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')>='%s' " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%%Y%%m%%d')<'%s' "  % (s_day, e_day)
        print(sql)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

monthly_union = open("data/monthly_all.data", "a")

def main_hb_go_times(s_day, e_day, out_file_name):

    out_file_path = "data/" + out_file_name
    out_file2 = open(out_file_path, "a")
    o_go_times = ConsumerTimesDao()
    result_model_list = o_go_times.get_uid(s_day, e_day)
    uid_list = [result_model.uid for result_model in result_model_list]
    print(len(uid_list))

    value_list = []

    all_temp = 0
    num_temp = 0
    for key, value in Counter(uid_list).items():
        # out_file1.write(str(key) + "\t" + str(value) + "\n")
        value_list.append(value)

    for key, value in Counter(value_list).items():
        all_temp += int(key) * int(value)
        num_temp += int(value)

        out_file2.write(str(key) + "\t" + str(value) + "\n")
    # monthly_union.write(str(s_day)+ "\t" + str(all_temp) + "\t" + str(num_temp) + "\t" + str(float(all_temp)/float(num_temp)) + "\n")
    print(s_day, all_temp, num_temp, float(all_temp)/float(num_temp))
    pass

if __name__ == "__main__":
    main_hb_go_times("20140101", "20150101", "year2014.data")
    pass