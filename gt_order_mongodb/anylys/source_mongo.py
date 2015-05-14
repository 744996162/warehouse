
__author__ = 'zhangchao'

import pymongo
from . import model


def get_db(dbtype="local"):
    if dbtype == "169server":
        client = pymongo.MongoClient(host="localhost", port=27017)
        db = client.admin
        db.authenticate("gtgj", "gtgj")
        db = client.gtgj
        pass
    else:
        client = pymongo.MongoClient(host="localhost", port=27017)
        db = client.gtgj
    return db


def get_data():
    db = get_db()
    sub_order_data = db.sub_order.find()
    for sub_order in sub_order_data:
        print(type(sub_order))
        print(sub_order)
    pass

if __name__ == "__main__":
    get_data()

    pass
