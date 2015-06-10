#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc

'''高铁2014年用户消费次数留存统计'''


def get_db(dbtype="local"):
    if dbtype == "169server":
        con_local=pymongo.Connection(host="localhost", port=27017)
        db = con_local.admin
        db.authenticate("gtgj", "gtgj")
        db = con_local.gtgj
    else:
        con_local=pymongo.Connection(host="localhost", port=27017)
        db = con_local.gtgj
    return db


def getMondoData(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":s2}}, {"uid": 1, "_id":0 })

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    return uid_list


def getMondoData_2015(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":20150301}}, {"uid": 1, "_id":0 })

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

    del result1

    result2 = db.order.find({"i_status": "3", "order_date":{"$gte":20150301, "$lt":s2}}, {"uid": 1, "_id":0 })
    for i in result2:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result2
    return uid_list


def main():
    """

    20140101
    20140401
    20140701
    20141001
    20150101
    20150401

    """
    uid_listQ1 = getMondoData(20140101, 20140401)
    uid_listQ2 = getMondoData(20140401, 20140701)
    uid_listQ3 = getMondoData(20140701, 20141001)
    uid_listQ4 = getMondoData(20141001, 20150101)
    uid_list2015Q1 = getMondoData_2015(20150101, 20150401)


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


def main_lcd():
    """

    20140101
    20140401
    20140701
    20141001
    20150101
    20150401

    """
    uid_listQ1 = getMondoData(20140101, 20140401)
    uid_listQ2 = getMondoData(20140401, 20140701)
    uid_listQ3 = getMondoData(20140701, 20141001)
    uid_listQ4 = getMondoData(20141001, 20150101)
    uid_list2015Q1 = getMondoData_2015(20150101, 20150401)


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
        if uid in uid_setQ1:
            uid_left_list_Q1_Q2.append(uid)

    for uid in uid_listQ3:
        if uid in uid_setQ1:
            uid_left_list_Q1_Q3.append(uid)

    for uid in uid_listQ4:
        if uid in uid_setQ1:
            uid_left_list_Q1_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ1:
            uid_left_list_Q1_2015Q1.append(uid)





    for uid in uid_listQ3:
        if uid in uid_setQ2:
            uid_left_list_Q2_Q3.append(uid)

    for uid in uid_listQ4:
        if uid in uid_setQ2:
            uid_left_list_Q2_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ2:
            uid_left_list_Q2_2015Q1.append(uid)



    for uid in uid_listQ4:
        if uid in uid_setQ3:
            uid_left_list_Q3_Q4.append(uid)

    for uid in uid_list2015Q1:
        if uid in uid_setQ3:
            uid_left_list_Q3_2015Q1.append(uid)


    for uid in uid_list2015Q1:
        if uid in uid_setQ4:
            uid_left_list_Q4_2015Q1.append(uid)


    out_file_path = "data/gt_consumers_lcd.dat"
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

if __name__ == "__main__":

    main_lcd()