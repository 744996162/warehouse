__author__ = 'Administrator'

from goal_mysql import *
from domain import hbgj_channel_model

class UpdateChannelBaseDao(Mysql):
    def __init__(self, tablename, ModelClass, dbtype_dao='91bi'):
        Mysql.__init__(self, dbtype=dbtype_dao)
        self.tablename = tablename
        self.modelClass = ModelClass

    def insert_users(self, _users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            sql = 'insert into ' + self.tablename + ' (' + list_str[0]+', ' + list_str[1]+', '+list_str[2]+', ' \
                                             'createtime, updatetime) ' \
                                         'values (%s, %s,%s, now(), now()) '
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.getValues()[0], user.getValues()[1], user.getValues()[2]]
                # print(arg)
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()


class UpdateChannelOrderDao(Mysql):
    def __init__(self, tablename, ModelClass, dbtype_dao='91bi'):
        Mysql.__init__(self, dbtype=dbtype_dao)
        self.tablename = tablename
        self.modelClass = ModelClass

    def insert_users(self, _users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            sql = 'insert into ' + self.tablename + ' (' + list_str[0]+', ' + list_str[1]+', '+list_str[2]+', ' + list_str[3] + ', ' + list_str[4] + ', ' \
                                             'createtime, updatetime) ' \
                                         'values (%s, %s,%s,%s,%s, now(), now()) '
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.getValues()[0], user.getValues()[1], user.getValues()[2], user.getValues()[3], user.getValues()[4]]

                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

class HbChannelUpdateDao():
     # hbgj_activeusers_daily Active_users
     # hbgj_activeusers_weekly  Active_users
     # hbgj_activeusers_monthly Active_users
     # hbgj_newusers_daily  New_users
     #
     # hbgj_consumers_daily Consumers
     # hbgj_consumers_weekly Consumers
     # hbgj_consumers_monthly Consumers

     # hbgj_order_daily Orders
     # hbgj_order_weekly Orders
     # hbgj_order_monthly Orders

     # hbgj_newconsumers_daily New_consumers

    def baseUpdate(self,tablename, modelClass, _users):
        o_updateBase = UpdateChannelBaseDao(tablename, modelClass)
        o_updateBase.insert_users(_users)

    def orderUpdate(self,tablename, modelClass,_users):
        o_updateOrder = UpdateChannelOrderDao(tablename, modelClass)
        o_updateOrder.insert_users(_users)


    def activeDailyUpdate(self, _users):
        tablename = "hbgj_channel_activeusers_daily"
        modelClass = hbgj_channel_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def activeWeeklyUpdate(self, _users):
        tablename = "hbgj_channel_activeusers_weekly"
        modelClass = hbgj_channel_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)

    def activeMonthlyUpdate(self, _users):
        tablename = "hbgj_channel_activeusers_monthly"
        modelClass = hbgj_channel_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def newusersDailyUpdate(self, _users):
        tablename = "hbgj_channel_newusers_daily"
        modelClass = hbgj_channel_model.New_users
        self.baseUpdate(tablename, modelClass, _users)

    def orderDailyUpdate(self, _users):
        tablename = "hbgj_channel_order_daily"
        modelClass = hbgj_channel_model.Orders_goal
        self.orderUpdate(tablename, modelClass, _users)



if __name__ == "__main__":




    pass