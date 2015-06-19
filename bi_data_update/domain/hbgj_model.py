__author__ = 'Administrator'
class BaseModel(object):

    def __init__(self):
        pass


class New_users(object):
    def __init__(self):
        self.s_day = ''
        self.new_users = 0
        self.new_users_ios = 0
        self.new_users_android = 0

    def getlist(self):
        return ['s_day', 'new_users', 'new_users_ios', 'new_users_android']

    def getValues(self):
        return [self.s_day, self.new_users, self.new_users_ios, self.new_users_android]

    def __str__(self):
        out_str = "HB_New_users:" + "\t" + self.s_day + "\t" + str(self.new_users)
        return out_str

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.new_users = int(valueList[1])
        self.new_users_ios = int(valueList[2])
        self.new_users_android = int(valueList[1]) - int(valueList[2])
        pass

    def set0(self, value):
        self.s_day = value

    def set1(self, value):
        self.new_users = value

    def set2(self, value):
        self.new_users_ios = value

    def set3(self, value):
        self.new_users_android = value

class New_consumers(object):
    def __init__(self):
        self.s_day = ''
        self.new_consumers = 0
        self.new_consumers_ios = 0
        self.new_consumers_android = 0

    def getlist(self):
        return ['s_day', 'new_consumers', 'new_consumers_ios', 'new_consumers_android']

    def getValues(self):
        return [self.s_day, self.new_consumers, self.new_consumers_ios, self.new_consumers_android]

    def __str__(self):
        out_str = "HB_New_consumers:" + "\t" + self.s_day + "\t" + str(self.new_consumers)
        return out_str

    def set0(self, value):
        self.s_day = value

    def set1(self, value):
        self.new_consumers = value

    def set2(self, value):
        self.new_consumers_ios = value

    def set3(self, value):
        self.new_consumers_android = value

class Active_users(object):
    def __init__(self):
        self.s_day = ''
        self.active_users = 0
        self.active_users_ios = 0
        self.active_users_android = 0

    def __str__(self):
        out_str = "HB_active_users:" + "\t" + str(self.s_day) + "\t" + str(self.active_users) \
                  + "\t" + str(self.active_users_ios) + "\t" + str(self.active_users_android)
        return out_str

    def getlist(self):
        return ['s_day', 'active_users', 'active_users_ios', 'active_users_android']

    def getValues(self):
        return [self.s_day, self.active_users, self.active_users_ios, self.active_users_android]


    def set0(self, value):
        self.s_day = value

    def set1(self, value):
        self.active_users = value

    def set2(self,value):
        self.active_users_ios = value

    def set3(self,value):
        self.active_users_android = value

class Consumers(object):
    def __init__(self):
        self.s_day = ''
        self.consumers = 0
        self.consumers_ios = 0
        self.consumers_android = 0

    def __str__(self):
        out_str = "HB_consumers:" + "\t" + self.s_day + "\t" + str(self.consumers)
        return out_str

    def getlist(self):
        return ['s_day', 'consumers', 'consumers_ios', 'consumers_android']

    def getValues(self):
        return [self.s_day, self.consumers, self.consumers_ios, self.consumers_android]

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.consumers = int(valueList[1])
        self.consumers_ios = int(valueList[2])
        self.consumers_android = int(valueList[1]) - int(valueList[2])

    def set0(self, value):
        self.s_day = value

    def set1(self, value):
        self.consumers = value

    def set2(self, value):
        self.consumers_ios = value

    def set3(self, value):
        self.consumers_android = value


class Orders(object):
    def __init__(self):
        self.s_day = ''
        self.ticket_num = 0
        self.order_num = 0
        self.ticket_num_gt = 0
        self.order_num_gt = 0

    def __str__(self):
        out_str = "HB_orders:" + "\t" + self.s_day + "\t" + str(self.ticket_num)
        return out_str

    def getlist(self):
        return ['s_day', 'ticket_num', 'order_num', 'ticket_num_gt', 'order_num_gt']

    def getValues(self):
        return [self.s_day, self.ticket_num, self.order_num, self.ticket_num_gt, self.order_num_gt]

    def setValues(self, valueList):
        self.s_day = str(valueList[0])
        self.ticket_num = int(valueList[1])
        self.order_num = int(valueList[2])
        self.ticket_num_gt = int(valueList[3])
        self.order_num_gt = int(valueList[4])

    def set0(self, value):
        self.s_day = value

    def set1(self, value):
        self.ticket_num = value

    def set2(self, value):
        self.order_num = value

    def set3(self, value):
        self.ticket_num_gt = value

    def set4(self, value):
        self.order_num_gt = value

def test():
    t = New_consumers()
    s = t.getlist()
    print(s[0], s[1], s[2])
    pass

if __name__ == '__main__':
    test()