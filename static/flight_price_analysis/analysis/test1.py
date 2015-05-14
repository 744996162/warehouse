#ecoding=utf-8
__author__ = 'zhangchao'
from model.flight_model import FlightDataModel
import jsonpickle
from model.seatcost_model import SeatCostModel
from model.price_model import  PriceModel
import json
import file_search
import matplotlib.pyplot as plt
import time
import datetime
from tools import *
from tools.city import  City


def getJsonFilePathList(org="BJS",dst="SHA",cdate="20150206"):

    datapath = "G:/flightprice_date/"+cdate
    file_path_list = []

    file_list = file_search.get_all_file(datapath)
    for file in file_list:
        if (org+"_"+dst) in file:
            file_path_list.append(file)
            # print(file)
    return file_path_list


#指定json文件名，仓位，获取该json内价格最低的PriceModel对象
def getLeastPriceModel(file_name,cabin="Y"):
    # datapath="G:/20150206"
    # file_name=datapath+"/BJS_SHA_2015-02-07.json"

    flightDataModel=FlightDataModel()
    priceModel=PriceModel()

    leastprice=999999

    fr_in=open(file_name)

    for line in fr_in.readlines():
        obj=jsonpickle.decode(line)
        if cabin=="Y":
            tempprice=obj.leastpriceY
            priceModel.cabin="Y"
        elif cabin=="C":
            tempprice=obj.leastpriceC
            priceModel.cabin="C"
        elif cabin=="F":
            tempprice=obj.leastpriceF
            priceModel.cabin="F"
        else:
            return 0

        if tempprice<leastprice:
            leastprice=tempprice
            flightDataModel=obj

    priceModel.fn=flightDataModel.fn
    priceModel.accode=flightDataModel.accode
    priceModel.org=flightDataModel.org
    priceModel.dst=flightDataModel.dst
    priceModel.departureairportcode=flightDataModel.departureairportcode
    priceModel.arrivingairportcode=flightDataModel.arrivingairportcode
    priceModel.src=flightDataModel.src
    priceModel.flydate=flightDataModel.flydate
    priceModel.cdate=flightDataModel.cdate
    priceModel.departuretime=flightDataModel.departuretime
    priceModel.arrivingtime=flightDataModel.arrivingtime
    priceModel.leastprice=leastprice
    priceModel.flytimecode=0

    # print(priceModel.printstr())
    return priceModel


def getLeastPriceModelTime(file_name, cabin="Y", time_factor="1"):
    # datapath="G:/20150206"
    # file_name=datapath+"/BJS_SHA_2015-02-07.json"

    flightDataModel=FlightDataModel()
    priceModel=PriceModel()

    leastprice=999999

    fr_in=open(file_name)

    for line in fr_in.readlines():
        obj=jsonpickle.decode(line)
        d_departuretime_temp = dateChangeGetTime(obj.departuretime)
        d_arrivingtime_temp = dateChangeGetTime(obj.arrivingtime)

        # print(d_departuretime_temp.tm_hour, d_departuretime_temp.tm_min, d_departuretime_temp.tm_sec)
        if time_factor == "1":
            if d_departuretime_temp.tm_hour >= 8 and  d_departuretime_temp.tm_hour < 22:
                pass
            else:
                continue
            pass
        elif time_factor == "2":
            pass
        if cabin == "Y":
            tempprice = obj.leastpriceY
            priceModel.cabin = "Y"
        elif cabin == "C":
            tempprice = obj.leastpriceC
            priceModel.cabin = "C"
        elif cabin == "F":
            tempprice = obj.leastpriceF
            priceModel.cabin = "F"
        else:
            return 0

        if tempprice < leastprice:
            leastprice = tempprice
            flightDataModel = obj

    priceModel.fn = flightDataModel.fn
    priceModel.accode = flightDataModel.accode
    priceModel.org = flightDataModel.org
    priceModel.dst = flightDataModel.dst
    priceModel.departureairportcode = flightDataModel.departureairportcode
    priceModel.arrivingairportcode = flightDataModel.arrivingairportcode
    priceModel.src = flightDataModel.src
    priceModel.flydate = flightDataModel.flydate
    priceModel.cdate = flightDataModel.cdate
    priceModel.departuretime = flightDataModel.departuretime
    priceModel.arrivingtime = flightDataModel.arrivingtime
    priceModel.leastprice = leastprice
    priceModel.flytimecode = 0

    print(dateChangeGetTime(priceModel.departuretime), dateChangeGetTime(priceModel.arrivingtime))

    # print(priceModel.printstr())
    return priceModel


def test2():
    Y, C, F = getLeastFlightModel()
    priceCabinY = PriceModel()
    priceCabinY.cabin = "Y"
    cabinC = PriceModel()
    cabinC.cabin = "C"
    cabinF = PriceModel()
    cabinF.cabin = "F"

    priceCabinY.fn = Y.fn
    priceCabinY.accode = Y.accode
    priceCabinY.org = Y.org
    priceCabinY.dst = Y.dst
    priceCabinY.departureairportcode=Y.departureairportcode
    priceCabinY.arrivingairportcode=Y.arrivingairportcode
    priceCabinY.src=Y.src
    priceCabinY.flydate=Y.flydate
    priceCabinY.cdate=Y.cdate
    priceCabinY.departuretime=Y.departuretime
    priceCabinY.arrivingtime=Y.arrivingtime
    priceCabinY.leastprice=Y.leastpriceY
    priceCabinY.flytimecode=0


    cabinC.fn=C.fn
    cabinC.accode=C.accode
    cabinC.org=C.org
    cabinC.dst=C.dst
    cabinC.departureairportcode=C.departureairportcode
    cabinC.arrivingairportcode=C.arrivingairportcode
    cabinC.src=C.src
    cabinC.flydate=C.flydate
    cabinC.cdate=C.cdate
    cabinC.departuretime=C.departuretime
    cabinC.arrivingtime=C.arrivingtime
    cabinC.leastprice=C.leastpriceC
    cabinC.flytimecode=0
    
    cabinF.fn=F.fn
    cabinF.accode=F.accode
    cabinF.org=F.org
    cabinF.dst=F.dst
    cabinF.departureairportcode=F.departureairportcode
    cabinF.arrivingairportcode=F.arrivingairportcode
    cabinF.src=F.src
    cabinF.flydate=F.flydate
    cabinF.cdate=F.cdate
    cabinF.departuretime=F.departuretime
    cabinF.arrivingtime=F.arrivingtime
    cabinF.leastprice=F.leastpriceF
    cabinF.flytimecode=0

    print(cabinY.printstr())
    print(cabinC.printstr())
    print(cabinF.printstr())

    return cabinY,cabinC,cabinF


def date_change(str_13):
    date_10 = str_13[0:10]
    date_time = datetime.datetime.localtime(int(date_10))
    date1 = time.strftime("%Y%m%d",date_time)
    # print(date1)
    return date1

def dateChangeGetTime(str_13):
    date_10=str_13[0:10]
    date_time=time.localtime(int(date_10))
    # date1=time.strftime("%H:%M:%S",date_time)
    return date_time

def plot_price(priceModelList):
    leastPrice_list=[]
    cdate_list=[]
    flydate_list=[]
    for priceModel in priceModelList:
        c_date=priceModel.cdate
        fly_date=priceModel.flydate
        fly_date_int=datetime.datetime.strptime(fly_date,'%Y-%m-%d')

        flydate_list.append(fly_date_int)
        leastPrice_list.append(priceModel.leastprice)
        # leastpriceF_list.append(cabinF.leastpriceF)

    plt.plot(flydate_list,leastPrice_list,"*-")
    plt.xlabel("datetime")
    plt.ylabel("price")
    plt.show()


def plot_main_test(org, dst, cdate="20150209", cabin="Y", time_factor="1"):
    if len(org)>3:
        org = City().getCityCode(org)
        dst = City().getCityCode(dst)

    filePathList = getJsonFilePathList(org, dst, cdate)
    # filePathList=getJsonFilePathList(_org="BJS",_dst="WUH",_cdate="20150207")
    # print(filePathList)
    priceModelList = []
    for filePath in filePathList:
        # print(filePath)
        priceModel = getLeastPriceModelTime(filePath, cabin,time_factor)
        priceModelList.append(priceModel)
        # print(priceModel.printstr())
    plot_price(priceModelList)
    pass

if __name__ == "__main__":
    # plot_main_test("广州","武汉",_cdate="20150225",_cabin="Y")
    # plot_main_test("武汉", "深圳", _cdate="20150210", _cabin="Y")

    # plot_main_test("深圳", "武汉", cdate="20150210", cabin="Y", time_factor="2")

    # plot_main_test(org="BJS",dst="SHA",cdate="20150311")
    plot_main_test(org="武汉",dst="深圳",cdate="20150311", time_factor="1")


