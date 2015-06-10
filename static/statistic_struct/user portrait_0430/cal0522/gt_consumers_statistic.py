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


def getMondoData(dbtype="local"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order.find({"i_status": "3", "order_date": {"$gte": 20150228, "$lt": 20150501}}, {"uid": 1, "_id": 0})

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1

    result2 = db.order_history.find({"i_status": "3", "order_date": {"$gte": 20150101, "$lt": 20150228}}, {"uid": 1, "_id": 0})

    print(str(0) + "\t" + str(time.ctime()))
    for i in result2:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

    print(len(uid_list))
    return uid_list

if __name__ == "__main__":
    getMondoData("169server")


    pass

