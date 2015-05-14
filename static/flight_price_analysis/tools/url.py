#coding=utf-8
__author__ = 'zhangchao'
import datetime

from city import City


class Url(City):
    def __init__(self):
        City.__init__(self)
        # self.url_header="http://search.rsscc.cn/flight/domestic?src=ctrip"
        self.url_header="http://search.rsscc.cn/flight/domestic?src=qunar"

    def getUrl(self,org,dst,date_str):
        header=self.url_header
        url_out=header+"&_org="+org+"&_dst="+dst+"&date="+date_str
        return url_out

    def getFileName(self,org,dst,date_str):
        file_name=org+"_"+dst+"_"+date_str
        return file_name

    def getUrlCityName(self,org_name,dst_name,date_str):
        org=self.getCityCode(org_name)
        dst=self.getCityCode(dst_name)
        url_out=self.getUrl(org,dst,date_str)
        return url_out

    def getDateList(self,start_day_str,diff_day,date_format="%Y-%m-%d"):
        start_day = datetime.datetime.strptime(start_day_str,date_format)
        date_list=[]
        for i in range(0,diff_day):
            temop_date = start_day + datetime.timedelta(days=i)
            date_list.append(temop_date.strftime(date_format))
        return date_list


    def getUrlOneDay(self,date_str):
        two_city_list=self.getTwoCityList()
        url_list=[]
        for i in two_city_list:
            org=i[0]
            dst=i[1]
            url_out=self.getUrl(org,dst,date_str)
            file_name=self.getFileName(org,dst,date_str)
            url_list.append([org,dst,date_str,file_name,url_out])
        return url_list

    def getAllUrl(self,start_day_str,diff_day,date_format="%Y-%m-%d"):
        url_list=[]
        date_list=self.getDateList(start_day_str,diff_day,date_format="%Y-%m-%d")
        for date_str_temp in date_list:
            url_one_day=self.getUrlOneDay(date_str_temp)
            for url in url_one_day:
                url_list.append(url)
        return url_list



if __name__=="__main__":
    t=Url()
    url_list=t.getAllUrl("2015-02-03",10)
    # print(len(url_list))
    for i in url_list:
        print(i)
    print(len(url_list))

