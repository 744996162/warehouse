__author__ = 'Administrator'
import datetime
import pymongo
from model import CheapModel
from model import ExpensiveModel
from goal_dao import CheapPriceUpdateDao
from goal_dao import ExpensivePriceUpdateDao


def getMondoData(date_start, date_end, dbtype="225"):
     if dbtype == 'local':
        con_local = pymongo.Connection(host="localhost",port=27017)
        db = con_local.test
        flight = db.flight.find({"datatime":{"$gt":date_start}})

     elif dbtype=='225':
        con_225=pymongo.Connection(host="182.92.194.225",port=27017)
        db = con_225.collectdata
        db.authenticate("readonly","read@hl123")
        # flight=db.flight_price_percent.find()
        flight=db.flight_price_percent.find({"datatime": {"$gt": date_start, "$lt": date_end}})
        print(flight)
        return flight
     else:
        return None
     pass


def getResult(flights):
    cheapResult=[]
    expensiveResult=[]

    for i in flights:
        # print i
        cheap_object = CheapModel()
        expensive_object = ExpensiveModel()
        cheap_object.flightnum = expensive_object.flightnum = int(i['flightnum'])
        cheap_object.airlineno = expensive_object.airlineno = str(i['airlineno'])

        cheap_object.hbgj_percent_cheap=int(i['hbgj_cheap'])
        cheap_object.xc_percent_cheap=int(i['xc_cheap'])
        cheap_object.qunar_percent_cheap=int(i['qunar_cheap'])
        cheap_object.datatime=(i['datatime']+datetime.timedelta(days=0))
        cheap_object.updatetime=i['datatime']

        expensive_object.hbgj_percent = int(i['hbgj_percent'])
        expensive_object.xc_percent=int(i['xc_percent'])
        expensive_object.qunar_percent=int(i['qunar_percent'])
        expensive_object.datatime=(i['datatime']+datetime.timedelta(days=0))
        expensive_object.updatetime=i['datatime']

        cheapResult.append(cheap_object)
        expensiveResult.append(expensive_object)
    return cheapResult, expensiveResult


def main(s_day, type="", goal_db="91bi"):

    date_start = datetime.datetime.strptime(s_day, "%Y%m%d")
    date_end = date_start + datetime.timedelta(days=1)
    data = getMondoData(date_start, date_end, dbtype="225")

    cheap_model_list,expensive_model_list = getResult(data)

    o_cheap_update_dao = CheapPriceUpdateDao(goal_db)
    o_expensive_update_dao = ExpensivePriceUpdateDao(goal_db)
    if type == "":
        o_cheap_update_dao.insert_data(cheap_model_list)
        o_expensive_update_dao.insert_data(o_expensive_update_dao)
    elif type == "cheap":
        o_cheap_update_dao.insert_data(cheap_model_list)
    elif type == "expensive":
        o_expensive_update_dao.insert_data(expensive_model_list)
    else:
        pass

    pass


if __name__ == "__main__":
    today = datetime.datetime.now().strftime("%Y%m%d")
    date_start = datetime.datetime.strptime(today, "%Y%m%d")
    date_end = date_start + datetime.timedelta(days=1)
    data = getMondoData(date_start, date_end, dbtype="225")
    print(type(data))

    # today = datetime.datetime.now().strftime("%Y%m%d")
    # main(today,"expensive")
    pass