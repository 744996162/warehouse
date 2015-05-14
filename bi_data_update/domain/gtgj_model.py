__author__ = 'Administrator'

class New_users(object):
    def __init__(self):
        self.s_day = ''
        self.new_users = 0
        self.new_users_ios = 0
        self.new_users_android = 0

    def __str__(self):
        out_str = "GT_New_users:" + "\t" + self.s_day + "\t" + str(self.new_users)
        return out_str

    def getlist(self):
        return ['s_day', 'new_users', 'new_users_ios', 'new_users_android']

    def getValues(self):
        return [self.s_day, self.new_users, self.new_users_ios, self.new_users_android]

    def set0(self,value):
        self.s_day = value

    def set1(self,value):
        self.new_users=value

    def set2(self,value):
        self.new_users_ios=value

    def set3(self, value):
        self.new_users_android = value

class New_consumers(object):
    def __init__(self):
        self.s_day = ''
        self.new_consumers=0
        self.new_consumers_ios=0
        self.new_consumers_android=0

    def __str__(self):
        out_str = "GT_New_consumers:" + "\t" + self.s_day + "\t" + str(self.new_consumers)
        return out_str

    def getlist(self):
        return ['s_day', 'new_consumers', 'new_consumers_ios', 'new_consumers_android']

    def getValues(self):
        return [self.s_day, self.new_consumers, self.new_consumers_ios, self.new_consumers_android]

    def set0(self,value):
        self.s_day=value

    def set1(self,value):
        self.new_consumers=value

    def set2(self,value):
        self.new_consumers_ios=value

    def set3(self,value):
        self.new_consumers_android=value

class Active_users(object):
    def __init__(self):
        self.s_day = ''
        self.active_users = 0
        self.active_users_ios = 0
        self.active_users_android = 0

    def __str__(self):
        out_str = "GT_Active_users:" + "\t" + self.s_day + "\t" + str(self.active_users) + "\t" + str(self.active_users_ios)
        return out_str

    def getlist(self):
        return ['s_day', 'active_users', 'active_users_ios', 'active_users_android']

    def getValues(self):
        return [self.s_day, self.active_users, self.active_users_ios, self.active_users_android]

    def set0(self,value):
        self.s_day=value

    def set1(self,value):
        self.active_users=value

    def set2(self,value):
        self.active_users_ios=value

    def set3(self,value):
        self.active_users_android=value


class Consumers(object):
    def __init__(self):
        self.s_day = ''
        self.consumers = 0
        self.consumers_ios = 0
        self.consumers_android = 0

    def __str__(self):
        out_str = "GT_Consumers:" + "\t" + self.s_day + "\t" + str(self.consumers)
        return out_str


    def getlist(self):
        return ['s_day', 'consumers', 'consumers_ios', 'consumers_android']


    def getValues(self):
        return [self.s_day, self.consumers, self.consumers_ios, self.consumers_android]

    def set0(self, value):
        self.s_day = value

    def set1(self,value):
        self.consumers = value

    def set2(self,value):
        self.consumers_ios = value

    def set3(self,value):
        self.consumers_android = value

def test():
    t = New_consumers()
    s = t.getlist()
    print(s[0], s[1], s[2])
    pass

if __name__ == '__main__':
    test()