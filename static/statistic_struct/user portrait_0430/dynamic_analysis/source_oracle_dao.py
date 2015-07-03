#coding=utf-8
__author__ = 'Administrator'
import time
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

from db.source_hbgj_oracle import oracle_con_hbdt

class BaseUserOracleDao(object):
    def __init__(self):
        self.cursor = oracle_con_hbdt()

    def query_result(self, sql, model_class):
        cursor = oracle_con_hbdt()
        cursor.execute(sql)
        result=cursor.fetchall()
        users_model_list = []
        if not result:
            return False
        for row in result:
            model_object = model_class()
            model_object.set0(row[0])
            model_object.set1(row[1])
            model_object.set2(row[2])
            model_object.set3(row[1]-row[2])
            users_model_list.append(model_object)
        return users_model_list


def test(i_start, i_end):
    file_out = open("data/out_data_test.dat", "a")
    cursor = oracle_con_hbdt()
    sql = "select * from FLIGHT_DYNAMIC_CHANGE_RECORD where FLYDATE='2015-06-30' "

    sql = "select * " \
    "from  " \
    "(select A.*, ROWNUM RN " \
    "from " \
    "(select * from FLIGHT_DYNAMIC_CHANGE_RECORD where FLYDATE='2015-06-30' ) A where ROWNUM<=%d ) " \
    "where RN>=%d " %(i_end, i_start)

    cursor.execute(sql)
    result = cursor.fetchall()
    # print(type(result))
    for values in result:
        out_str = ""
        for value in values:
            out_str += str(value) + "\t"
        file_out.write(out_str + "\n")
    # print(result)
    pass

if __name__ == "__main__":

    # for i in range(1, 500000, 10000):
    #     print(i, time.ctime())
    #     test(i, i+9999)
    test(1, 10000)

    pass