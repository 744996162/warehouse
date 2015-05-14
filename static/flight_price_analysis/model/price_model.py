#ecoding=utf-8
__author__ = 'zhangchao'
import pickle
import jsonpickle
import json
# {
# 航班号:fn("GS7569")
# 航空公司编号:accode("GS")
# 起飞城市:_org("BJS")
# 到达城市:_dst("SHA")
# 起飞机场:departureairportcode("PEK")
# 到达机场:"arrivingairportcode"("SHA")
# 机票渠道:src("ctrip","qunaer")
# 飞机日期:date("20151113")
# 数据采集时间:_cdate("20150204")
# 飞机起飞时间:departuretime("")
# 飞机到达时间:arrivingtime("")
# 仓位cabin("Y" "C" "F")
# 最低价:leastprice()
# 时间段编号:flytimecode=0

class PriceModel(object):
    def __init__(self):
        self.fn = ""
        self.accode = ""
        self.org = ""
        self.dst = ""
        self.departureairportcode = ""
        self.arrivingairportcode = ""
        self.src = ""
        self.flydate = ""
        self.cdate = ""
        self.departuretime = ""
        self.arrivingtime = ""
        self.cabin=""
        self.leastprice=999999
        self.flytimecode=0

    def printstr(self):
        string_out1 = "fn:"+str(self.fn)+","+"_org:"+str(self.org)+","+"_dst:"+str(self.dst)+","+"departcode:"+str(self.departureairportcode)+","+"arrcode:"+str(self.arrivingairportcode)
        string_out2 = "_flydate:"+str(self.flydate)+","+"leastprice:"+str(self.leastprice)+","+"_cabin:"+str(self.cabin)
        string_out = string_out1+","+string_out2
        return string_out

if __name__ == "__main__":
    pass
