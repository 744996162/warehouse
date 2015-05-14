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
    model_list =[]
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    print("result1:start" + str(time.ctime()))
    result1 = db.sub_order.find({"status": "支付成功", "order_date":{"$gte":20150226, "$lt":20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result1:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))

    print("result2:start" + str(time.ctime()))
    result2 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$lt":20140101}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result2:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))


    print("result3:start" + str(time.ctime()))
    result3 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140101, "$lt":20140401}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result3:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))

    print("result4:start" + str(time.ctime()))
    result4 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140401, "$lt":20140501}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result4:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))


    print("result5:start" + str(time.ctime()))
    result5 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140501, "$lt":20140601}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result5:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))

    print("result6:start" + str(time.ctime()))
    result6 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140601, "$lt":20140701}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result6:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))

    print("result7:start" + str(time.ctime()))
    result7 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140701, "$lt":20140801}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result7:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))

    print("result8:start" + str(time.ctime()))
    result8 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140801, "$lt":20140901}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result8:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))

    print("result9:start" + str(time.ctime()))
    result9 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20140901, "$lt":20141001}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result9:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:"+ str(len(model_list)))

    print("result10:start" + str(time.ctime()))
    result10 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20141001, "$lt":20141101}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result10:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))

    print("result11:start" + str(time.ctime()))
    result11 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20141101, "$lt":20141201}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result11:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))



    print("result12:start" + str(time.ctime()))
    result12 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20141201, "$lt":20150101}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result12:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))

    print("result13:start" + str(time.ctime()))
    result13 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":20150101, "$lt":20150226}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result13:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))


    return model_list


def getMondoData_new(dbtype="169server"):
    db = get_db(dbtype)
    model_list =[]
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    print("result1:start" + str(time.ctime()))
    result1 = db.sub_order.find({"status": "支付成功", "order_date":{"$gte":20150226, "$lt":20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result1:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)
    print("model_list_len:" + str(len(model_list)))
    return model_list


def getMondoData_old(stime, etime, dbtype="169server"):
    db = get_db(dbtype)
    model_list =[]
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    print("result1:start" + str(time.ctime()))
    result1 = db.sub_order_his.find({"status": "支付成功", "order_date":{"$gte":int(stime), "$lt":int(etime)}}, {"card_no": 1, "phone": 1, "_id":0 })
    for i in result1:
        o_model = hb_model.HbUser()
        o_model.cardno = i["card_no"]
        o_model.phone = i["phone"]
        model_list.append(o_model)

    print("model_list_len:" + str(len(model_list)))
    return model_list


if __name__ == "__main__":

    model_list = getMondoData()
    for i in model_list:
        print(i)
    # print(type(result))
