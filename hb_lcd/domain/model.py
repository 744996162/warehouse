__author__ = 'Administrator'

class ActiveId(object):
    def __init__(self):
        self.uid = ''

    def __str__(self):
        out_str = "ActiveId:" + "\t" + str(self.uid)
        return out_str

    def setValues(self,valueList):
        self.uid = str(valueList[0])

    def getlist(self):
        return ['uid']

    def getValues(self):
        return [self.uid]

    def set0(self, value):
        self.uid = value


class NewUsersId(object):
    def __init__(self):
        self.uid = ''

    def __str__(self):
        out_str = "NewUsersId:" + "\t" + str(self.uid)
        return out_str

    def setValues(self, valueList):
        self.uid = str(valueList[0])

    def getlist(self):
        return ['uid']

    def getValues(self):
        return [self.uid]

    def set0(self, value):
        self.uid = value