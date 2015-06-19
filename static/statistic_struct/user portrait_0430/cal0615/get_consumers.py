#ecoding=utf-8
__author__ = 'zhangchao'

import pymongo
import time
from collections import OrderedDict
from collections import defaultdict



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


def get_channel(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    dict_channel = dict()

    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":s2}}, {"uid": 1, "p_info": 1, "_id":0})

    count = 1


    for i in result1:
        count += 1
        uid = str(i["uid"])
        p_info = str(i["p_info"])

        channel = p_info.strip().split(",")[0]

        dict_channel[uid] = channel

    pass


def get_gt_uid_list(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":s2}}, {"uid": 1, "p_info": 1, "amount": 1, "_id":0})

    count = 1


    dict_channel = dict()

    d = defaultdict(defaultdict(list))



    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        p_info = str(i["p_info"])
        amount = str[i["amount"]]

        channel = p_info.strip().split(",")[0]

        dict_channel[uid] = channel



        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    return uid_list

def get_gt_uid_list2015(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt": 20150301}}, {"uid": 1, "_id":0 })

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
