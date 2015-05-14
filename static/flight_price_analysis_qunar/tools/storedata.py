__author__ = 'Administrator'
from url import Url
import json
import urllib2


class StoreFlightPrice(Url):
    def __init__(self):
        Url.__init__(self)

    def getJson(self,url):
        req_headers = {}
        req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        req_headers['Accept-Encoding'] = 'deflate'
        req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
        # req_headers['Connection'] = 'keep-alive'

        # req_headers['DNT'] = 1
        #req_headers['Host'] = 'hm.baidu.com'
        req_headers['Referer'] = "http://search.rsscc.cn"
        req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        request=urllib2.Request(url,headers=req_headers)

        page_content=urllib2.urlopen(request)
        article_json=page_content.read()
        return article_json

    def test_all(json_str):
        json_object = json.loads(json_str)
        status=json_object['status']
        dst=json_object['dst']
        cost=json_object['cost']
        date_str=json_object['date']
        org=json_object['org']
        datas=json_object['datas']
        # print(status,dst,cost,date_str,org,type(datas))
        # for i in datas.keys():
        #     print i
        flightData_all_list=datas["ctrip"]
        # print(data)

        for flightData_dict in flightData_all_list:


            seatcost_list=flightData_dict["price_info"]["seatcost"]
            seatcost_model=seatcost_analyse(seatcost_list)


            flightmodel=FlightDataModel()


            flightmodel.fn=flightData_dict["flight_info"]["fn"]
            flightmodel.accode=flightData_dict["flight_info"]["accode"]
            flightmodel.org=org
            flightmodel.dst=dst
            flightmodel.departureairportcode=flightData_dict["flight_info"]["departureairportcode"]
            flightmodel.arrivingairportcode=flightData_dict["flight_info"]["arrivingairportcode"]
            flightmodel.src="ctrip"
            flightmodel.flydate=date_str
            flightmodel.cdate=""
            flightmodel.departuretime=flightData_dict["flight_info"]["departuretime"]
            flightmodel.arrivingtime=flightData_dict["flight_info"]["arrivingtime"]


            flightmodel.leastpriceY=seatcost_model.yprice
            flightmodel.leastpriceC=seatcost_model.cprice
            flightmodel.leastpriceF=seatcost_model.fprice
            obj_store(flightmodel,"test.json")
            print(flightmodel.printstr())






    def getDataFromUrl(self,url):

        json_str=self.getJson(url)
        print(json_str)
        self.test_all(json_str)
        pass
