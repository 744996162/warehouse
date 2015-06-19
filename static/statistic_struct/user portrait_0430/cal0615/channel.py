#ecoding=utf-8
__author__ = 'zhangchao'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pymongo
import time
from collections import OrderedDict
from collections import defaultdict

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


def get_channel(dbtype="169server"):
    db = get_db(dbtype)
    dict_channel = dict()

    result1 = db.order_history.find({"i_status": "3", "order_date":{"$gte":20130101, "$lt":20150301}}, {"uid": 1, "p_info": 1, "_id":0})
    count = 0

    print(str(count) + "\t" + str(time.ctime()))

    for i in result1:
        count += 1
        uid = str(i["uid"])
        p_info = str(i["p_info"])

        channel = p_info.strip().split(",")[0]

        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

        if dict_channel.has_key(uid):
            continue
        else:
            dict_channel[uid] = channel

    del result1

    result2 = db.order.find({"i_status": "3", "order_date":{"$gte":20150301, "$lt":20150601}}, {"uid": 1, "p_info": 1, "_id":0})

    for i in result2:
        count += 1
        uid = str(i["uid"])
        p_info = str(i["p_info"])

        channel = p_info.strip().split(",")[0]
        if count % 100000 == 0:
            print(str(count) + "\t" + str(time.ctime()))

        if dict_channel.has_key(uid):
            continue
        else:
            dict_channel[uid] = channel

    del result2

    dict_channel_list = defaultdict(list)
    dict_channel_set = defaultdict(set)

    for k,v in dict_channel.items():
        dict_channel_list[v].append(k)



    channel_list = []
    for k,v in dict_channel_list.items():
        dict_channel_set[k] = set(v)
        channel_list.append(k)
        pass
    channel_set = set(channel_list)
    del dict_channel_list
    return dict_channel_set, channel_set


if __name__ == "__main__":

    dict_channel_set, channel_set = get_channel("169server")

    out_file = open("channel.dat", "a")

    count = 0
    for k,v in dict_channel_set.items():
        count += len(v)
        out_file.write(str(k) + "\t" + str(len(v)) + "\n")
        print(k, len(v))
    out_file.close()
    print(channel_set)
    pass