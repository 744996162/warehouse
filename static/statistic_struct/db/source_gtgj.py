__author__ = 'Administrator'

from mysql import *
from model import user


class GtUserDao(Mysql):
    def __init__(self, dbtype="gtgj89"):
        Mysql.__init__(self, dbtype=dbtype)

    def get_users(self, sql, model=user.Users):

        results = self.get_all(sql)
        model_list = []

        if not results:
            return []
        for row in results:
            o_model = model()
            o_model.setVale(row[0], int(row[1]), int(row[2]), int(row[1]) - int(row[2]))
            model_list.append(o_model)
        return model_list


class ActiveUserDao(GtUserDao):
    def __init__(self):
        GtUserDao.__init__(self)

    def get_users_daily(self, query_date):
        sql = "SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) active_users_ios FROM global_statistics where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s and DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>='20141219' GROUP BY s_day" % query_date
        model_result = self.get_users(sql)
        return model_result

    def get_users_weekly(self, query_date):
        sql = "SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) active_users_ios FROM global_week_statistics where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s GROUP BY s_day" % query_date
        model_result = self.get_users(sql)
        return model_result

    def get_users_monthly(self, query_date):
        sql = "SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%%91ZS%%' or source LIKE '%%appstore%%' or source LIKE '%%juwan%%' or source LIKE '%%91PGZS%%' or source LIKE '%%kuaiyong%%' or source LIKE '%%TBT%%' or source LIKE '%%PPZS%%' then active_users else 0 end) active_users_ios FROM global_month_statistics where DATE_FORMAT(str_to_date(s_day, '%%Y-%%m-%%d'),'%%Y%%m%%d')>=%s GROUP BY s_day" % querydate
        model_result = self.get_users(sql)
        return model_result


class ConsumersDao(GtUserDao):
    def __init__(self):
        GtUserDao.__init__(self)

    def get_consumers_daily(self, query_date):
        sql = "select date_format(create_time,'%%Y-%%m-%%d') s_day,count(DISTINCT uid) consumers," \
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
            "group by s_day " % (query_date, query_date)

        model_result = self.get_users(sql)

        return model_result
        pass

    def get_consumers_weekly(self, query_date):
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
            "group by s_day " % (query_date,query_date)

        model_result = self.get_users(sql)

        return model_result

    def get_consumers_monthly(self, query_date):

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
            "group by s_day "  % (query_date, query_date)

        model_result = self.get_users(sql)
        return model_result



