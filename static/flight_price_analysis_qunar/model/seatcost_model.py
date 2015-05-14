#ecoding=utf-8
__author__ = 'zhangchao'

class SeatCostModel(object):
    def __init__(self):
        self.yprice=999999
        self.cprice=999999
        self.fprice=999999
        self.yct=""
        self.cct=""
        self.fct=""


    def printstr(self):
        string_out1="yprice:"+str(self.yprice)+","+"cprice:"+str(self.cprice)+","+"fprice:"+str(self.fprice)
        string_out2="yct:"+str(self.yct)+","+"cct:"+str(self.cct)+","+"fct:"+str(self.fct)
        string_out=string_out1+","+string_out2
        return string_out