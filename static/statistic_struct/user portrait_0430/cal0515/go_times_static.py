#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc

'''高铁2014年用户出行次数统计'''


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
    card_no_list = []
    result1 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140101, "$lt":20150701}}, {"card_no": 1, "_id":0 })

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        card_no = str(i["card_no"])
        card_no_list.append(card_no)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    return card_no_list


def counter():
    card_no_list = getMondoData()
    o_Counter = Counter(card_no_list)
    out_file = open("data/counter.data", "a")
    out_file2 = open("data/result.data", "a")
    value_list = []

    for key, value in o_Counter.items():
        # out_file.write(key + "\t" + str(value) + "\n")
        value_list.append(value)

    for key, value in Counter(value_list).items():
        out_file2.write(str(key) + "\t" + str(value) + "\n")
    pass

if __name__ == "__main__":

    # getMondoData()
    counter()
