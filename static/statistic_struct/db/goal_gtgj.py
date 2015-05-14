__author__ = 'Administrator'
import logging

from mysql import *
from model import user


class GtUsersDao(Mysql):
    def __init__(self, dbtype="bi79"):
        Mysql.__init__(self, dbtype=dbtype)

    def insert_users(self, users_list, sql=""):
        if (users_list is None) or (len(users_list) <= 0):
            pass
        else:
            args = []
            i = 0
            for o_user_model in users_list:
                i += 1
                arg = [o_user_model.s_day, o_user_model.users, o_user_model.users_ios, o_user_model.users_android]
                args.append(arg)
                if i % 100 == 0 or i == len(users_list):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_users(self, s_day, model=user.Users, sql=""):
        arg = [s_day]
        result = self.get_all(sql, arg)
        # logging.DEBUG(str(sql))
        users_list = []
        if not result:
            return  False
        for row in result:
            o_user_model = model()
            o_user_model.setVale(row[0], int(row[1]), int(row[2]), int(row[3]))
            users_list.append(o_user_model)
        return users_list

    def update_users(self, users_list, sql=""):
        if (users_list is None) or (len(users_list) <= 0):
            pass
        else:

            for o_user_model in users_list:
                arg = [o_user_model.s_day, o_user_model.users, o_user_model.users_ios, o_user_model.users_android]
                self.update(sql, arg)
                self.end()

class ActiveUsersDaily(GtUsersDao):
    def __init__(self, dbtype="bi79"):
        GtUsersDao.__init__(self, dbtype=dbtype)
        self.dbname = 'gtgj_activeusers_daily'

    def insert_users(self, users_list, sql=""):
        if sql == "":
            sql = 'insert into '+self.dbname+' (s_day,active_users,active_users_ios, active_users_android,createtime,updatetime)'\
                'values (%s, %s,%s,%s, now(), now())'
        super(ActiveUsersDaily, self).insert_users(sql, users_list)


    def get_users(self, s_day, model=user.Users, sql=""):
        if sql == "":
            sql = "select s_day,active_users,active_users_ios,active_users_android from "+ self.dbname + " where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            # logging.DEBUG(sql)
        users_list = super(ActiveUsersDaily, self).get_users(s_day, model, sql)
        return users_list
        pass

    def update_users(self, users_list, sql=""):
         if sql == "":
             sql = "update " +self.dbname + " set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d') "
         super(ActiveUsersDaily, self).update_users(users_list, sql=sql)



class ActiveUsersWeekly(ActiveUsersDaily):
    def __init__(self, dbtype="bi79"):
        GtUsersDao.__init__(self, dbtype=dbtype)
        self.dbname = 'gtgj_activeusers_weekly'

class ActiveUsersMonthly(ActiveUsersDaily):
    def __init__(self, dbtype="bi79"):
        GtUsersDao.__init__(self, dbtype=dbtype)
        self.dbname = 'gtgj_activeusers_monthly'



def testDaily():
    o_AUD = ActiveUsersMonthly()
    result = o_AUD.get_users("2015-03-30")
    print(result[0])

def testWeekly():
    o_AUW = ActiveUsersMonthly()
    result = o_AUW.get_users("2015-03-30")
    print(result[0])


def testMonthly():
    o_AUM = ActiveUsersMonthly()
    result = o_AUM.get_users("2015-02-01")
    print(result[0])

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    testMonthly()