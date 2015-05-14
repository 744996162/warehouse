#coding=utf-8
__author__ = 'zhangchao'
import datetime

def getDateList(start_day_str,diff_day,date_format="%Y-%m-%d"):
    start_day = datetime.datetime.strptime(start_day_str,date_format)
    date_list=[]
    for i in range(0,diff_day):
        temop_date = start_day + datetime.timedelta(days=i)
        date_list.append(temop_date.strftime(date_format))
    return date_list

def getFileName(org,dst,date):
    file_name=org+"_"+dst+"_"+date+".txt"
    return file_name

def getCityCode(city_name):
    airport_table="city_code"
    fr_in=open(airport_table)
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        if stringArr[0]==city_name:
            return stringArr[1]
    return 0

def getCityList():
    airport_table="city_code"
    fr_in=open(airport_table)
    city_list=[]
    for line in fr_in.readlines():
        stringArr=line.strip().split("\t")
        if stringArr!="":
            city_list.append(stringArr[1])
    return city_list

def getTwoCityList():
    two_city_list=[]
    t=getCityList()
    for i in t:
        for j in t:
            if i!=j:
                two_city_list.append([i,j])
    return two_city_list

def getUrlOneDay(date):
    two_city_list=getTwoCityList()
    url_list=[]
    url_header="http://search.rsscc.cn/flight/domestic?src=ctrip"
    for i in two_city_list:
        org=i[0]
        dst=i[1]
        url_out=url_header+"&_org="+org+"&_dst="+dst+"&date="+date
        url_list.append([org,dst,date,url_out])
    return url_list

def getAllUrl():

    pass


def url_search(org,dst,date):
    header="http://search.rsscc.cn/flight/domestic?src=ctrip"
    url_out=header+"&_org="+org+"&_dst="+dst+"&date="+date
    return url_out




if __name__=="__main__":
    # t=url_search("BJS","SHA","2015-02-05")
    # t=getCityCode("北京")
    # city_list=getCityList()
    # two_city_list=getTwoCityList()
    # url_all=getUrlOneDay("2015-02-03")


    # for i in url_all:
    #     print(i)

    s_date="2015-02-03"
    date_list=getDateList(s_date,30,date_format="%Y-%m-%d")
    for i in date_list:
        print i

    # print(t)
    # print(city_list)
    # print(two_city_list,len(two_city_list))
    pass