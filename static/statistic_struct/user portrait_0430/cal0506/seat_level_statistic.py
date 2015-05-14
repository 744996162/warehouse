#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import gc


# """座位等级统计"""

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


def getMondoData(dbtype="169server"):

    """"  huo qu zuo wei deng ji shu ju"""
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })


    G_list = []
    D_list = []
    Normal_list = []

    result1 = db.sub_order.find({"status": "支付成功", "order_date":{"$gte":20150226, "$lt":20150401}}, {"train_no": 1, "seat_name": 1, "_id":0 })

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        train_no = str(i["train_no"])
        seat_name = str(i["seat_name"])

        if train_no[0] == "G":
            G_list.append(seat_name)
        elif train_no[0] == "D":
            D_list.append(seat_name)
        else:
            Normal_list.append(seat_name)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1

    result2 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20130601, "$lt":20150226}}, {"train_no": 1, "seat_name": 1, "_id":0 })

    for i in result2:
        count += 1
        train_no = str(i["train_no"])
        seat_name = str(i["seat_name"])

        if train_no[0] == "G":
            G_list.append(seat_name)
        elif train_no[0] == "D":
            D_list.append(seat_name)
        else:
            Normal_list.append(seat_name)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

    del result2

    return G_list, D_list, Normal_list


def seat_level_statistic():
    G_list, D_list, Normal_list = getMondoData()

    out_file_G = open("data/seat_level_G.data", "a")
    out_file_D = open("data/seat_level_D.data", "a")
    out_file_Normal = open("data/seat_level_Normal.data", "a")

    o_G_Counter = Counter(G_list)
    o_D_Counter = Counter(D_list)
    o_Normal_Counter = Counter(Normal_list)

    for key, value in o_G_Counter.items():
        out_file_G.write(key + "\t" + str(value) + "\n")

    for key, value in o_D_Counter.items():
        out_file_D.write(key + "\t" + str(value) + "\n")

    for key, value in o_Normal_Counter.items():
        out_file_Normal.write(key + "\t" + str(value) + "\n")

if __name__ == "__main__":
    seat_level_statistic()
