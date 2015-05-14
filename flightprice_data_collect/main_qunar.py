__author__ = 'Administrator'
import datetime
import os
import logging
import json
import threading
import urllib2
import jsonpickle


from model.seatcost_model import SeatCostModel
from model.flight_model import FlightDataModel
from tools.url import Url


# store_path = "/home/huolibi/data/price"
today_str = datetime.datetime.now().strftime("%Y%m%d")
today_in = datetime.datetime.now().strftime("%Y-%m-%d")


#return url list

def getUrl(s_day, detal_days, platform="ctrip"):
    url_obj = Url(platform)
    url_list = url_obj.getAllUrl(s_day, detal_days)
    return url_list


#from an url get a json
#type = "str" or "json"
# def getJson(url, type=""):
def getJson(url, type=""):
    req_headers = {}
    req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    req_headers['Accept-Encoding'] = 'deflate'
    req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
    req_headers['Referer'] = "http://search.rsscc.cn"
    req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
    request = urllib2.Request(url, headers=req_headers)

    page_content = urllib2.urlopen(request)
    article_json = page_content.read()
    if type == "json":
        # article_json = page_content.read()
        return json.loads(article_json)
    else:
        return article_json

#store s json_str in a text



#getLeastPrice
def getLeastPrice(seatcost_list):
    seatcost_model = SeatCostModel()
    Yprice = 999999
    Cprice = 999999
    Fprice = 999999
    Yct = ""
    Cct = ""
    Fct = ""

    for seatcost in seatcost_list:
        bct = str(seatcost["bct"])
        try:
            ct = str(seatcost["ct"])
        except Exception as a:
            ct = ""
        price = int(seatcost["price"])
        # print(bct,ct,"Y",price)
        if bct == "Y" and price < Yprice:
            Yct = ct
            Yprice = price
        if bct == "C" and price < Cprice:
            Cct = ct
            Cprice = price
        if bct == "F" and price < Fprice:
            Fct = ct
            Fprice = price
    seatcost_model.yprice = Yprice
    seatcost_model.cprice = Cprice
    seatcost_model.fprice = Fprice
    seatcost_model.yct = Yct
    seatcost_model.cct = Cct
    seatcost_model.fct = Fct
    return seatcost_model



# getModelList
def analysis_Json(json_str, platform):
    json_object = json.loads(json_str)
    result_flightmodel_list = []

    status = json_object['status']
    dst = json_object['dst']
    cost = json_object['cost']
    date_str = json_object['date']
    org = json_object['org']
    datas = json_object['datas']

    flightData_all_list = datas[platform]

    try:
        for flightData_dict in flightData_all_list:
            try:
                seatcost_list = flightData_dict["price_info"]["seatcost"]
                seatcost_model = getLeastPrice(seatcost_list)

                flightmodel = FlightDataModel()
                flightmodel.fn = flightData_dict["flight_info"]["fn"]
                flightmodel.accode = flightData_dict["flight_info"]["accode"]
                flightmodel.org = org
                flightmodel.dst = dst
                flightmodel.departureairportcode = flightData_dict["flight_info"]["departureairportcode"]
                flightmodel.arrivingairportcode = flightData_dict["flight_info"]["arrivingairportcode"]
                flightmodel.src = platform
                flightmodel.flydate = date_str
                try:
                    flightmodel.cdate = flightData_dict["flight_info"]["updatetime"]
                except Exception as a:
                    flightmodel.cdate = ""
                flightmodel.departuretime = flightData_dict["flight_info"]["departuretime"]
                flightmodel.arrivingtime = flightData_dict["flight_info"]["arrivingtime"]

                flightmodel.leastpriceY = seatcost_model.yprice
                flightmodel.leastpriceC = seatcost_model.cprice
                flightmodel.leastpriceF = seatcost_model.fprice

                result_flightmodel_list.append(flightmodel)
            except Exception as e:
                logging.info(e)
    except Exception as e:
        logging.info(e)
    return result_flightmodel_list


def storeFlightModelList(obj_list, file_path):
    try:
        fr_out = open(file_path, "a")
        for obj in obj_list:
            obj_str = jsonpickle.encode(obj)
            fr_out.write(obj_str+"\n")
        return 1
    except Exception as a:
        return 0
    pass

def main(s_day, detal_days=30, platform="qunar", store_path="", folder_name=today_str):

    folder_path = store_path + "/" + folder_name
    if os.path.exists(folder_path):
        pass
    else:
        os.mkdir(folder_path)

    all_url_detail_list = getUrl(s_day, detal_days, platform)

    for url_detail_temp in all_url_detail_list:
        try:
            org = url_detail_temp[0]
            dst = url_detail_temp[1]
            file_name = url_detail_temp[3] + ".json"
            file_path = folder_path + "/" + file_name
            url = url_detail_temp[4]

            json_str = getJson(url)
            result_flightmodel_list = analysis_Json(json_str, platform)
            if len(result_flightmodel_list) > 0:
                storeFlightModelList(result_flightmodel_list, file_path)
        except Exception as e:
            logging.error(e)
            pass
    pass



mylock = threading.RLock()
class StoreData(threading.Thread):
    def __init__(self,s_day, detal_days=1, platform="qunar", store_path="", folder_name=today_str):
        threading.Thread.__init__(self)
        self.s_day = s_day
        self.platform = platform
        self.detal_days = detal_days
        self.store_path = store_path
        self.folder_name = folder_name
        pass

    def getUrl(self, s_day, detal_days, platform="ctrip"):
        url_obj = Url(platform)
        url_list = url_obj.getAllUrl(s_day, detal_days)
        return url_list

    def getJson(self, url, type=""):
        req_headers = {}
        req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        req_headers['Accept-Encoding'] = 'deflate'
        req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
        req_headers['Referer'] = "http://search.rsscc.cn"
        req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        request = urllib2.Request(url, headers=req_headers)

        page_content = urllib2.urlopen(request)
        article_json = page_content.read()
        if type == "json":
            # article_json = page_content.read()
            return json.loads(article_json)
        else:
            return article_json

    def analysis_Json(self, json_str, platform):
        json_object = json.loads(json_str)
        result_flightmodel_list = []

        status = json_object['status']
        dst = json_object['dst']
        cost = json_object['cost']
        date_str = json_object['date']
        org = json_object['org']
        datas = json_object['datas']

        flightData_all_list = datas[platform]

        try:
            for flightData_dict in flightData_all_list:
                try:
                    seatcost_list = flightData_dict["price_info"]["seatcost"]
                    seatcost_model = getLeastPrice(seatcost_list)

                    flightmodel = FlightDataModel()
                    flightmodel.fn = flightData_dict["flight_info"]["fn"]
                    flightmodel.accode = flightData_dict["flight_info"]["accode"]
                    flightmodel.org = org
                    flightmodel.dst = dst
                    flightmodel.departureairportcode = flightData_dict["flight_info"]["departureairportcode"]
                    flightmodel.arrivingairportcode = flightData_dict["flight_info"]["arrivingairportcode"]
                    flightmodel.src = platform
                    flightmodel.flydate = date_str
                    try:
                        flightmodel.cdate = flightData_dict["flight_info"]["updatetime"]
                    except Exception as a:
                        flightmodel.cdate = ""
                    flightmodel.departuretime = flightData_dict["flight_info"]["departuretime"]
                    flightmodel.arrivingtime = flightData_dict["flight_info"]["arrivingtime"]

                    flightmodel.leastpriceY = seatcost_model.yprice
                    flightmodel.leastpriceC = seatcost_model.cprice
                    flightmodel.leastpriceF = seatcost_model.fprice

                    result_flightmodel_list.append(flightmodel)
                except Exception as e:
                    logging.info(e)
        except Exception as e:
            logging.info(e)
        return result_flightmodel_list



    def storeFlightModelList(self, obj_list, file_path):
        try:
            fr_out = open(file_path, "a")
            for obj in obj_list:
                obj_str = jsonpickle.encode(obj)
                fr_out.write(obj_str+"\n")
            return 1
        except Exception as a:
            return 0
        pass

    def run(self):
        folder_path = self.store_path + "/" + self.folder_name
        if os.path.exists(folder_path):
            pass
        else:
            os.mkdir(folder_path)
        mylock.acquire()
        all_url_detail_list = self.getUrl(self.s_day, self.detal_days, self.platform)
        mylock.release()
        for url_detail_temp in all_url_detail_list:
            try:
                org = url_detail_temp[0]
                dst = url_detail_temp[1]
                file_name = url_detail_temp[3] + ".json"
                file_path = folder_path + "/" + file_name
                url = url_detail_temp[4]

                json_str = self.getJson(url)
                result_flightmodel_list = self.analysis_Json(json_str, self.platform)
                if len(result_flightmodel_list) > 0:
                    self.storeFlightModelList(result_flightmodel_list, file_path)
            except Exception as e:
                logging.error(e)
                pass
    pass


def storedata_multydays(s_day, detal_days=30, platform="qunar", base_path="", store_path=""):
    thread_list = []
    start_day = datetime.datetime.strptime(s_day, "%Y-%m-%d")
    date_list = []
    for i in range(0, detal_days):
        temop_date = start_day + datetime.timedelta(days=i)
        date_list.append(temop_date.strftime("%Y-%m-%d"))

    #prepare thread list
    for s_day_temp in date_list:
        if platform == "":
            store_path = base_path + "/qunar"
            thread_temp1 = StoreData(s_day_temp, 1, "qunar", store_path)
            thread_list.append(thread_temp1)
            store_path = base_path + "/ctrip"
            thread_temp2 = StoreData(s_day_temp, 1, "ctrip", store_path)
            thread_list.append(thread_temp2)
        else:
            thread_temp = StoreData(s_day_temp, 1, platform, store_path)
            thread_list.append(thread_temp)


    # start thread in threat_list
    for thread_temp in thread_list:
        thread_temp.start()



def multithread_main():
    thread_qunar = StoreData("2015-04-25", 1, "qunar", store_path="data/qunar")
    thread_ctrip = StoreData("2015-04-25", 1, "ctrip", store_path="data/ctrip")

    thread_ctrip.start()
    thread_qunar.start()
    pass




if __name__ == "__main__":

    # main("2015-04-24", 30, "qunar", store_path="/home/huolibi/data/flight_price/qunar")
    # main("2015-04-24", 30, "ctrip", store_path="/home/huolibi/data/flight_price/ctrip")
    # main("2015-04-25", 1, "qunar", store_path="data/qunar")
    # main("2015-04-25", 1, "ctrip", store_path="data/ctrip")
    # multithread_main()
    storedata_multydays(today_in, 30, base_path="/home/huolibi/data/flight_price")

    pass