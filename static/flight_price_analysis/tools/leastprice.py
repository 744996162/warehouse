#ecoding=utf-8
__author__ = 'Administrator'

from model.flight_model import FlightDataModel
import jsonpickle
from model.price_model import  PriceModel
from analysis import file_search
import time
import datetime
import matplotlib.pyplot as plt
from city import City

class LeastPrice(object):
    #input:the _file_path of json file
    #return a leastprice  priceModel
    def __init__(self, file_path, cabin, time_range="0"):
        self._file_path = file_path
        self._time_range = time_range
        self._cabin = cabin
        # self._file_path="G:/flightprice_date/20150206/BJS_SHA_2015-02-06.json"
        pass

    @staticmethod
    def dateChangeGetTime(str_13):
        date_10 = str_13[0:10]
        date_time = time.localtime(int(date_10))
        return date_time


    def getLeastPriceModel(self):

        flightDataModel = FlightDataModel()
        priceModel = PriceModel()
        leastprice = 999999
        fr_in = open(self._file_path)

        for line in fr_in.readlines():
            obj = jsonpickle.decode(line)
            d_departuretime_temp = LeastPrice.dateChangeGetTime(obj.departuretime)
            d_arrivingtime_temp = LeastPrice.dateChangeGetTime(obj.arrivingtime)

            if self._time_range == "1":
                if d_departuretime_temp.tm_hour >= 8 and  d_departuretime_temp.tm_hour < 22:
                    pass
                else:
                    continue
                pass
            elif self._time_range == "0":
                pass
            if self._cabin == "Y":
                tempprice = obj.leastpriceY
                priceModel.cabin = "Y"
            elif self._cabin == "C":
                tempprice = obj.leastpriceC
                priceModel.cabin = "C"
            elif self._cabin == "F":
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

        # print(dateChangeGetTime(priceModel.departuretime), dateChangeGetTime(priceModel.arrivingtime))

        # print(priceModel.printstr())
        return priceModel


class LeastPriceCDateList(object):
    #input:_data_path, org_city, dst_city, _cdate
    #return priceModel_list

    def __init__(self,data_path, org, dst, cdate, cabin="Y", time_range="0"):
        self._data_path = data_path
        self._org = org
        self._dst = dst
        self._cdate = cdate
        self._cabin = cabin
        self._time_range = time_range
        if len(self._org)>3:
            self._org = City().getCityCode(self._org)
            self._dst = City().getCityCode(self._dst)


    def getJsonFilePathList(self):

        datapath = self._data_path+self._cdate
        file_path_list = []

        file_list = file_search.get_all_file(datapath)
        for file in file_list:
            if (self._org+"_"+self._dst) in file:
                file_path_list.append(file)
                # print(file)
        return file_path_list

    def getLeastPriceModelList(self):

        file_path_list=self.getJsonFilePathList()
        priceModel_list=[]
        for file_path in file_path_list:
            priceModel=LeastPrice(file_path, self._cabin, self._time_range).getLeastPriceModel()
            priceModel_list.append(priceModel)
            pass
        return priceModel_list

    def plot_price(self):
        leastPrice_list=[]
        cdate_list=[]
        flydate_list=[]
        priceModelList=self.getLeastPriceModelList()
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


class LeastPriceFlyDate(object):
    #input:_data_path, org_city, dst_city, fdate,_cabin
    #return priceModel
    def __init__(self,data_path, org, dst, flydate, cabin="Y", time_range="0"):
        self._data_path = data_path
        self._org = org
        self._dst = dst
        self._flydate = flydate
        self._cabin = cabin
        self._time_range = time_range

    def getJsonFilePathList(self):

        datapath = self._data_path
        date_str = self._flydate[0:4]+"-"+self._flydate[4:6]+"-"+self._flydate[6:8]
        file_path_list = []

        file_list = file_search.get_all_file(datapath)
        for file in file_list:
            if (self._org+"_"+self._dst+"_"+date_str) in file:
                file_path_list.append(file)
                # print(file)
        return file_path_list

    @staticmethod
    def getLeastPriceModel(file_name, cabin="Y", time_range="0"):
        flightDataModel = FlightDataModel()
        priceModel = PriceModel()

        leastprice = 999999

        filename_list = file_name.strip().split("/")
        c_date = filename_list[-2]
        fr_in = open(file_name)


        for line in fr_in.readlines():
            obj=jsonpickle.decode(line)
            d_departuretime_temp = LeastPrice.dateChangeGetTime(obj.departuretime)
            d_arrivingtime_temp = LeastPrice.dateChangeGetTime(obj.arrivingtime)

            # print(d_departuretime_temp.tm_hour, d_departuretime_temp.tm_min, d_departuretime_temp.tm_sec)
            if time_range == "1":
                if d_departuretime_temp.tm_hour >= 8 and  d_departuretime_temp.tm_hour < 22:
                    pass
                else:
                    continue
                pass
            elif time_range == "0":
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
        priceModel.cdate = c_date
        priceModel.departuretime = flightDataModel.departuretime
        priceModel.arrivingtime = flightDataModel.arrivingtime
        priceModel.leastprice = leastprice
        priceModel.flytimecode = 0
        #print(LeastPrice.dateChangeGetTime(priceModel.departuretime), LeastPrice.dateChangeGetTime(priceModel.arrivingtime))
        return priceModel

    def getLeastPriceModelList(self):
        file_path_list = self.getJsonFilePathList()
        priceModel_list = []
        for file_path in file_path_list:
            priceModel = LeastPriceFlyDate.getLeastPriceModel(file_path,self._cabin,self._time_range)
            priceModel_list.append(priceModel)
            pass
        return priceModel_list
        pass


    def getLeastDay(self):
        priceModelList =self.getLeastPriceModelList()

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

class LeastPriceFlyDateList(object):

    def __init__(self,data_path, org, dst, flydate_start, date_num, cabin="Y", time_range="0"):
        self._data_path = data_path
        self._org = org
        self._dst = dst
        self._flydate_start = flydate_start
        self._date_num = date_num
        self._cabin = cabin
        self._time_range = time_range

    def getPriceModelList(self):
        date_str = datetime.datetime.strptime(self._flydate_start, '%Y%m%d')
        leastPrice_list = []
        dateString_list = []
        dateDiffer_list = []
        for i in range(self._date_num):
            date_str_temp = date_str + datetime.timedelta(days=i)
            s_flydate = date_str_temp.strftime("%Y%m%d")
            o_LeastPriceFlyDate = LeastPriceFlyDate(self._data_path, self._org, self._dst, s_flydate, cabin="Y", time_range=self._time_range)
            leastPrice, leastPriceDate, dateDiffer = o_LeastPriceFlyDate.getLeastDay()
            leastPrice_list.append(leastPrice)
            dateString_list.append(date_str_temp)
            dateDiffer_list.append(dateDiffer)
            print(leastPrice, s_flydate, dateDiffer)
        return leastPrice_list, dateString_list, dateDiffer_list
        pass


def test_leastPriceCDateList():
    data_path = "G:/flightprice_date/"
    file_path = "G:/flightprice_date/20150206/BJS_SHA_2015-02-10.json"

    o_leastPriceList = LeastPriceCDateList(data_path, org="BJS", dst="SHA", cdate="20150229",time_range="1")
    o_priceModel_list = o_leastPriceList.getLeastPriceModelList()
    for o_priceModel in o_priceModel_list:
        print(o_priceModel.printstr())
    o_leastPriceList.plot_price()
    pass


def test_LeastPriceFlyDate():
    data_path = "G:/flightprice_date/"
    file_path = "G:/flightprice_date/20150206/BJS_SHA_2015-02-10.json"
    o_LeastPriceFlyDateList = LeastPriceFlyDate(data_path=data_path, org="BJS", dst="SHA", flydate="20150224",time_range="1")
    t = o_LeastPriceFlyDateList.getLeastPriceModelList()
    n = o_LeastPriceFlyDateList.getLeastDay()
    for i in t:
        print(i.printstr())
    print(n)
    pass

if __name__ == "__main__":
    data_path = "G:/flightprice_date/"
    file_path = "G:/flightprice_date/20150206/BJS_SHA_2015-02-10.json"

    # test_leastPriceCDateList()
    # test_LeastPriceFlyDate()
    o_LeastPriceFlyDateList = LeastPriceFlyDateList(data_path=data_path, org="BJS", dst="SHA", flydate_start="20150224",date_num=10, time_range="1")
    t = o_LeastPriceFlyDateList.getPriceModelList()

    # file_path_list=o_leastprice.getJsonFilePathList()

    # print(file_path_list)



