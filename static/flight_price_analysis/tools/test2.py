#coding=utf-8
__author__ = 'zhangchao'
import sys
import json
import bs4
import urllib2
import time
import datetime
import jsonpickle
import requests
from city import City
from url import Url

from model.seatcost_model import SeatCostModel
from model.flight_model import FlightDataModel
reload(sys)
sys.setdefaultencoding('utf-8')

def getJson(url):
    #提取出json
    req_headers = {}
    req_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    req_headers['Accept-Encoding'] = 'deflate'
    req_headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
    req_headers['Connection'] = 'keep-alive'
    req_headers['Cookie'] = 'Hm_lvt_339d749938744acd9bea875d1d494696=1402974179,1403052976,1403086979,1403139829; Hm_lpvt_339d749938744acd9bea875d1d494696=1403165411'
    req_headers['DNT'] = 1
    #req_headers['Host'] = 'hm.baidu.com'
    req_headers['Referer'] = 'http://www.zhihudaily.com/'
    req_headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    request=urllib2.Request(url,headers=req_headers)
    page_content=urllib2.urlopen(request)

    article_json=page_content.read()
    return article_json

def test():
    url="http://search.rsscc.cn/flight/domestic?src=ctrip&_org=TSN&_dst=HRB&date=2015-03-04"
    file_in=open("json_test")
    # json_str=getJson(url)
    json_str=file_in.read()
    print json_str
    json_object = json.loads(json_str)
    print(json_object)
    for i in json_object.keys():
        print i

    status=json_object['status']
    dst=json_object['_dst']
    cost=json_object['cost']
    date_str=json_object['date']
    org=json_object['_org']
    datas=json_object['datas']
    print(status,dst,cost,date_str,org,type(datas))
    # for i in datas.keys():
    #     print i
    data=datas["ctrip"]
    # print(data)
    for i in data:
        # print(type(i))
        price_info_dict=i["price_info"]
        flight_info_dict=i["flight_info"]
        for price_info_key in price_info_dict.keys():
            # print "'price_info_key'"
            print price_info_key
        for flight_info_key in flight_info_dict.keys():
            # print "'flight_info_key'"
            print flight_info_key

def test2():
    file_in=open("json_test")
    json_str=file_in.read()
    # print json_str
    json_object = json.loads(json_str)
    status=json_object['status']
    dst=json_object['_dst']
    cost=json_object['cost']
    date_str=json_object['date']
    org=json_object['_org']
    datas=json_object['datas']

    data=datas["ctrip"]

    for i in data:
        print(type(i),i)
        price_info_dict=i["price_info"]
        flight_info_dict=i["flight_info"]

        flight_info_fn=flight_info_dict["fn"]
        flight_info_accode=flight_info_dict["accode"]
        flight_info_arrivingairportcode=flight_info_dict["arrivingairportcode"]
        flight_info_departureairportcode=flight_info_dict["departureairportcode"]
        flight_info_arrivingtime=flight_info_dict["arrivingtime"]
        flight_info_departuretime=flight_info_dict["departuretime"]
        flight_info_planecode=flight_info_dict["planecode"]
        flight_info_updatetime=flight_info_dict["updatetime"]

        # print(type(price_info_dict),price_info_dict)
        seatcost_dict=price_info_dict["seatcost"]
        # print(seatcost_dict)
        # print(seatcost_dict,seatcost_dict.printstr)
        seat_cost_model=seatcost_analyse(seatcost_dict)

        # print(seat_cost_model,seat_cost_model.printstr())
        # for seat_cost in seatcost_dict:
        #     print(seat_cost)
            # seat_cost_model=seatcost_analyse(seat_cost)
            # print seat_cost["bct"],seat_cost["ct"],seat_cost["price"]

        # stringout1=flight_info_fn+","+flight_info_accode+","+flight_info_arrivingairportcode+","+flight_info_departureairportcode
        # stringout2=flight_info_arrivingtime+","+flight_info_departuretime+","+flight_info_planecode+","+flight_info_updatetime
        # stringout=stringout1+","+stringout2
        # print(stringout,seatcost_dict)



def seatcost_analyse(seatcost_list):
    # from model.seatcost_model import SeatCostModel
    seatcost_model=SeatCostModel()
    # seatcost_list=[{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]
    Yprice=999999
    Cprice=999999
    Fprice=999999
    Yct=""
    Cct=""
    Fct=""

    for seatcost in seatcost_list:
        bct=str(seatcost["bct"])
        ct=str(seatcost["ct"])
        price=int(seatcost["price"])
        # print(bct,ct,"Y",price)
        if bct=="Y" and price<Yprice:
            Yct=ct
            Yprice=price
        if bct=="C" and price<Cprice:
            Cct=ct
            Cprice=price
        if bct=="F" and price<Fprice:
            Fct=ct
            Fprice=price
    seatcost_model.yprice=Yprice
    seatcost_model.cprice=Cprice
    seatcost_model.fprice=Fprice
    seatcost_model.yct=Yct
    seatcost_model.cct=Cct
    seatcost_model.fct=Fct
    return seatcost_model

def price_info_analyse():
    dict_str={u'leastprice': u'196', u'updatetime': u'1422874948144', u'srcUrl': u'http://flights.ctrip.com/booking/TSN-HRB-day-1.html', u'seatcost': [{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]}
    seatcost_list=dict_str["seatcost"]
    seatcost_model=seatcost_analyse(seatcost_list)
    print(seatcost_model.printstr())


    # for seatcost in seatcost_list:
    #     print(type(seatcost),seatcost)
    # print(seatcost_list)
    # print(type(dict_str))

def flightinfo_analyse():

    flight_data_obj=FlightDataModel()
    flightData_str={u'price_info': {u'leastprice': u'196', u'updatetime': u'1422874948144', u'srcUrl': u'http://flights.ctrip.com/booking/TSN-HRB-day-1.html', u'seatcost': [{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]}, u'flight_info': {u'proximaterate': u'0.0', u'accode': u'GS', u'departuretime': u'1425425400000', u'oilfee': u'30', u'planecode': u'32G', u'departureairportcode': u'TSN', u'tax': u'50', u'updatetime': u'1422874948144', u'arrivingtime': u'1425434100000', u'islocaltime': u'true', u'arrivingairportcode': u'HRB', u'fn': u'GS6663', u'duringminutes': u'0'}, u'static_info': {}}
    price_info_dict=flightData_str["price_info"]


    flight_info_dict=flightData_str["flight_info"]

    flight_info_fn=flight_info_dict["fn"]
    flight_info_accode=flight_info_dict["accode"]
    flight_info_arrivingairportcode=flight_info_dict["arrivingairportcode"]
    flight_info_departureairportcode=flight_info_dict["departureairportcode"]
    flight_info_arrivingtime=flight_info_dict["arrivingtime"]
    flight_info_departuretime=flight_info_dict["departuretime"]
    flight_info_planecode=flight_info_dict["planecode"]
    flight_info_updatetime=flight_info_dict["updatetime"]

    seatcost_dict=price_info_dict["seatcost"]
    seat_cost_model=seatcost_analyse(seatcost_dict)
    print(seat_cost_model,seat_cost_model.printstr())



    # print(seatcost_dict)
    # print(seatcost_dict,seatcost_dict.printstr)


    flight_data_obj.fn=flight_info_fn
    flight_data_obj.accode=flight_info_dict["accode"]
    flight_data_obj.org=""
    flight_data_obj.dst=""
    flight_data_obj.departuretime=flight_info_dict["departuretime"]
    flight_data_obj.arrivingtime=flight_info_dict["arrivingtime"]

    flight_data_obj.departureairportcode=flight_info_dict["departureairportcode"]
    flight_data_obj.arrivingairportcode=flight_info_dict["arrivingairportcode"]
    flight_data_obj.src="ctrip"
    flight_data_obj.flydate=""
    flight_data_obj.cdate=""
    flight_data_obj.departuretime=""
    flight_data_obj.arrivingtime=""
    flight_data_obj.leastpriceY=999999
    flight_data_obj.leastpriceC=999999
    flight_data_obj.leastpriceF=999999



def time_change(seconds):
    gmt_time = time.ctime(seconds)
    # gmt_time = time.gmtime(seconds)
    print time.strftime("%Y-%m-%d %H:%M:%S", gmt_time)
    pass


def test_all(json_str):
    # today=datetime.datetime.now()
    #
    # file_in1=open("json_test")
    # file_in=open("domestic.json")
    #
    # json_str=file_in.read()

    json_object = json.loads(json_str)
    print(type(json_object))
    # print(json_object)
    # for i in json_object.keys():
    #     print i

    status=json_object['status']
    dst=json_object['_dst']
    cost=json_object['cost']
    date_str=json_object['date']
    org=json_object['_org']
    datas=json_object['datas']
    # print(status,_dst,cost,date_str,_org,type(datas))
    # for i in datas.keys():
    #     print i
    flightData_all_list=datas["ctrip"]
    # print(data)
    # print(flightData_str)
    try:
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
            store_state=obj_store(flightmodel,"test.json")
            return store_state
    except Exception as e:
        print(e)
        return 0





        # print(flightData_dict)
        # print(seatcost_analyse(flightData_dict["price_info"]["seatcost"]).printstr(),flightData_dict["price_info"]["seatcost"])
        # for seatcost_list in flightData_dict["seatcost"]:
        #     print(seatcost_list)
        # print(type(i))
        # price_info_dict=i["price_info"]
        # flight_info_dict=i["flight_info"]


def store_date(org,dst,date_str):
    url=Url()
    url1=url.getUrl(org,dst,date_str)

    print(url1)

    pass

def getDataFromUrl():
    url="http://search.rsscc.cn/flight/domestic?src=ctrip&_org=BJS&_dst=SHA&date=2015-02-08"
    json_str=getJson(url)
    print(json_str)
    test_all(json_str)
    pass

def obj_store(obj,file_path):
    try:
        fr_out=open(file_path,"a")
        obj_str=jsonpickle.encode(obj)
        fr_out.write(obj_str+"\n")
        return 1
    except Exception as a:
        return 0





if __name__=="__main__":
    # test2()
    seat_list=[{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]
    # seatcost_dic={u'leastprice': u'196', u'updatetime': u'1422874948144', u'srcUrl': u'http://flights.ctrip.com/booking/TSN-HRB-day-1.html', u'seatcost': [{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]}
    # flightData_str={'price_info': {'leastprice': '196', 'pdatetime': '1422874948144', 'srcrl': 'http://flights.ctrip.com/booking/TSN-HRB-day-1.html', 'seatcost': [{'refndcondition': '\4e0d\652f\6301\4ea7\54c1\9000\8ba2', 'rerotecondition': '\4e0d\652f\6301\4ea7\54c1\66f4\6539', 'needapplication': 'false', 'copon': '0', 'money': 'CNY', 'price': '196', 'pdatetime': '1422874948144', 'terminal': '3', 'tgqflag': '0', 'rate': '0.2', 'bct': 'Y', 'forceinsrance': 'tre', 'endorsementcondition': '\4e0d\5f97\4ea7\54c1\7b7e\8f6c', 'seatleft': 'A', 'insrance': '30', 'ct': 'Z'}, {'refndcondition': '\4e0d\5f97\9000\7968', 'rerotecondition': '\4e0d\5f97\66f4\6539', 'needapplication': 'false', 'copon': '0', 'money': 'CNY', 'price': '200', 'remark': '\4e0d\53c2\52a0\91cc\7a0b\7d2f\79ef', 'terminal': '3', 'tgqflag': '0', 'rate': '0.2', 'forceinsrance': 'false', 'bct': 'Y', 'pdatetime': '1422874948144', 'endorsementcondition': '\4e0d\5f97\7b7e\8f6c', 'seatleft': 'A', 'insrance': '0', 'ct': 'Z'}, {'refndcondition': '\8d77\98de\524d24\5c0f\65f6\4ee5\5916\529e\7406\9700\6536\53d6\7968\9762\4ef710\ff05\7684\9000\7968\8d39\ff0c24\5c0f\65f6\4ee5\5185\53ca\8d77\98de\540e\529e\7406\9700\6536\53d6\7968\9762\4ef720\ff05\7684\9000\7968\8d39\ff08\5a74\513f\514d\6536\9000\7968\8d39\ff09\3002', 'rerotecondition': '\8d77\98de\524d24\5c0f\65f6\ff08\542b\ff09\4ee5\5916\529e\7406\9700\6536\53d6\7968\9762\4ef710%\7684\53d8\66f4\8d39\ff0c24\5c0f\65f6\4ee5\5185\53ca\8d77\98de\540e\9700\6536\53d6\7968\9762\4ef720%\7684\53d8\66f4\8d39\3002\5347\8231\8d39\4e0e\6539\671f\8d39\540c\65f6\53d1\751f\65f6\ff0c\9700\540c\65f6\6536\53d6\3002', 'rfndamtper': '10', 'copon': '0', 'money': 'CNY', 'price': '990', 'pdatetime': '1422874948144', 'reshdamtper': '10', 'terminal': '3', 'tgqflag': '7', 'rate': '1.0', 'needapplication': 'false', 'bct': 'Y', 'forceinsrance': 'false', 'endorsementcondition': '\5141\8bb8\7b7e\8f6c\ff0c\5982\53d8\66f4\540e\627f\8fd0\4eba\9002\7528\7968\4ef7\9ad8\4e8e\5929\6d25\822a\7968\4ef7\ff0c\9700\8865\9f50\5dee\989d\540e\8fdb\884c\53d8\66f4\ff0c\82e5\4f4e\4e8e\5929\6d25\822a\7968\4ef7\ff0c\5dee\989d\4e0d\9000\3002', 'seatleft': 'A', 'insrance': '0', 'ct': 'Y'}]}, 'flight_info': {'proximaterate': '0.0', 'accode': 'GS', 'departretime': '1425425400000', 'oilfee': '30', 'planecode': '32G', 'departreairportcode': 'TSN', 'tax': '50', 'pdatetime': '1422874948144', 'arrivingtime': '1425434100000', 'islocaltime': 'tre', 'arrivingairportcode': 'HRB', 'fn': 'GS6663', 'dringmintes': '0'}, 'static_info': {}}
    flightData_str={u'price_info': {u'leastprice': u'196', u'updatetime': u'1422874948144', u'srcUrl': u'http://flights.ctrip.com/booking/TSN-HRB-day-1.html', u'seatcost': [{u'refundcondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u9000\u8ba2', u'reroutecondition': u'\u4e0d\u652f\u6301\u4ea7\u54c1\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'196', u'updatetime': u'1422874948144', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'bct': u'Y', u'forceinsurance': u'true', u'endorsementcondition': u'\u4e0d\u5f97\u4ea7\u54c1\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'30', u'ct': u'Z'}, {u'refundcondition': u'\u4e0d\u5f97\u9000\u7968', u'reroutecondition': u'\u4e0d\u5f97\u66f4\u6539', u'needapplication': u'false', u'coupon': u'0', u'money': u'CNY', u'price': u'200', u'remark': u'\u4e0d\u53c2\u52a0\u91cc\u7a0b\u7d2f\u79ef', u'terminal': u'3', u'tgqflag': u'0', u'rate': u'0.2', u'forceinsurance': u'false', u'bct': u'Y', u'updatetime': u'1422874948144', u'endorsementcondition': u'\u4e0d\u5f97\u7b7e\u8f6c', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Z'}, {u'refundcondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710\uff05\u7684\u9000\u7968\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef720\uff05\u7684\u9000\u7968\u8d39\uff08\u5a74\u513f\u514d\u6536\u9000\u7968\u8d39\uff09\u3002', u'reroutecondition': u'\u8d77\u98de\u524d24\u5c0f\u65f6\uff08\u542b\uff09\u4ee5\u5916\u529e\u7406\u9700\u6536\u53d6\u7968\u9762\u4ef710%\u7684\u53d8\u66f4\u8d39\uff0c24\u5c0f\u65f6\u4ee5\u5185\u53ca\u8d77\u98de\u540e\u9700\u6536\u53d6\u7968\u9762\u4ef720%\u7684\u53d8\u66f4\u8d39\u3002\u5347\u8231\u8d39\u4e0e\u6539\u671f\u8d39\u540c\u65f6\u53d1\u751f\u65f6\uff0c\u9700\u540c\u65f6\u6536\u53d6\u3002', u'rfndamtper': u'10', u'coupon': u'0', u'money': u'CNY', u'price': u'990', u'updatetime': u'1422874948144', u'reshdamtper': u'10', u'terminal': u'3', u'tgqflag': u'7', u'rate': u'1.0', u'needapplication': u'false', u'bct': u'Y', u'forceinsurance': u'false', u'endorsementcondition': u'\u5141\u8bb8\u7b7e\u8f6c\uff0c\u5982\u53d8\u66f4\u540e\u627f\u8fd0\u4eba\u9002\u7528\u7968\u4ef7\u9ad8\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u9700\u8865\u9f50\u5dee\u989d\u540e\u8fdb\u884c\u53d8\u66f4\uff0c\u82e5\u4f4e\u4e8e\u5929\u6d25\u822a\u7968\u4ef7\uff0c\u5dee\u989d\u4e0d\u9000\u3002', u'seatleft': u'A', u'insurance': u'0', u'ct': u'Y'}]}, u'flight_info': {u'proximaterate': u'0.0', u'accode': u'GS', u'departuretime': u'1425425400000', u'oilfee': u'30', u'planecode': u'32G', u'departureairportcode': u'TSN', u'tax': u'50', u'updatetime': u'1422874948144', u'arrivingtime': u'1425434100000', u'islocaltime': u'true', u'arrivingairportcode': u'HRB', u'fn': u'GS6663', u'duringminutes': u'0'}, u'static_info': {}}
    store_date("BJS","SHA","2015-02-06")
    # getDataFromUrl()
    # test_all()
    # price_info_dict=flightData_str["price_info"]
    # seatcost_list2=price_info_dict["seatcost"]
    # # print(seatcost_analyse(seat_list))
    # # print(seatcost_analyse(seatcost_list2))
    # for i in seatcost_list2:
    #     pass
    # print(seatcost_list2)

    # for seat_list_temp in seatcost_dict:
    #     t=seatcost_analyse(seat_list_temp)
    #     print(t.printstr())
    # print(type(flighData_str))
    # print(type(dict_str))
    # price_info_analyse()
    # md=seatcost_analyse(t)
    # print(md.printstr())
    # t1=1422874948
    # t3=1423014159
    # t2=1309433893
    # t4=1415743208
    # print(time.ctime(t4))
    # time_change(t3)














    # print(type(json_str),json_str)
    # json_object=json.loads(json_str)
    # dump_obj=json.dumps(jsonobject)

    # for i in json_object.key():
    #     print i


    # data = json.loads(article_json)
    # article_date=data['date']
    # article_json= data['stories']
    # article_dumps = json.dumps(article_json)
    # article_list=json.loads(article_dumps)






    pass