#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
import gc
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#"""高端用户统计("一等座", "软卧", "商务座", "特等座", "高级软卧", "高级动卧")"""

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

    result1 = db.sub_order.find({"status": "支付成功", "order_date":{"$gte":20150226, "$lt":20150401}}, {"uid": 1, "seat_name": 1, "_id":0 })
    d = defaultdict(list)
    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        seat_name = str(i["seat_name"])
        d[uid].append(seat_name)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result1


    result2 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20130601, "$lt":20141001}}, {"uid": 1, "seat_name": 1, "_id":0 })

    print(str(0) + "\t" + str(time.ctime()))
    for i in result2:
        count += 1
        uid = str(i["uid"])
        seat_name = str(i["seat_name"])
        d[uid].append(seat_name)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result2
    #
    result3 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20141001, "$lt":20150226}}, {"uid": 1, "seat_name": 1, "_id":0 })
    print(str(0) + "\t" + str(time.ctime()))
    for i in result3:
        count += 1
        uid = str(i["uid"])
        seat_name = str(i["seat_name"])
        d[uid].append(seat_name)
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))
    del result3
    return d


def cal_dic():
    d_list = getMondoData()
    result_dict = {}
    out_file = open("data/user_level.data", "a")
    count = 1

    seat_level = ["一等座", "软卧", "商务座", "特等座", "高级软卧", "高级动卧"]

    for key, value in d_list.items():
        count += 1
        set_seat_name = set(value)
        state = 1
        out_str = ""
        for seat_name in set_seat_name:
            # if out_str == "":
            #     out_str += seat_name.encode('gbk')
            # else:
            #     out_str += "," + seat_name.encode('gbk')
            if seat_name not in seat_level:
                state = 0
                break

        if state == 1:
            # print(out_str)
            ticket_num = len(value)
            # out_file.write(key + "\t" + str(ticket_num) + "\t" + str(out_str) + "\n")
            out_file.write(key + "\t" + str(ticket_num) + "\n")

        if count % 100000 == 0:
            print("cal_time" + str(count) + "\t" + str(time.ctime()))
    print(time.ctime())
    return result_dict

if __name__ == "__main__":

    # getMondoData()
    cal_dic()
