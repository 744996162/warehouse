__author__ = 'Administrator'
from goal_mysql import *

from domain import hbgj_model
from domain import gtgj_model
from db import source_gtgj_dao
# from db.source_hbgj_dao import *


class UpdateBaseDao(Mysql):
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
            sql = 'insert into ' + self.tablename + ' (' + list_str[0]+', ' + list_str[1]+', '+list_str[2]+', ' + list_str[3] + ', ' \
                                             'createtime, updatetime) ' \
                                         'values (%s, %s,%s,%s, now(), now()) '
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.getValues()[0], user.getValues()[1], user.getValues()[2], user.getValues()[3]]
                # print(arg)
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self, _day):
        o_model = self.modelClass()
        list_str = o_model.getlist()
        sql = "select " + str(list_str[0]) + "," + str(list_str[1]) + "," + str(list_str[2]) + "," + str(list_str[2]) + " from " + self.tablename + " " \
              "where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg = [_day]
        result = self.get_all(sql, arg)
        users = []
        if not result:
            return False
        for row in result:
            user = self.modelClass()
            user.set0(row[0])
            user.set1(row[1])
            user.set2(row[2])
            user.set3(row[3])
            users.append(user)
        return users

    def update_users(self, _users):
        if (_users == None):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            # sql="update gtgj_activeusers_daily set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date('%s','%%Y-%%m-%%d'),'%%Y%%m%%d')"
            sql = "update " + self.tablename + " set " + str(list_str[1]) + "=%s, " + str(list_str[2]) + "=%s, " + str(list_str[3]) + "=%s, " + "updatetime=now() " + \
                  "where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            # print(sql)
            args = []
            for user in _users:
                arg = [user.getValues()[1], user.getValues()[2], user.getValues()[3], user.getValues()[0]]
                print(arg)
                self.update(sql, arg)
                self.end()

    def updatenew(self, _users):
        if ( _users == None):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            for user in _users:
                s_day = user.getValues()[0]
                sday_result = self.get_user(s_day)
                if sday_result == False:
                    user_temp = self.modelClass()
                    user_temp.set0(s_day)
                    users = []
                    users.append(user_temp)
                    self.insert_users(users)
                    self.end()
                    print(s_day, "insert")
                else:
                    # print(row.s_day,1)
                    pass
            self.update_users(_users)
        pass


class UpdateOrderDao(Mysql):
    def __init__(self, tablename, ModelClass, dbtype_dao='91bi'):
        Mysql.__init__(self, dbtype=dbtype_dao)
        self.tablename = tablename
        self.modelClass = ModelClass

    def insert_users(self, _users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            # sql = 'insert into ' + self.tablename +'(s_day,active_users,active_users_ios,active_users_android,createtime,updatetime)'\
            #                              'values (%s, %s,%s,%s, now(), now())'
            o_model = self.modelClass()
            list_str = o_model.getlist()
            sql = 'insert into ' + self.tablename + ' (' + list_str[0]+', ' + list_str[1]+', '+list_str[2]+', ' + list_str[3] + ', ' + list_str[4] + ', ' \
                                             'createtime, updatetime) ' \
                                         'values (%s, %s,%s,%s,%s, now(), now()) '
            # print(sql)
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.getValues()[0], user.getValues()[1], user.getValues()[2], user.getValues()[3], user.getValues()[4]]
                # print(arg)
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self, _day):
        o_model = self.modelClass()
        list_str = o_model.getlist()
        sql = "select " + str(list_str[0]) + "," + str(list_str[1]) + "," + str(list_str[2]) + "," + str(list_str[2]) + " from " + self.tablename + " " \
              "where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg = [_day]
        result = self.get_all(sql, arg)
        users = []
        if not result:
            return False
        for row in result:
            user = self.modelClass()
            user.set0(row[0])
            user.set1(row[1])
            user.set2(row[2])
            user.set3(row[3])
            users.append(user)
        return users

    def update_users(self, _users):
        if (_users == None):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            # sql="update gtgj_activeusers_daily set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date('%s','%%Y-%%m-%%d'),'%%Y%%m%%d')"
            sql = "update " + self.tablename + " set " + str(list_str[1]) + "=%s, " + str(list_str[2]) + "=%s, " + str(list_str[3]) + "=%s, " + str(list_str[4]) + "=%s, " + "updatetime=now() " + \
                  "where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            # print(sql)
            args = []
            for user in _users:
                arg = [user.getValues()[1], user.getValues()[2], user.getValues()[3], user.getValues()[4], user.getValues()[0]]
                print(arg)
                self.update(sql, arg)
                self.end()

    def updatenew(self, _users):
        if ( _users == None):
            pass
        else:
            o_model = self.modelClass()
            list_str = o_model.getlist()
            for user in _users:
                s_day = user.getValues()[0]
                sday_result = self.get_user(s_day)
                if sday_result == False:
                    user_temp = self.modelClass()
                    user_temp.set0(s_day)
                    users = []
                    users.append(user_temp)
                    self.insert_users(users)
                    self.end()
                    print(s_day, "insert")
                else:
                    # print(row.s_day,1)
                    pass
            self.update_users(_users)
        pass

class GtUpdateDao():
     # gtgj_activeusers_daily Active_users
     # gtgj_activeusers_weekly  Active_users
     # gtgj_activeusers_monthly Active_users
     # gtgj_newusers_daily  New_users
     #
     # gtgj_consumers_daily Consumers
     # gtgj_consumers_weekly Consumers
     # gtgj_consumers_monthly Consumers
     # gtgj_newconsumers_daily New_consumers
    def baseUpdate(self, tablename, modelClass, _users):
        o_updateBase = UpdateBaseDao(tablename, modelClass)
        o_updateBase.updatenew(_users)

    def activeDailyUpdate(self, _users):
        tablename = "gtgj_activeusers_daily"
        modelClass = gtgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def activeWeeklyUpdate(self, _users):
        tablename = "gtgj_activeusers_weekly"
        modelClass = gtgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def activeMonthlyUpdate(self, _users):
        tablename = "gtgj_activeusers_monthly"
        modelClass = gtgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def newusersDailyUpdate(self, _users):
        tablename = "gtgj_newusers_daily"
        modelClass = gtgj_model.New_users
        self.baseUpdate(tablename, modelClass, _users)


    def consumersDailyUpdate(self, _users):
        tablename = "gtgj_consumers_daily"
        modelClass = gtgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)


    def consumersWeeklyUpdate(self, _users):
        tablename = "gtgj_consumers_weekly"
        modelClass = gtgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)


    def consumersMonthlyUpdate(self, _users):
        tablename = "gtgj_consumers_monthly"
        modelClass = gtgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)


    def newconsumersDailyUpdate(self, _users):
        tablename = "gtgj_newconsumers_daily"
        modelClass = gtgj_model.New_consumers
        self.baseUpdate(tablename, modelClass, _users)

class HbUpdateDao():
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

    def baseUpdate(self,tablename, modelClass,_users):
        o_updateBase = UpdateBaseDao(tablename, modelClass)
        o_updateBase.updatenew(_users)

    def orderUpdate(self,tablename, modelClass,_users):
        o_updateOrder = UpdateOrderDao(tablename, modelClass)
        o_updateOrder.updatenew(_users)

    def activeDailyUpdate(self, _users):
        tablename = "hbgj_activeusers_daily"
        modelClass = hbgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def activeWeeklyUpdate(self, _users):
        tablename = "hbgj_activeusers_weekly"
        modelClass = hbgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def activeMonthlyUpdate(self, _users):
        tablename = "hbgj_activeusers_monthly"
        modelClass = hbgj_model.Active_users
        self.baseUpdate(tablename, modelClass, _users)


    def newusersDailyUpdate(self, _users):
        tablename = "hbgj_newusers_daily"
        modelClass = hbgj_model.New_users
        self.baseUpdate(tablename, modelClass, _users)


    def consumersDailyUpdate(self, _users):
        tablename = "hbgj_consumers_daily"
        modelClass = hbgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)


    def consumersWeeklyUpdate(self, _users):
        tablename = "hbgj_consumers_weekly"
        modelClass = hbgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)

    def consumersMonthlyUpdate(self, _users):
        tablename = "hbgj_consumers_monthly"
        modelClass = hbgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)

    def consumersQuarterlyUpdate(self, _users):
        tablename = "hbgj_consumers_quarterly"
        modelClass = hbgj_model.Consumers
        self.baseUpdate(tablename, modelClass, _users)

    def orderDailyUpdate(self, _users):
        tablename = "hbgj_order_daily"
        modelClass = hbgj_model.Orders
        self.orderUpdate(tablename, modelClass, _users)

    def orderWeeklyUpdate(self, _users):
        tablename = "hbgj_order_weekly"
        modelClass = hbgj_model.Orders
        self.orderUpdate(tablename, modelClass, _users)

    def orderMonthlyUpdate(self, _users):
        tablename = "hbgj_order_monthly"
        modelClass = hbgj_model.Orders
        self.orderUpdate(tablename, modelClass, _users)

    def newconsumersDailyUpdate(self, _users):
        tablename = "hbgj_newconsumers_daily"
        modelClass = hbgj_model.New_consumers
        self.baseUpdate(tablename, modelClass, _users)

    def newconsumersFromGtDailyUpdate(self, _users):
        tablename = "hbgj_from_gt_newconsumers_daily"
        modelClass = hbgj_model.New_consumers
        self.baseUpdate(tablename, modelClass, _users)


def test():
    o_ActiveUsers = source_gtgj_dao.ActiveUsersDao()
    users = o_ActiveUsers.get_users_daily("20150412")
    # user.s_day = "2015-04-13"
    # users = []
    # users.append(user)
    #
    o = UpdateBaseDao("gtgj_activeusers_daily", gtgj_model.Active_users)
    o.updatenew(users)
    # o.get_user("20140822")
    # # results = o.get_user("20150412")
    # # for result in results:
    # #     print(result)
    # o.updatenew(users)
    # pass


if __name__ == "__main__":



    pass