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

    def printstr(self):
        string_out1="fn:"+str(self.fn)+","+"_org:"+str(self.org)+","+"_dst:"+str(self.dst)+","+"departureairportcode:"+str(self.departureairportcode)+","+"arrivingairportcode:"+str(self.arrivingairportcode)
        string_out2="_flydate:"+str(self.flydate)+","+"leastpriceY:"+str(self.leastpriceY)+","+"leastpriceC:"+str(self.leastpriceC)+","+"leastpriceF:"+str(self.leastpriceF)
        string_out=string_out1+","+string_out2
        return string_out

    # def store(self,_file_path):
    #     fr_out=open(_file_path,"a")
    #     pickle.dump(self, fr_out)

        # fr_out=open(_file_path,"a")
        # string_out1="{"+"'fn'"+":"+str(self.fn)+","+"'accode'"+":"+str(self.accode)
        # fr_out.write(string_out1+"\n")

        # self._org=""
        # self._dst=""
        # self.departureairportcode=""
        # self.arrivingairportcode=""
        # self.src=""
        # self._flydate=""
        # self._cdate=""
        # self.departuretime=""
        # self.arrivingtime=""
        # self.leastpriceY=999999
        # self.leastpriceC=999999
        # self.leastpriceF=999999


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

