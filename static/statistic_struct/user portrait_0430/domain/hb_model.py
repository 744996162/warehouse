__author__ = 'Administrator'
class HbUser(object):
    def __init__(self):
        self.uid = ""
        self.cardno = ""
        self.phone = ""


    def setValues(self, valueList):
        '''
        :param valueList:
        :return:
        '''
        self.uid = str(valueList[0])
        self.cardno = str(valueList[1])
        self.phone = str(valueList[2])


    def __str__(self):
        out_str = "HBuser:" + "\t" + str(self.uid) + "\t" + str(self.phone)
        return out_str

class CardNo(object):
    def __init__(self):

        self.cardno = ""



    def setValues(self, valueList):
        '''
        :param valueList:
        :return:
        '''
        self.cardno = str(valueList[0])


    def __str__(self):
        out_str = "CardNo:" + "\t" + str(self.cardno)
        return out_str