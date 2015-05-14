__author__ = 'Administrator'
import datetime
class CheapModel(object):
    def __init__(self):
        self.flightnum = 0
        self.airlineno = ""
        self.hbgj_percent_cheap = 0
        self.xc_percent_cheap = 0
        self.qunar_percent_cheap = 0
        self.datatime = datetime.datetime.now()
        self.updatetime = datetime.datetime.now()

class ExpensiveModel(object):
    def __init__(self):
        self.flightnum = 0
        self.airlineno = ""
        self.hbgj_percent = 0
        self.xc_percent = 0
        self.qunar_percent = 0
        self.datatime = datetime.datetime.now()
        self.updatetime = datetime.datetime.now()











