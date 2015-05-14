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

    result1 = db.order.find({"i_status": "3", "order_date":{"$gte":20150226, "$lt": 20150401}}, {"pay_method": 1, "_id":0 })
    pay_method_list = []
    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        # uid = str(i["uid"])
        pay_method = str(i["pay_method"])
        pay_method_list.append(pay_method)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1

    result2 = db.order_history.find({"i_status": "3", "order_date":{"$gte":20130601, "$lt": 20141001}}, {"pay_method": 1, "_id":0 })
    pay_method_list = []

    print(str(0) + "\t" + str(time.ctime()))
    for i in result2:
        count += 1
        # uid = str(i["uid"])
        pay_method = str(i["pay_method"])
        pay_method_list.append(pay_method)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result2

    result3 = db.order.find({"i_status": "3", "order_date":{"$gte":20141001, "$lt": 20150226}}, {"pay_method": 1, "_id":0 })

    print(str(0) + "\t" + str(time.ctime()))
    for i in result3:
        count += 1
        # uid = str(i["uid"])
        pay_method = str(i["pay_method"])
        pay_method_list.append(pay_method)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1
    return pay_method_list


def count():
    file_out_paymethod = open("paymethod_count.data", "a")
    pay_method_list = getMondoData()
    o_Counter = Counter(pay_method_list)
    for k,v in o_Counter.iteritems():
        file_out_paymethod.write(str(k) + "\t" + str(v) + "\n")
        print(k, v)
        pass


def pay_method_exchange():
    data_in = open("paymethod_count.data")
    dict_in = open("pay_method.data")

    data_out = open("paymethod_count_out.data","a")

    pay_method_dict = defaultdict(str)

    for i in dict_in:
        stringArr = i.strip().split("\t")
        pay_method = stringArr[0]
        pay_method_title = stringArr[1]
        pay_method_dict[pay_method] = pay_method_title

    for i in data_in:
        stringArr = i.strip().split("\t")
        pay_method = stringArr[0]
        number = stringArr[1]
        pay_method_title = pay_method_dict[pay_method]
        data_out.write(pay_method + "\t" + pay_method_title + "\t" + number + "\n")

if __name__ == "__main__":

    # getMondoData()
    # count()
    pay_method_exchange()
    pass