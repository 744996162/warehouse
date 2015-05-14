#coding=utf-8
#
import sys
import os

import pymongo

def test1():
    sys.path.append("G:\data")
    con=pymongo.Connection('localhost',27017)
    # file_in=open("G:\data\test_result.txt",'w')
    file_in="G:/data/result.txt"

    #选择test数据库
    db1=con.test

    #使用db集合
    col_db=db1.db


    for line in  file(file_in):
        id,phone,province,city=line.strip().split(',')
        col_db.insert({"id":id,"phone":phone,"province":province,"city":city})
        print(phone,city)



    # #选择test数据库
    # db=con.test
    #
    # #使用blog集合
    # collection=db.blog
    #
    # for data in collection.find():
    #     print data
    # print(collection.find)

def test2():
    # con_225=pymongo.Connection("182.92.194.225",27017,"readonly","read@hl123")
    con_225=pymongo.Connection(host="182.92.194.225",port=27017)
    db = con_225.collectdata
    db.authenticate("readonly","read@hl123")
    flight=db.flight_price_percent.find()
    for i in  flight:
        print(i)
    pass

def query_local():
    con_local=pymongo.Connection(host="localhost",port=27017)
    db = con_local.test
    # db.authenticate("readonly","read@hl123")
    t=db.flight.find()
    for i in t:
        flightnum=int(i['flightnum'])
        airlineno=str(i['airlineno'])
        hbgj_percent=int(i['hbgj_percent'])
        xc_percent=int(i['xc_percent'])
        qunar_percent=int(i['qunar_percent'])
        datatime=i['datatime']



        print(i['flightnum'],i['airlineno'],i['hbgj_percent'],i['xc_percent'],i['qunar_percent'],i['datatime'])
        print(type(i['flightnum']),type(i['airlineno']),type(i['hbgj_percent']),type(i['xc_percent']) \
            ,type(i['qunar_percent']),type(i['datatime']))

    pass


if __name__=="__main__":
    test2()
    # query_local()
    pass








