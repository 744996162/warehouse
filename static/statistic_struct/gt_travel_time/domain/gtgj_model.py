__author__ = 'Administrator'

class TravelTime():
    def __init__(self):
        self.uid = ""
        self.train_no = ""
        self.seat_name = ""
        self.price = ""
        self.depart_time = ""
        self.arrive_time = ""
        pass

    def __str__(self):
        out_str = "TravelTime:" + str(self.train_no) + "\t" + str(self.depart_time)
        return out_str


    def setValues(self, valueList):
        self.uid = str(valueList[0])
        self.train_no = str(valueList[1])
        self.seat_name = str(valueList[2])
        self.price = str(valueList[3])
        self.depart_time = str(valueList[4])
        self.arrive_time = str(valueList[5])

    def toString(self):
        out_str = str(self.uid) + "\t" + str(self.train_no) + "\t" + str(self.seat_name) + "\t" + str(self.price) + "\t" + str(self.depart_time) + "\t" + str(self.arrive_time)
        return out_str



if __name__ == '__main__':
    pass