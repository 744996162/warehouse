__author__ = 'Administrator'
from url import Url
import os
import urllib2
import jsonpickle
import json
import logging
from model.seatcost_model import SeatCostModel
from model.flight_model import FlightDataModel
import datetime

def getUrl(date_str,detal_days=30):
    url_obj=Url()
    url_list=url_obj.getAllUrl(date_str,detal_days)
    return url_list

def getJson(url):
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

def objStore(obj,file_path):
    try:
        fr_out=open(file_path,"a")
        obj_str=jsonpickle.encode(obj)
        fr_out.write(obj_str+"\n")
        return 1
    except Exception as a:
        return 0

def store_all(json_str,store_path):
    count_right=0
    count_wrong=0
    # logger = logging.getLogger('mylogger')
    # logger.setLevel(logging.DEBUG)
    # fh = logging.FileHandler('store0206.log')
    # fh.setLevel(logging.DEBUG)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # logger.addHandler(fh)
    # logger.addHandler(ch)

    json_object = json.loads(json_str)

    status=json_object['status']
    dst=json_object['dst']
    cost=json_object['cost']
    date_str=json_object['date']
    org=json_object['org']
    datas=json_object['datas']

    flightData_all_list=datas["ctrip"]

    try:
        for flightData_dict in flightData_all_list:
            try:
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
                flightmodel.cdate=flightData_dict["flight_info"]["updatetime"]
                flightmodel.departuretime=flightData_dict["flight_info"]["departuretime"]
                flightmodel.arrivingtime=flightData_dict["flight_info"]["arrivingtime"]

                flightmodel.leastpriceY=seatcost_model.yprice
                flightmodel.leastpriceC=seatcost_model.cprice
                flightmodel.leastpriceF=seatcost_model.fprice
                # print(flightmodel.printstr())
                store_state=objStore(flightmodel,store_path)
                # return store_state
                if store_state==1:
                    count_right=count_right+1
                    # logger.debug(flightmodel.printstr())
                else:
                    count_wrong=count_wrong+1
                    # logger.error(flightmodel.printstr())
            except Exception as e:
                pass
                # logger.error(e)
                # logger

    except Exception as e:
        pass
        # print(e)
        # logger.error(e)
        # return 0
    return count_right,count_wrong

# def getFileName(org,dst,date):
#     file_name=org+"_"+dst+"_"+date+".json"
#     return file_name

def get_one_store_test():
    url_list=getUrl("2015-02-07",detal_days=30)
    print(url_list[0])
    org=url_list[0][0]
    dst=url_list[0][1]
    file_name=url_list[0][3]+".json"
    url=url_list[0][4]
    print(url)
    json_str=getJson(url)
    state=store_all(json_str,file_name)
    print(state)


def getToday():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=0)
    return yes_time.strftime('%Y%m%d')

def get_all_store_test():

    today=getToday()
    file_path=today

    if os.path.exists(today):
        pass
    else:
        os.mkdir(today)


    # logger = logging.getLogger('mylogger')
    # logger.setLevel(logging.INFO)
    # fh = logging.FileHandler('store0206.log')
    # fh.setLevel(logging.INFO)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # logger.addHandler(fh)
    # logger.addHandler(ch)

    url_detail_list=getUrl("2015-02-07",detal_days=30)
    for url_temp in url_detail_list:

        try:
            org=url_temp[0]
            dst=url_temp[1]
            file_name=file_path+"/"+url_temp[3]+".json"
            url=url_temp[4]

            json_str=getJson(url)
            state=store_all(json_str,file_name)
            print(state)
            # logger.error(state)
        except Exception as e:
            print(e)
    pass

if __name__=="__main__":
    get_one_store_test()