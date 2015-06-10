__author__ = 'Administrator'

class PhoneNumber(object):
    def __init__(self):
        self.phone = ''

    def getlist(self):
        return ['phone']

    def getValues(self):
        return [self.phone]

    def __str__(self):
        out_str = "PhoneNumber:" + "\t" + self.phone
        return out_str

    def setValues(self, valueList):
        self.phone = str(valueList[0])

    def set0(self, value):
        self.phone = value

    def toString(self):
        out_Str = self.phone
        return out_Str

class PhoneDict():
    def __init__(self):
        self.phone = ""
        self.sheng = ""
        self.shi = ""


    def setValues(self,valueList):
        self.phone = valueList[0]
        self.sheng = valueList[1]
        self.shi  = valueList[2]

    def toString(self):
        out_Str = self.phone + "\t" + self.sheng + "\t" + self.shi
        return out_Str


class ThreeCodeDict():
    def __init__(self):
        self.code = ""
        self.name = ""

    def setValues(self,valueList):
        self.code = valueList[0]
        self.name = valueList[1]

    def toString(self):
        out_Str = str(self.code + "\t" + self.name)
        return out_Str

class SourcePhone(object):
    def __init__(self):
        self.phone = ''
        self.phoneid = ''

    def getlist(self):
        return ['phone', 'phoneid']

    def getValues(self):
        return [self.phone, self.phoneid]

    def __str__(self):
        out_str = "PhoneNumber:" + "\t" + self.phone + "\t" + self.phoneid
        return out_str

    def setValues(self, valueList):
        self.phone = str(valueList[0])
        self.phoneid = str(valueList[1])

    def set0(self, value):
        self.phone = value

    def set1(self, value):
        self.phoneid = value

    def toString(self):
        out_Str = self.phone + "\t" + self.phoneid
        return out_Str
        pass

class OrderDetail():

    def __init__(self):

        self.flyno = ""
        self.depcode = ""
        self.arrcode = ""
        self.phone = ""
        self.phoneid = ""

    def setValues(self, valueList):
        self.flyno = str(valueList[0])
        self.depcode = str(valueList[1])
        self.arrcode = str(valueList[2])
        self.phone = str(valueList[3])
        self.phoneid = str(valueList[4])


    def toString(self):
        out_str = self.flyno + "\t" + self.depcode + "\t" + self.arrcode + "\t" + self.phone + "\t" + self.phoneid
        return out_str
        pass


    pass

