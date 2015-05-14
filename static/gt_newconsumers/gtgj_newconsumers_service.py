#coding=utf-8
__author__ = 'zhangchao'
import datetime

import goal_gtgj_newconsmers_dao
import gtgj_new_consumers


class NewconsumersDailyService():
    def __init__(self,result):
        self._goal_dao=goal_gtgj_newconsmers_dao.NewconsumersDaily()
        self._result = result

    def insert_data(self):
        for row in self._result:
            sday_result=self._goal_dao.get_user(row.s_day)
            print
            if sday_result==False:
                # user_his=hbgj_new_users.New_users()
                user_his=gtgj_new_consumers.New_consumers()
                user_his.s_day=row.s_day
                user_his.new_consumers=0
                user_his.new_consumers_ios=0
                user_his.new_consumers_android=0
                users = []
                users.append(user_his)
                self._goal_dao.insert_users(users)
                print(row.s_day,"insert")
            else:
                # print(row.s_day,1)
                pass



    def update_data(self):
        test=self._goal_dao.update_users(self._result)
        print(test)

    def main(self):
        self.insert_data()
        self.update_data()
        pass

if __name__=="__main__":

    # test=NewconsumersDailyService()
    # test.update_bi()
    pass