#ecoding=utf-8
__author__ = 'zhangchao'
from model.flight_model import FlightDataModel
import jsonpickle
from model.price_model import  PriceModel
import file_search
import matplotlib.pyplot as plt
import time
import datetime
from tools.city import City

def getJsonFilePathList_flyDate(org="BJS", dst="SHA", flydate="20150227"):

    datapath = "G:/flightprice_date/"
    date_str = flydate[0:4]+"-"+flydate[4:6]+"-"+flydate[6:8]
    file_path_list = []

    file_list = file_search.get_all_file(datapath)
    for file in file_list:
        if (org+"_"+dst+"_"+date_str) in file:
            file_path_list.append(file)
            # print(file)
    return file_path_list


#指定json文件名，仓位，获取该json内价格最低的PriceModel对象
def getLeastPriceModel(file_name, cabin="Y"):
    # datapath="G:/20150206"
    # file_name=datapath+"/BJS_SHA_2015-02-07.json"

    flightDataModel = FlightDataModel()
    priceModel = PriceModel()

    leastprice = 999999

    filename_list = file_name.strip().split("/")
    c_date = filename_list[-2]
    fr_in = open(file_name)

    for line in fr_in.readlines():
        obj = jsonpickle.decode(line)
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
    priceModel.cdate = c_date
    priceModel.departuretime = flightDataModel.departuretime
    priceModel.arrivingtime = flightDataModel.arrivingtime
    priceModel.leastprice = leastprice
    priceModel.flytimecode = 0

    # print(priceModel.printstr())
    return priceModel


def getLeastPriceModelTime(file_name,cabin="Y",time_factor="1"):
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
    return priceModel



def date_change(str_13):
    date_10 = str_13[0:10]
    date_time = time.localtime(int(date_10))
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
        # c_date_int=datetime.datetime.strptime(c_date,'%Y-%m-%d')

        flydate_list.append(fly_date_int)
        leastPrice_list.append(priceModel.leastprice)
        # leastpriceF_list.append(cabinF.leastpriceF)

    plt.plot(flydate_list,leastPrice_list,"*-")
    plt.xlabel("datetime")
    plt.ylabel("price")
    plt.show()

    pass

def plot_price_flydate(priceModelList):
    leastPrice_list = []
    cDate_list = []
    flyDate_list = []
    dateDifferList = []
    for priceModel in priceModelList:
        c_date = priceModel.cdate
        # print(c_date)
        fly_date = priceModel.flydate
        flyDate_date = datetime.datetime.strptime(fly_date,'%Y-%m-%d')
        cDate_date = datetime.datetime.strptime(c_date,'%Y%m%d')
        # fly_date_int=datetime.datetime.strptime(fly_date,'%Y-%m-%d')

        dateDiffer = (cDate_date - flyDate_date).days


        flyDate_list.append(flyDate_date)
        cDate_list.append(cDate_date)
        leastPrice_list.append(priceModel.leastprice)

        dateDifferList.append(dateDiffer)

        # leastpriceF_list.append(cabinF.leastpriceF)
    print(cDate_list, leastPrice_list)
    print(dateDifferList, leastPrice_list)
    # print(dateDifferList,leastPrice_list)
    # plt.plot(cDate_list,leastPrice_list,"*-")
    plt.plot(dateDifferList, leastPrice_list, "*-")
    plt.xlabel("datetime")
    plt.ylabel("price")
    plt.show()

def plotMainleastPrice(org, dst, flydate="20150227", cabin="Y"):
    if len(org) > 3:
        org = City().getCityCode(org)
        dst = City().getCityCode(dst)

    filePathList = getJsonFilePathList_flyDate(org, dst, flydate)
    priceModelList = []
    for filePath in filePathList:
        # print(filePath)
        priceModel = getLeastPriceModelTime(filePath, cabin=cabin, time_factor="1")
        priceModelList.append(priceModel)
        # print(priceModel.printstr())
    # plot_price(priceModelList)
    plot_price_flydate(priceModelList)
    pass

def getLeastPriceModelList(org, dst, flydate, cabin="Y"):
    if len(org)>3:
        org = City().getCityCode(org)
        dst = City().getCityCode(dst)

    filePathList = getJsonFilePathList_flyDate(org, dst, flydate)
    priceModelList = []
    for filePath in filePathList:
        # priceModel = getLeastPriceModelTime(filePath,_cabin=_cabin)
        priceModel = getLeastPriceModel(filePath, cabin=cabin)
        priceModelList.append(priceModel)
    return priceModelList


def getLeastDay(org, dst, flydate, cabin="Y"):
    priceModelList = getLeastPriceModelList(org, dst, flydate, cabin)

    leastPrice_temp = 999999
    leastPriceDate_temp = ""
    dateDiffer_temp = ""

    for priceModel in priceModelList:
        leastPrice = priceModel.leastprice
        c_date = priceModel.cdate
        fly_date = priceModel.flydate

        flyDate_date = datetime.datetime.strptime(fly_date,'%Y-%m-%d')
        cDate_date = datetime.datetime.strptime(c_date,'%Y%m%d')

        dateDiffer = (cDate_date - flyDate_date).days

        if leastPrice <= leastPrice_temp:
            leastPrice_temp = leastPrice
            leastPriceDate_temp = c_date
            dateDiffer_temp = dateDiffer
    return leastPrice_temp, leastPriceDate_temp, dateDiffer_temp

def plotMainDateDiffer(start_date, date_num, org, dst, cabin="Y"):
    # base_date = "20150210"
    date_str = datetime.datetime.strptime(start_date, '%Y%m%d')
    leastPrice_list = []
    dateString_list = []
    dateDiffer_list = []
    # for i in range(20):
    for i in range(date_num):
        date_str_temp = date_str + datetime.timedelta(days=i)
        dateString = date_str_temp.strftime("%Y%m%d")
        leastPrice, leastPriceDate, dateDiffer = getLeastDay(org, dst, flydate=dateString, cabin=cabin)

        leastPrice_list.append(leastPrice)
        dateString_list.append(date_str_temp)
        dateDiffer_list.append(dateDiffer)

        print(leastPrice, dateString, dateDiffer)
        # plot_main_test2("北京","上海",_flydate=date_str,_cabin="Y")

    plt.plot(dateString_list, dateDiffer_list, "*-")
    plt.xlabel("datetime")
    plt.ylabel("dateDiffer")
    plt.show()

if __name__ == "__main__":
    # plot_main_test("广州","武汉",_cdate="20150210",_cabin="Y")
    # plotMainleastPrice("广州","武汉",_flydate="20150227",_cabin="Y")
    # getJsonFilePathList_flyDate()

    # plot_main_test2("北京","上海",_flydate="20150228",_cabin="F")
    # plot_main_test2("广州","武汉",_flydate="20150304",_cabin="Y")
    # A,B,C=getLeastDay("广州","武汉",_flydate="20150304",_cabin="Y")
    # print(A,B,C)

    # plotMainDateDiffer("20150220", 10, "北京", "广州", _cabin="Y")
    plotMainDateDiffer("20150224", 20, "BJS", "SHA")


