#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc

'''高铁2014年用户消费次数统计'''


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
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list_all = []
    uid_list_ios = []
    result1 = db.order.find({"i_status": "3", "order_date": {"$gte": 20150401, "$lt": 20150701}}, {"uid": 1, "_id": 0})

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        uid_list_all.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    uid_list_all_num = len(set(uid_list_all))
    del result1




    result2 = db.order.find({"i_status": "3", "platform": "ios", "order_date": {"$gte": 20150401, "$lt": 20150701}}, {"uid": 1, "_id": 0})

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result2:
        count += 1
        uid = str(i["uid"])
        uid_list_ios.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    uid_list_ios_num = len(set(uid_list_ios))
    del result2


    print("uid_list_all_num:",uid_list_all_num)
    print("uid_list_ios_num:",uid_list_ios_num)

if __name__ == "__main__":
    getMondoData()