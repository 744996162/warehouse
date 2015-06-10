#ecoding=utf-8
__author__ = 'Administrator'


from db import source_hbgj_mysql
from uid_phone_dict import *


import time
import pymongo
import gc

class Uid():
    def __init__(self):
        self.uid = ""

    def setValues(self, valueList):
        self.uid = str(valueList[0])



class HbBaseDao(source_hbgj_mysql.Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        source_hbgj_mysql.Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result_by_setValue(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class Hb_consumers_id():
    """
    table: phone_user
    "select phoneid,phone from phone_user"

    """

    def __init__(self, DBClass = HbBaseDao, ModelClass=Uid):
        self.db = DBClass()
        self.ModelClass = ModelClass
    def get_consumers_set(self, s1, s2):
        sql = "SELECT distinct PHONEID " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')>='%s' " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s' "  %(s1, s2)

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        uid_list = []

        for model in result_model_list:
            uid_list.append(model.uid)
        uid_set = set(uid_list)

        return uid_set

hb_dict, gt_dict = get_dict()


def get_hb_consumers_phone_set(s1, s2):
    hb_object = Hb_consumers_id()
    hb_uid_set = hb_object.get_consumers_set(s1, s2)

    hb_phone_list = []
    cannot_find_phone = 0

    for uid in hb_uid_set:
        try:
            phone = hb_dict[uid]
            hb_phone_list.append(phone)
        except Exception as e:
            cannot_find_phone += 1
            pass
    print(s1, cannot_find_phone)
    hb_phone_set = set(hb_phone_list)
    return hb_phone_set



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


def get_gt_uid_list(s1, s2, dbtype="169server"):
    db = get_db(dbtype)
    # result = db.sub_order.find({"status": "支付成功","order_date": {"$gte": 20150101, "$lt": 20150401}}, {"card_no": 1, "phone": 1, "_id":0 })
    uid_list = []
    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":s1, "$lt":s2}}, {"uid": 1, "_id":0 })

    count = 1
    print(str(0) + "\t" + str(time.ctime()))
    for i in result1:
        count += 1
        uid = str(i["uid"])
        uid_list.append(uid)
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

def get_gt_consumers_phone_set(uid_list):
    uid_set = set(uid_list)
    gt_phone_list = []

    for uid in uid_set:
        try:
            phone = gt_dict[uid]
            gt_phone_list.append(phone)
        except Exception as e:
            pass

    gt_phone_set = set(gt_phone_list)
    return gt_phone_set



def get_phone_set(s1, s2):
    hb_phone_set = get_hb_consumers_phone_set(s1, s2)
    int_s1 = int(s1)
    int_s2 = int(s2)
    if int_s2 > 20150301:
        gt_uid_list = get_gt_uid_list2015(int_s1,int_s2)
    else:
        gt_uid_list = get_gt_uid_list(int_s1, int_s2)

    gt_phone_set = get_gt_consumers_phone_set(gt_uid_list)

    hb_consumers_num = len(hb_phone_set)
    gt_consumers_num = len(gt_phone_set)
    union_num = len(hb_phone_set & gt_phone_set)

    return hb_consumers_num, gt_consumers_num, union_num


def main(s1, s2):
    print(s1, time.ctime())
    file_out = open("result.dat", "a")
    hb_consumers_num, gt_consumers_num, union_num = get_phone_set(s1, s2)
    file_out.write(str(s1) + "\t" + str(hb_consumers_num) + "\t" + str(gt_consumers_num) + "\t" + str(union_num) + "\n")
    file_out.close()

if __name__ == "__main__":
    """
    20140101
    20140401
    20140701
    20141001
    20150101
    20150401

    """


    file_out = open("result.dat", "a")
    file_out.write("time" + "\t" + "hb_consumers" + "\t" + "gt_consuemrs" + "\t" + "union_numbers" + "\n")
    file_out.close()
    main("20130701", "20131001")
    main("20131001", "20140101")

    main("20140101", "20140401")
    main("20140401", "20140701")
    main("20140701", "20141001")
    main("20141001", "20150101")

    main("20150101", "20150401")


    pass