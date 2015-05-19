#ecoding=utf-8
import time
__author__ = 'Administrator'
import pymongo
from domain import hb_model


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

def getMondoData(s1, s2, dbtype="local"):
    db = get_db(dbtype)
    cardno_list =[]

    print("result1:start" + str(time.ctime()))
    result1 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":s1, "$lt":s2}}, {"card_no": 1, "_id":0 })
    for i in result1:
        cardno = i["card_no"]
        cardno_list.append(cardno)
    print("model_list_len:" + str(len(cardno_list)))
    return cardno_list

def getMondoData2015(s1, s2, dbtype="local"):
    db = get_db(dbtype)
    cardno_list =[]

    print("result1:start" + str(time.ctime()))
    result1 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":s1, "$lt":20150224}}, {"card_no": 1, "_id":0 })
    result2 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20150224, "$lt":s2}}, {"card_no": 1, "_id":0 })

    for i in result1:
        cardno = i["card_no"]
        cardno_list.append(cardno)
    print("model_list_len:" + str(len(cardno_list)))

    for i in result2:
        cardno = i["card_no"]
        cardno_list.append(cardno)
    print("model_list_len:" + str(len(cardno_list)))

    return cardno_list



if __name__ == "__main__":

    pass