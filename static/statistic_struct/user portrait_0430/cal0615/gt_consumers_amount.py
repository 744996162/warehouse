#ecoding=utf-8
__author__ = 'Administrator'
import time
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc

from channel import *
from channel_list import *

dict_channel_set, channel_set = get_channel("169server")


def getMondoData(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    # uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date": {"$gte":s1, "$lt":s2}}, {"uid": 1, "amount": 1, "_id": 0})

    count = 1
    print(str(0) + "\t" + str(time.ctime()))

    d = defaultdict(list)
    for i in result1:
        count += 1
        uid = str(i["uid"])
        try:
            amount = float(i["amount"])
        except Exception as e:
            amount = 0
        d[uid].append(amount)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    return d


def getMondoData_2015(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":20150301}}, {"uid": 1, "amount": 1, "_id": 0})

    count = 1
    d = defaultdict(list)
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        try:
            amount = float(i["amount"])
        except Exception as e:
            amount = 0
        d[uid].append(amount)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

    del result1

    result2 = db.order.find({"i_status": "3", "order_date":{"$gte":20150301, "$lt":s2}}, {"uid": 1, "amount": 1, "_id": 0})
    for i in result2:
        count += 1
        uid = str(i["uid"])
        try:
            amount = float(i["amount"])
        except Exception as e:
            amount = 0
        d[uid].append(amount)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result2
    return d


dict_listQ1 = getMondoData(20140101, 20140401)
dict_listQ2 = getMondoData(20140401, 20140701)
dict_listQ3 = getMondoData(20140701, 20141001)
dict_listQ4 = getMondoData(20141001, 20150101)
dict_list2015Q1 = getMondoData_2015(20150101, 20150401)




def main_lcd(channel):

    channel_uid_set = dict_channel_set[channel]


    error_Q1 = 0
    sum_Q1 = 0
    num_Q1 = 0

    for k, value_list in dict_listQ1.items():
        if k in channel_uid_set:
            for value in value_list:
                if value>0:
                    sum_Q1 += value
                    num_Q1 += 1
                else:
                    error_Q1 += 1




    error_Q2 = 0
    sum_Q2 = 0
    num_Q2 = 0

    for k, value_list in dict_listQ2.items():
        if k in channel_uid_set:
            for value in value_list:
                if value>0:
                    sum_Q2 += value
                    num_Q2 += 1
                else:
                    error_Q2 += 1


    error_Q3 = 0
    sum_Q3 = 0
    num_Q3 = 0

    for k, value_list in dict_listQ3.items():
        if k in channel_uid_set:
            for value in value_list:
                if value>0:
                    sum_Q3 += value
                    num_Q3 += 1
                else:
                    error_Q3 += 1


    error_Q4 = 0
    sum_Q4 = 0
    num_Q4 = 0

    for k, value_list in dict_listQ4.items():
        if k in channel_uid_set:
            for value in value_list:
                if value>0:
                    sum_Q4 += value
                    num_Q4 += 1
                else:
                    error_Q4 += 1


    error_2015Q1 = 0
    sum_2015Q1 = 0
    num_2015Q1 = 0

    for k, value_list in dict_list2015Q1.items():
        if k in channel_uid_set:
            for value in value_list:
                if value > 0:
                    sum_2015Q1 += value
                    num_2015Q1 += 1
                else:
                    error_2015Q1 += 1


    out_file_path = "data/" + channel + "_average_price.dat"
    out_file = open(out_file_path, "a")
    out_file.write("time" + "\t" + "sum" + "\t" + "num" + "\t" + "error_num" + "\n")
    out_file.write("Q1" + "\t" + str(sum_Q1) + "\t" + str(num_Q1) + "\t" + str(error_Q1) + "\n")
    out_file.write("Q2" + "\t" + str(sum_Q2) + "\t" + str(num_Q2) + "\t" + str(error_Q2) + "\n")
    out_file.write("Q3" + "\t" + str(sum_Q3) + "\t" + str(num_Q3) + "\t" + str(error_Q3) + "\n")
    out_file.write("Q4" + "\t" + str(sum_Q4) + "\t" + str(num_Q4) + "\t" + str(error_Q4) + "\n")
    out_file.write("2015Q1" + "\t" + str(sum_2015Q1) + "\t" + str(num_2015Q1) + "\t" + str(error_2015Q1) + "\n")


channel_list = get_channel_list()
for channel in channel_list:
    main_lcd(channel)
    print(channel)







