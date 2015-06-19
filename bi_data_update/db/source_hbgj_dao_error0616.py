__author__ = 'zhangchao'
from source_hbgj_mysql import *
from source_hbgj_oracle import *
from domain.hbgj_model import *

import sys
sys.path.append('..')

# update hbgj_activeusers daily/weekly/monthly
# update newusers daily

# update hbgj_newconsumers daily
# update hbgj_from_gt_newconsumers daily



class ErrorModel():
    def __init__(self):
        self.s_day = ''
        self.active_ios = 0
        self.active_android = 0
        self.active_android_error = 0

    def setValues(self,valueList):
        self.s_day = str(valueList[0])
        self.active_ios = int(valueList[1])
        self.active_android = int(valueList[2])
        self.active_android_error = int(valueList[3])
        pass




class BaseUserMysqlDao(Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        # model_object = model_class()
        if not result:
            return False
        for row in result:
            model_object = model_class()
            model_object.set0(row[0])
            model_object.set1(row[1])
            model_object.set2(row[2])
            model_object.set3(row[1]-row[2])
            users_model_list.append(model_object)
        return users_model_list

    def query_result_by_setValue(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list

class BaseUserOracleDao(object):
    def __init__(self):
        self.cursor = oracle_con()

    def query_result(self, sql, model_class):
        cursor = oracle_con()
        cursor.execute(sql)
        result=cursor.fetchall()
        users_model_list = []
        if not result:
            return False
        for row in result:
            model_object = model_class()
            model_object.set0(row[0])
            model_object.set1(row[1])
            model_object.set2(row[2])
            model_object.set3(row[1]-row[2])
            users_model_list.append(model_object)
        return users_model_list

    def query_result_by_setValue(self, sql, model_class):
        cursor = oracle_con()
        cursor.execute(sql)
        result=cursor.fetchall()
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list

class ActiveUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ErrorClass=ErrorModel, ModelClass=Active_users):
        self.db = DBClass()
        self.ErrorClass = ErrorClass
        self.ModelClass = ModelClass
    def get_users_daily(self, querydate_str):


        sql = "select distinct to_char(createtime,'yyyy-mm-dd') s_day, " \
              "count(distinct case when  (p LIKE '%%ios%%')  then userid end) ios, " \
              "count(distinct case when  (p LIKE '%%android%%')  then userid end) android, " \
              "count(distinct case when  (p LIKE '%%android%%' and to_char(createtime,'hh24') < '12' and p LIKE '%%hbgj,5.1%%')  then userid end) android1 " \
              "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(createtime,'yyyy-mm-dd') order by  to_char(createtime,'yyyy-mm-dd')" % querydate_str

        print(sql)
        result_temp_list = self.db.query_result_by_setValue(sql, self.ErrorClass)

        result_model_list = []

        for temp_model in result_temp_list:

            model_object = self.ModelClass()
            s_day = temp_model.s_day
            active_ios = int(temp_model.active_ios)
            active_android = int(temp_model.active_android)
            active_android_error = int(temp_model.active_android_error)


            active_android_last = int(((active_ios/1.1598) + (active_android-active_android_error))/2)
            if active_android_last > 150000 or active_android_last < 90000:
                active_android_last = int(active_ios/1.1598)

            model_object.set0(s_day)
            model_object.set1(active_ios + active_android_last)
            model_object.set2(active_ios)
            model_object.set3(active_android_last)

            result_model_list.append(model_object)


        return result_model_list



    def get_users_weekly(self, querydate_str):


        sql = "select to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') s_day, " \
              "count(distinct case when  (p LIKE '%%ios%%')  then userid end) ios, " \
              "count(distinct case when  (p LIKE '%%android%%')  then userid end) android, " \
              "count(distinct case when  (p LIKE '%%android%%' and to_char(createtime,'hh24') < '12' and p LIKE '%%hbgj,5.1%%')  then userid end) android1 " \
              "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') "  % querydate_str

        print(sql)
        result_temp_list = self.db.query_result_by_setValue(sql, self.ErrorClass)
        result_model_list = []

        for temp_model in result_temp_list:

            model_object = self.ModelClass()
            s_day = temp_model.s_day
            active_ios = int(temp_model.active_ios)
            active_android = int(temp_model.active_android)
            active_android_error = int(temp_model.active_android_error)

            active_android_last = int((active_android-active_android_error))
            # active_android_last = int(((active_ios/1.1598) + (active_android-active_android_error))/2)
            # # if active_android_last > 150000 or active_android_last < 90000:
            # #     active_android_last = int(active_ios/1.1598)

            model_object.set0(s_day)
            model_object.set1(active_ios + active_android_last)
            model_object.set2(active_ios)
            model_object.set3(active_android_last)

            result_model_list.append(model_object)

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    # def get_users_monthly(self,querydate_str):
    #     sql="select to_char(trunc(createtime,'mm'),'yyyy-mm-dd') s_day,count(distinct userid) active_users,count(distinct case when p LIKE '%%91ZS%%' or p LIKE '%%appstore%%' or p LIKE '%%juwan%%' or p LIKE '%%91PGZS%%' or p LIKE '%%kuaiyong%%' or p LIKE '%%TBT%%' or p LIKE '%%PPZS%%' then userid else null end ) active_users_ios " \
    #         "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(trunc(createtime,'mm'),'yyyy-mm-dd')" % querydate_str
    #     result_model_list=self.db.query_result(sql, self.ModelClass)
    #     return result_model_list


if __name__ == '__main__':
    o_object = ActiveUsersDao()
    result_list = o_object.get_users_weekly("20150601")
    for model in result_list:
        print(model)

    # activeUsersDaoTest()
    # newUsersDaoTest()
    # newConsumersDaoTest()
    # newConsumersFromGtDao()

    # orderDaoTest()


    pass