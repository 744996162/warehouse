__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
import gtgj_new_consumers

class NewconsumersDaily(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='gtgj_newconsumers_daily'
            sql='insert into '+db_name+' (s_day,new_consumers,new_consumers_ios,new_consumers_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s,now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.new_consumers,user.new_consumers_ios,user.new_consumers_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self,_day):
        sql="select s_day,new_consumers,new_consumers_ios,new_consumers_android from gtgj_newconsumers_daily where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=gtgj_new_consumers.New_consumers()
            user.s_day = row['s_day']
            user.new_consumers = row['new_consumers']
            user.new_consumers_ios = row['new_consumers_ios']
            user.new_consumers_android = row['new_consumers_android']
            users.append(user)
        return users


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'gtgj_newconsumers_daily'
            sql="update gtgj_newconsumers_daily set new_consumers=%s,new_consumers_ios=%s,new_consumers_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.new_consumers,user.new_consumers_ios,user.new_consumers_android,user.s_day]
                self.update(sql,arg)
                self.end()
def test():
    pass

if __name__=="__main__":
    o_new_consumers=NewconsumersDaily()
    o_new_consumers.get_user("2014-11-19")
    pass