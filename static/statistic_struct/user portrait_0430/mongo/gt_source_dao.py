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


def getMondoData(dbtype="local"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })

    result = db.sub_order.find({"status": "支付成功", "order_date":{"$gte":20150101, "$lt":20150430}}, {"card_no": 1, "phone": 1, "_id":0 })
    # print(result)

    model_list = []
    for i in result:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    return model_list

if __name__ == "__main__":

    model_list = getMondoData()
    for i in model_list:
        print(i)
    # print(type(result))
