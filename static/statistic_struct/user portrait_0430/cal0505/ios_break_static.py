#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc

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

    result1 = db.sub_order.find({"status": "支付成功", "uid":"20c27fb772000217b", "order_date":{"$gte":20150226, "$lt":20150401}}, {"account": 1, "card_no": 1, "_id":0 })
    d = defaultdict(list)
    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["account"])
        card_no = str(i["card_no"])
        d[uid].append(card_no)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1

    result2 = db.sub_order_his.find({"status": "支付成功", "uid":"20c27fb772000217b", "order_date":{"$gte":20130601, "$lt":20150226}}, {"account": 1, "card_no": 1, "_id":0 })

    for i in result2:
        count += 1
        uid = str(i["account"])
        card_no = str(i["card_no"])
        d[uid].append(card_no)
        if count % 100000 == 0:
            print("query_time" + str(count) + "\t" + str(time.ctime()))

    del result2

    return d


def cal_dic():
    d_list = getMondoData()
    result_dict = {}
    out_file = open("ios_break_count.data", "a")
    count = 1
    for key, value in d_list.items():
        count += 1
        list_num = len(value)
        set_num = len(set(value))
        result_dict[key] = set_num
        if set_num > 20:
            print(key,set_num)
        out_file.write(str(key) + "\t" + str(list_num) + "\t" + str(set_num) + "\n")
        if count % 100000 == 0:
            print("cal_time" + str(count) + "\t" + str(time.ctime()))
    print(time.ctime())
    return result_dict

if __name__ == "__main__":
    # getMondoData()
    cal_dic()
