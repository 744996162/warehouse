# ecoding=utf-8
__author__ = 'Administrator'


class Users(object):
    def __init__(self):
        self.s_day = ''
        self.users = 0
        self.users_ios = 0
        self.users_android = 0

    def setVale(self, str_s_day, i_users, i_users_ios, i_users_android):
        self.s_day = str_s_day
        self.users = i_users
        self.users_ios = i_users_ios
        self.users_android = i_users_android

    def __str__(self):
        str_out = "Users:" + "\t" + self.s_day + "\t" + str(self.users) + "\t" + str(self.users_ios) +"\t"+str(self.users_android)
        return str_out


class ActiveUser(object):
    def __init__(self):
        self.s_day = ''
        self.active_users = 0
        self.active_users_ios = 0
        self.active_users_android = 0

    def setVale(self, str_s_day, i_active_users, i_active_users_ios, i_active_users_android):
        self.s_day = str_s_day
        self.active_users = i_active_users
        self.active_users_ios = i_active_users_ios
        self.active_users_android = i_active_users_android

    def __str__(self):
        str_out = "ActiveUser" + "\t" + self.s_day
        return str_out

class Consumer(object):
    def __init__(self):
        self.s_day = ''
        self.consumers = 0
        self.consumers_ios = 0
        self.consumers_android = 0


class NewUser(object):
    def __init__(self):
        self.s_day = ''
        self.new_users = 0
        self.new_users_ios = 0
        self.new_users_android = 0

class NewConsumer(object):
    def __init__(self):
        self.s_day = ''
        self.new_consumers = 0
        self.new_consumers_ios = 0
        self.new_consumers_android = 0