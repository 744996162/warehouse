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
        uid_list = []
        for model in result_model_list:
            uid_list.append(model.uid)
        return uid_list



def main():
    o_object = ConsumerTimesDao()

    uid_listQ1 = o_object.get_uid("20140101", "20140401")
    uid_listQ2 = o_object.get_uid("20140401", "20140701")
    uid_listQ3 = o_object.get_uid("20140701", "20141001")
    uid_listQ4 = o_object.get_uid("20141001", "20150101")
    uid_list2015Q1 = o_object.get_uid("20150101", "20150401")


    uid_setQ1 = set(uid_listQ1)
    uid_setQ2 = set(uid_listQ2)
    uid_setQ3 = set(uid_listQ3)
    uid_setQ4 = set(uid_listQ4)


    uid_left_listQ2 = []
    uid_left_listQ3 = []
    uid_left_listQ4 = []
    uid_left_list2015Q1 = []

    for uid in uid_listQ2:
        if uid in uid_setQ1:
            uid_left_listQ2.append(uid)

    for uid in uid_listQ3:
        if uid in uid_setQ2:
            uid_left_listQ3.append(uid)

    for uid in uid_listQ4:
        if uid in uid_setQ3:
            uid_left_listQ4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ4:
            uid_left_list2015Q1.append(uid)

    del uid_setQ1,uid_setQ2,uid_setQ3,uid_setQ4
    del uid_listQ1,uid_listQ2,uid_listQ3,uid_listQ4, uid_list2015Q1

    out_file_path = "data/all.dat"
    out_file = open(out_file_path, "a")
    out_file.write("Q2" + "\t" + str(len(set(uid_left_listQ2))) + "\n")
    out_file.write("Q3" + "\t" + str(len(set(uid_left_listQ3))) + "\n")
    out_file.write("Q4" + "\t" + str(len(set(uid_left_listQ4))) + "\n")
    out_file.write("2015Q1" + "\t" + str(len(set(uid_left_list2015Q1))) + "\n")

    o_CounterQ2 = Counter(uid_left_listQ2)
    out_file_pathQ2 = "data/" + "Q2.dat"
    out_fileQ2 = open(out_file_pathQ2, "a")
    value_listQ2 = []
    for key, value in o_CounterQ2.items():
        value_listQ2.append(value)
    for key, value in Counter(value_listQ2).items():
        out_fileQ2.write(str(key) + "\t" + str(value) + "\n")

    o_CounterQ3 = Counter(uid_left_listQ3)
    out_file_pathQ3 = "data/" + "Q3.dat"
    out_fileQ3 = open(out_file_pathQ3, "a")
    value_listQ3 = []
    for key, value in o_CounterQ3.items():
        value_listQ3.append(value)
    for key, value in Counter(value_listQ3).items():
        out_fileQ3.write(str(key) + "\t" + str(value) + "\n")

    o_CounterQ4 = Counter(uid_left_listQ4)
    out_file_pathQ4 = "data/" + "Q4.dat"
    out_fileQ4 = open(out_file_pathQ4, "a")
    value_listQ4 = []
    for key, value in o_CounterQ4.items():
        value_listQ4.append(value)
    for key, value in Counter(value_listQ4).items():
        out_fileQ4.write(str(key) + "\t" + str(value) + "\n")

    o_Counter2015Q1 = Counter(uid_left_list2015Q1)
    out_file_path2015Q1 = "data/" + "2015Q1.dat"
    out_file2015Q1 = open(out_file_path2015Q1, "a")
    value_list2015Q1 = []
    for key, value in o_Counter2015Q1.items():
        value_list2015Q1.append(value)
    for key, value in Counter(value_list2015Q1).items():
        out_file2015Q1.write(str(key) + "\t" + str(value) + "\n")
    pass



# def main_Test():
#     o_object = ConsumerTimesDao()
#
#     uid_listQ4 = o_object.get_uid("20141001", "20150101")
#     uid_list2015Q1 = o_object.get_uid("20150101", "20150401")
#
#
#     uid_setQ4 = set(uid_listQ4)
#
#     uid_left_list2015Q1 = []
#
#
#
#
#     for uid in uid_list2015Q1:
#         if uid in uid_setQ4:
#             uid_left_list2015Q1.append(uid)
#
#
#
#     o_Counter2015Q1 = Counter(uid_left_list2015Q1)
#     out_file_path2015Q1 = "data/" + "test.dat"
#     out_file2015Q1 = open(out_file_path2015Q1, "a")
#     value_list2015Q1 = []
#     for key, value in o_Counter2015Q1.items():
#         out_file2015Q1.write(str(key) + "\t" + str(value) + "\n")
#         value_list2015Q1.append(value)
#     # for key, value in Counter(value_list2015Q1).items():
#     #     out_file2015Q1.write(str(key) + "\t" + str(value) + "\n")
#     pass
#     pass



def main_lcd():
    """

    20140101
    20140401
    20140701
    20141001
    20150101
    20150401

    """
    o_object = ConsumerTimesDao()

    uid_listQ1 = o_object.get_uid("20140101", "20140401")
    uid_listQ2 = o_object.get_uid("20140401", "20140701")
    uid_listQ3 = o_object.get_uid("20140701", "20141001")
    uid_listQ4 = o_object.get_uid("20141001", "20150101")
    uid_list2015Q1 = o_object.get_uid("20150101", "20150401")


    uid_setQ1 = set(uid_listQ1)
    uid_setQ2 = set(uid_listQ2)
    uid_setQ3 = set(uid_listQ3)
    uid_setQ4 = set(uid_listQ4)


    # uid_left_listQ2 = []
    # uid_left_listQ3 = []
    # uid_left_listQ4 = []
    # uid_left_list2015Q1 = []

    uid_left_list_Q1_Q2 = []
    uid_left_list_Q1_Q3 = []
    uid_left_list_Q1_Q4 = []
    uid_left_list_Q1_2015Q1 = []


    uid_left_list_Q2_Q3 = []
    uid_left_list_Q2_Q4 = []
    uid_left_list_Q2_2015Q1 = []

    uid_left_list_Q3_Q4 = []
    uid_left_list_Q3_2015Q1 = []


    uid_left_list_Q4_2015Q1 = []


    for uid in uid_listQ2:
        if uid in uid_setQ1 and uid != "0" and uid != "":
            uid_left_list_Q1_Q2.append(uid)

    for uid in uid_listQ3:
        if uid in uid_setQ1 and uid != "0" and uid != "":
            uid_left_list_Q1_Q3.append(uid)

    for uid in uid_listQ4:
        if uid in uid_setQ1 and uid != "0" and uid != "":
            uid_left_list_Q1_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ1 and uid != "0" and uid != "":
            uid_left_list_Q1_2015Q1.append(uid)





    for uid in uid_listQ3:
        if uid in uid_setQ2 and uid != "0" and uid != "":
            uid_left_list_Q2_Q3.append(uid)

    for uid in uid_listQ4:
        if uid in uid_setQ2 and uid != "0" and uid != "":
            uid_left_list_Q2_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ2 and uid != "0" and uid != "":
            uid_left_list_Q2_2015Q1.append(uid)



    for uid in uid_listQ4:
        if uid in uid_setQ3 and uid != "0" and uid != "":
            uid_left_list_Q3_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ3 and uid != "0" and uid != "":
            uid_left_list_Q3_2015Q1.append(uid)


    for uid in uid_list2015Q1:
        if uid in uid_setQ4 and uid != "0" and uid != "":
            uid_left_list_Q4_2015Q1.append(uid)


    out_file_path = "data/hb_consumers_lcd.dat"
    out_file = open(out_file_path, "a")


    out_file.write("Q1" + "\t" + "Q2" + "\t" + str(len(set(uid_left_list_Q1_Q2))) + "\t" + str(len(uid_left_list_Q1_Q2)) + "\n")
    out_file.write("Q1" + "\t" + "Q3" + "\t" + str(len(set(uid_left_list_Q1_Q3))) + "\t" + str(len(uid_left_list_Q1_Q3)) + "\n")
    out_file.write("Q1" + "\t" + "Q4" + "\t" + str(len(set(uid_left_list_Q1_Q4))) + "\t" + str(len(uid_left_list_Q1_Q4)) + "\n")
    out_file.write("Q1" + "\t" + "2015Q1" + "\t" + str(len(set(uid_left_list_Q1_2015Q1))) + "\t" + str(len(uid_left_list_Q1_2015Q1)) + "\n")

    out_file.write("Q2" + "\t" + "Q3" + "\t" + str(len(set(uid_left_list_Q2_Q3))) + "\t" + str(len(uid_left_list_Q2_Q3)) + "\n")
    out_file.write("Q2" + "\t" + "Q4" + "\t" + str(len(set(uid_left_list_Q2_Q4))) + "\t" + str(len(uid_left_list_Q2_Q4)) + "\n")
    out_file.write("Q2" + "\t" + "2015Q1" + "\t" + str(len(set(uid_left_list_Q2_2015Q1))) + "\t" + str(len(uid_left_list_Q2_2015Q1)) + "\n")

    out_file.write("Q3" + "\t" + "Q4" + "\t" + str(len(set(uid_left_list_Q3_Q4))) + "\t" + str(len(uid_left_list_Q3_Q4)) + "\n")
    out_file.write("Q3" + "\t" + "2015Q1" + "\t" + str(len(set(uid_left_list_Q3_2015Q1))) + "\t" + str(len(uid_left_list_Q3_2015Q1)) + "\n")

    out_file.write("Q4" + "\t" + "2015Q1" + "\t" + str(len(set(uid_left_list_Q4_2015Q1))) + "\t" + str(len(uid_left_list_Q4_2015Q1)) + "\n")



def jiduxiaofeicishu():
    """

    20140101
    20140401
    20140701
    20141001
    20150101
    20150401

    """
    o_object = ConsumerTimesDao()

    uid_listQ1 = o_object.get_uid("20140101", "20140401")
    uid_listQ2 = o_object.get_uid("20140401", "20140701")
    uid_listQ3 = o_object.get_uid("20140701", "20141001")
    uid_listQ4 = o_object.get_uid("20141001", "20150101")
    uid_list2015Q1 = o_object.get_uid("20150101", "20150401")
    print("季度")
    print("2014Q1", float(len(uid_listQ1))/len(set(uid_listQ1)), len(uid_listQ1), len(set(uid_listQ1)))
    print("2014Q2", float(len(uid_listQ2))/len(set(uid_listQ2)), len(uid_listQ2), len(set(uid_listQ2)))
    print("2014Q3", float(len(uid_listQ3))/len(set(uid_listQ3)), len(uid_listQ3), len(set(uid_listQ3)))
    print("2014Q4", float(len(uid_listQ4))/len(set(uid_listQ4)), len(uid_listQ4), len(set(uid_listQ4)))
    print("2015Q1", float(len(uid_list2015Q1))/len(set(uid_list2015Q1)), len(uid_list2015Q1), len(set(uid_list2015Q1)))
    pass




if __name__ == "__main__":
    # main(
    # main_lcd()

    jiduxiaofeicishu()
    pass