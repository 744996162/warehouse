#ecoding=utf-8
__author__ = 'zhangchao'
import jsonpickle
import json
import datetime
# {
# 航班号:fn("GS7569")
# 航空公司编号:accode("GS")
# 起飞城市:org("BJS")
# 到达城市:dst("SHA")
# 起飞机场:departureairportcode("PEK")
# 到达机场:"arrivingairportcode"("SHA")
# 机票渠道:src("ctrip","qunaer")
# 飞机日期:date("20151113")
# 数据采集时间:cdate("20150204")
# 飞机起飞时间:departuretime("")
# 飞机到达时间:arrivingtime("")
# Y最低价:Yleastprice()
# C最低价:Cleastprice()
# F最低价:Fleastprice()
# }
class FlightDataModel(object):
    def __init__(self):
        self.fn=""
        self.accode=""
        self.org=""
        self.dst=""
        self.departureairportcode=""
        self.arrivingairportcode=""
        self.src=""
        self.flydate=""
        self.cdate=""
        self.departuretime=""
        self.arrivingtime=""
        self.leastpriceY=999999
        self.leastpriceC=999999
        self.leastpriceF=999999

    def __str__(self):
        string_out1 = "fn:"+str(self.fn)+","+"org:"+str(self.org)+","+"dst:"+str(self.dst)+","+"departureairportcode:"+str(self.departureairportcode)+","+"arrivingairportcode:"+str(self.arrivingairportcode)
        string_out2 = "flydate:"+str(self.flydate)+","+"leastpriceY:"+str(self.leastpriceY)+","+"leastpriceC:"+str(self.leastpriceC)+","+"leastpriceF:"+str(self.leastpriceF)
        string_out=string_out1+","+string_out2
        return string_out


    def toJson(self):
        dict_temp = {}
        if self.departuretime != "":
            try:
                deptime = datetime.datetime.utcfromtimestamp(int(self.departuretime[0:10]))
                dict_temp["departuretime"] = deptime
            except Exception as a:
                pass
        if self.arrivingtime != "":
            try:
                arrtime = datetime.datetime.utcfromtimestamp(int(self.arrivingtime[0:10]))
                dict_temp["arrivingtime"] = arrtime
            except Exception as a:
                pass
        if self.cdate != "":
            try:
                cdate_temp = datetime.datetime.utcfromtimestamp(int(self.cdate[0:10]))
                dict_temp["cdate"] = int(cdate_temp.strftime("%Y%m%d"))
            except Exception as a:
                pass

        try:
            flydate_temp = int(self.flydate[0:4] + self.flydate[5:7] + self.flydate[8:10])
            dict_temp["flydate"] = flydate_temp
        except Exception as a:
            pass


        dict_temp["fn"] = self.fn
        dict_temp["accode"] = self.accode
        dict_temp["org"] = self.org
        dict_temp["dst"] = self.dst
        dict_temp["departureairportcode"] = self.departureairportcode
        dict_temp["arrivingairportcode"] = self.arrivingairportcode
        dict_temp["src"] = self.src


        dict_temp["leastpriceY"] = self.leastpriceY
        dict_temp["leastpriceC"] = self.leastpriceC
        dict_temp["leastpriceF"] = self.leastpriceF

        return dict_temp
        pass




if __name__=="__main__":

    # fr_in=open("testFlightMode.txt")
    fr_out=open("testFlightMode.txt","a")
    t=FlightDataModel()
    obj_str=jsonpickle.encode(t)
    obj = jsonpickle.decode(obj_str)
    print(type(obj),obj.printstr())
    fr_out.write(obj_str+"\n")
    print(type(obj_str))
    fr_in=open("testFlightMode.txt")
    for line in fr_in.readlines():

    # print json_str
        json_object = json.loads(line)
        print(type(json_object),json_object)
    # pickle.dump(t,fr_out)
    # t.store("testFlightModel.txt")
    # dict_test={'fn':"",'accode':""}
    # for line in fr_in.readlines():
    #     print(type(line),line)
    #
    #     pass
    # print(dict_test,type(dict_test))

