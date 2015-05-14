__author__ = 'zhangchao'
from source_gtgj_mysql import *
from domain.gtgj_model import *
import sys
sys.path.append('..')

class BaseUserDao(Mysql):
    def __init__(self, dbtype_dao='gtgj89'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result(self, sql, model_class):
        results = self.get_all(sql)
        users_model_list=[]
        if not results:
            return False
        for row in results:
            model_object = model_class()
            model_object.set0(row[model_object.getlist()[0]])
            model_object.set1(row[model_object.getlist()[1]])
            model_object.set2(row[model_object.getlist()[2]])
            model_object.set3(row[model_object.getlist()[1]]-row[model_object.getlist()[2]])
            users_model_list.append(model_object)
        return users_model_list


class ActiveUsersDao(object):
    def __init__(self, DBClass=BaseUserDao, ModelClass=Active_users):
        self.db = DBClass(dbtype_dao="gtgj81")
        self.ModelClass = ModelClass

    def get_users_daily(self, querydate_str):
        sql="SELECT s_day,sum(active_users) active_users," \
            "sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) active_users_ios " \
            "FROM global_statistics " \
            "where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s and DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>='20141219' " \
            "GROUP BY s_day" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def get_users_weekly(self, querydate_str):
        sql="SELECT s_day,sum(active_users) active_users," \
            "sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) active_users_ios " \
            "FROM global_week_statistics " \
            "where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s GROUP BY s_day" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def get_users_monthly(self, querydate_str):

        sql="SELECT s_day,sum(active_users) active_users," \
                "sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) " \
                "active_users_ios " \
                "FROM global_month_statistics where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s " \
                "GROUP BY s_day" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list


class NewUsersDao(object):
    def __init__(self, DBClass=BaseUserDao, ModelClass=New_users):
        self.db = DBClass()
        self.ModelClass = ModelClass

    def get_users_daily(self,querydate_str):
        sql="SELECT s_day,sum(new_users) new_users," \
               "sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then new_users else 0 end) new_users_ios " \
               "FROM global_statistics " \
               "where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s " \
               "GROUP BY s_day" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list


class ConsumersDao(object):
    def __init__(self, DBClass=BaseUserDao, ModelClass=Consumers):
        self.db = DBClass()
        self.ModelClass = ModelClass
    def get_consumers_daily(self, querydate_str):
        sql = "select date_format(create_time,'%%Y-%%m-%%d') s_day,count(DISTINCT uid) consumers," \
            "count(distinct case when p_info LIKE '%%ios%%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%%android%%' then uid else null end ) consumers_android " \
            "from user_order "\
            "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s "\
            "group by s_day " % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list
        pass

    def get_consumers_weekly(self, querydate_str):
        sql="select date_format(subdate(create_time,date_format(create_time,'%%w')-1),'%%Y-%%m-%%d') s_day,count(DISTINCT uid) consumers," \
            "count(distinct case when p_info LIKE '%%ios%%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%%android%%' then uid else null end ) consumers_android " \
            "from ( " \
            "select create_time,uid,p_info "\
            "from user_order_history "\
            "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s "\
            "UNION "\
            "select create_time,uid,p_info "\
            "from user_order "\
            "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s "\
            ") as A "\
            "group by s_day " % (querydate_str,querydate_str)
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list


    def get_consumers_monthly(self, querydate_str):
        sql="select DATE_FORMAT(str_to_date(CONCAT(YEAR(create_time),'-',MONTH(create_time),'-01'),'%%Y-%%m-%%d'),'%%Y-%%m-%%d') s_day,count(DISTINCT uid) consumers, " \
            "count(distinct case when p_info LIKE '%%ios%%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%%android%%' then uid else null end ) consumers_android " \
            "from ( " \
            "select create_time,uid,p_info "\
            "from user_order_history "\
            "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s "\
            "UNION "\
            "select create_time,uid,p_info "\
            "from user_order "\
            "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')>=%s "\
            ") as A "\
            "group by s_day " % (querydate_str,querydate_str)

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list


class NewConsumersDao(object):
    def __init__(self, DBClass=BaseUserDao):
        self.db = DBClass()
    def get_consumers_daily(self,querydate_str):
        # sql="SELECT count(distinct uid) new_consumers," \
        #     "count(distinct case when p_info LIKE '%%ios%%' then uid else null end ) new_consumers_ios, " \
        #     "count(distinct case when p_info LIKE '%%android%%' then uid else null end ) new_consumers_android " \
        #     "from user_order " \
        #     "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')=%s  "\
        #     "and uid not in(  " \
        #     "select uid "\
        #     "from user_order_history "\
        #     "where i_status=3 " \
        #     ") "  \
        #     "and uid not in(  " \
        #     "select uid "\
        #     "from user_order " \
        #     "where i_status=3 " \
        #     "and DATE_FORMAT(create_time,'%%Y%%m%%d')<%s " \
        #     ")"  %(querydate_str,querydate_str)
        sql = ""
        result_model_list=self.db.query_result(sql,New_consumers)
        return result_model_list
        pass


def activeUsersDaoTest():

    activeUser_object = ActiveUsersDao()
    results = activeUser_object.get_users_daily("20150423")
    # results = activeUser_object.get_users_weekly("20150406")
    # results = activeUser_object.get_users_monthly("20150301")

    for result in results:
        print(result)

def newUsersDaoTest():
    newUser_object = NewUsersDao()
    results = newUser_object.get_users_daily("20150412")
    for result in results:
        print(result.s_day, result.new_users)
    pass


def consumersDaoTest():
    consumers_object = ConsumersDao()
    results = consumers_object.get_consumers_daily("20150422")
    for result in results:
        print(result.s_day, result.active_users,result.active_users_ios,result.active_users_android)
    pass
if __name__ == '__main__':
    activeUsersDaoTest()
    # newUsersDaoTest()
    # consumersDaoTest()

    pass
