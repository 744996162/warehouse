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

class ActiveUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass=Active_users):
        self.db = DBClass()
        self.ModelClass = ModelClass
    def get_users_daily(self, querydate_str):
        sql = "select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct userid),sum(case when p LIKE '%%91ZS%%' or p LIKE '%%appstore%%' or p LIKE '%%juwan%%' or p LIKE '%%91PGZS%%' or p LIKE '%%kuaiyong%%' or p LIKE '%%TBT%%' or p LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
              "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(createtime,'yyyy-mm-dd') order by  to_char(createtime,'yyyy-mm-dd')" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def get_users_weekly(self, querydate_str):

        sql="select to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') s_day,count(distinct userid) active_users,count(distinct case when p LIKE '%%91ZS%%' or p LIKE '%%appstore%%' or p LIKE '%%juwan%%' or p LIKE '%%91PGZS%%' or p LIKE '%%kuaiyong%%' or p LIKE '%%TBT%%' or p LIKE '%%PPZS%%' then userid else null end ) active_users_ios " \
               "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd')" % querydate_str
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def get_users_monthly(self,querydate_str):
        sql="select to_char(trunc(createtime,'mm'),'yyyy-mm-dd') s_day,count(distinct userid) active_users,count(distinct case when p LIKE '%%91ZS%%' or p LIKE '%%appstore%%' or p LIKE '%%juwan%%' or p LIKE '%%91PGZS%%' or p LIKE '%%kuaiyong%%' or p LIKE '%%TBT%%' or p LIKE '%%PPZS%%' then userid else null end ) active_users_ios " \
            "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(trunc(createtime,'mm'),'yyyy-mm-dd')" % querydate_str
        result_model_list=self.db.query_result(sql, self.ModelClass)
        return result_model_list


class NewUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass =New_users):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_users_daily(self,querydate_str):

        sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
               "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list



class OrderDao(object):
    def __init__(self, DBClass=BaseUserMysqlDao, ModelClass=Orders):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_orders_daily(self, start_sday, end_sday):
        sql = "select TicketAll.s_day,TicketAll.ticket_num,TicketAll.order_num,Ticket_GT.ticket_num_gt,Ticket_GT.order_num_gt " \
              "from " \
              "(SELECT DATE_FORMAT(CREATETIME,'%%Y-%%m-%%d') s_day, " \
              "count(A.ORDERID) ticket_num,  " \
              "count(distinct A.ORDERID) order_num, " \
              "count(case when A.p like '%%gtgj%%' then A.ORDERID END) ticket_num_gt " \
              "from  " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "GROUP BY s_day) as TicketAll,  " \
              "(SELECT DATE_FORMAT(CREATETIME,'%%Y-%%m-%%d') s_day, " \
              "count(A.ORDERID) ticket_num_gt, " \
              "count(distinct A.ORDERID) order_num_gt " \
              "from " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s  " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "where A.p like '%%gtgj%%'  "  \
              "GROUP BY s_day " \
              ") as Ticket_GT " \
              "where TicketAll.s_day = Ticket_GT.s_day  "  %(start_sday,end_sday,start_sday,end_sday)
        print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list
    pass


    def get_orders_weekly(self, start_sday, end_sday):
        sql = "select TicketAll.s_day,TicketAll.ticket_num,TicketAll.order_num,Ticket_GT.ticket_num_gt,Ticket_GT.order_num_gt " \
              "from " \
              "(SELECT date_format(subdate(createtime,date_format(createtime,'%%w')-1),'%%Y-%%m-%%d') s_day , " \
              "count(A.ORDERID) ticket_num,  " \
              "count(distinct A.ORDERID) order_num, " \
              "count(case when A.p like '%%gtgj%%' then A.ORDERID END) ticket_num_gt " \
              "from  " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "GROUP BY s_day) as TicketAll,  " \
              "(SELECT date_format(subdate(createtime,date_format(createtime,'%%w')-1),'%%Y-%%m-%%d') s_day , " \
              "count(A.ORDERID) ticket_num_gt, " \
              "count(distinct A.ORDERID) order_num_gt " \
              "from " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s  " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "where A.p like '%%gtgj%%'  "  \
              "GROUP BY s_day " \
              ") as Ticket_GT " \
              "where TicketAll.s_day = Ticket_GT.s_day  "  %(start_sday, end_sday, start_sday, end_sday)
        print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list
    pass

    def get_orders_monthly(self, start_sday, end_sday):
        sql = "select TicketAll.s_day,TicketAll.ticket_num,TicketAll.order_num,Ticket_GT.ticket_num_gt,Ticket_GT.order_num_gt " \
              "from " \
              "(SELECT DATE_FORMAT(str_to_date(CONCAT(YEAR(createtime),'-',MONTH(createtime),'-01'),'%%Y-%%m-%%d'),'%%Y-%%m-%%d') s_day , " \
              "count(A.ORDERID) ticket_num,  " \
              "count(distinct A.ORDERID) order_num, " \
              "count(case when A.p like '%%gtgj%%' then A.ORDERID END) ticket_num_gt " \
              "from  " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "GROUP BY s_day) as TicketAll,  " \
              "(SELECT DATE_FORMAT(str_to_date(CONCAT(YEAR(createtime),'-',MONTH(createtime),'-01'),'%%Y-%%m-%%d'),'%%Y-%%m-%%d') s_day , " \
              "count(A.ORDERID) ticket_num_gt, " \
              "count(distinct A.ORDERID) order_num_gt " \
              "from " \
              "(select TICKET_ORDERDETAIL.createtime as CREATETIME,TICKET_ORDERDETAIL.ORDERID as ORDERID,TICKET_ORDER.p AS p " \
              "from TICKET_ORDERDETAIL INNER JOIN  TICKET_ORDER ON TICKET_ORDER.ORDERID = TICKET_ORDERDETAIL.ORDERID " \
              "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')>=%s  " \
              "and DATE_FORMAT(TICKET_ORDER.createtime,'%%Y%%m%%d')<%s) as A " \
              "where A.p like '%%gtgj%%'  "  \
              "GROUP BY s_day " \
              ") as Ticket_GT " \
              "where TicketAll.s_day = Ticket_GT.s_day  "  %(start_sday, end_sday, start_sday, end_sday)
        # print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list
    pass

class ConsumersDao(object):
    def __init__(self, DBClass=BaseUserMysqlDao, ModelClass=Consumers):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_consumers_daily(self, start_sday, end_sday):

        sql = "select DATE_FORMAT(createtime,'%%Y-%%m-%%d') s_day,  " \
              "count(DISTINCT PHONEID) consumers, " \
              "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) consumers_ios " \
              "from( " \
              "SELECT createtime,phoneid,p " \
              "from gift_order " \
              "where PRODUCTID=12 " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "UNION " \
              "SELECT createtime,phoneid,p " \
              "from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              ") as A " \
              "GROUP BY s_day " \
              "order BY s_day " %(start_sday, end_sday, start_sday, end_sday)

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list



    def get_consumers_weekly(self, start_sday, end_sday):

        sql = "select date_format(subdate(createtime,date_format(createtime,'%%w')-1),'%%Y-%%m-%%d') s_day,  " \
              "count(DISTINCT PHONEID) consumers, " \
              "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) consumers_ios " \
              "from( " \
              "SELECT createtime,phoneid,p " \
              "from gift_order " \
              "where PRODUCTID=12 " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "UNION " \
              "SELECT createtime,phoneid,p " \
              "from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              ") as A " \
              "GROUP BY s_day " \
              "order BY s_day " %(start_sday, end_sday, start_sday, end_sday)
        print(sql)

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def get_consumers_monthly(self, start_sday, end_sday):

        sql = "select DATE_FORMAT(str_to_date(CONCAT(YEAR(createtime),'-',MONTH(createtime),'-01'),'%%Y-%%m-%%d'),'%%Y-%%m-%%d') s_day,  " \
              "count(DISTINCT PHONEID) consumers, " \
              "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) consumers_ios " \
              "from( " \
              "SELECT createtime,phoneid,p " \
              "from gift_order " \
              "where PRODUCTID=12 " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "UNION " \
              "SELECT createtime,phoneid,p " \
              "from TICKET_ORDER " \
              "where ORDERSTATUE not in (2,12,21,51,75) " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
              "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
              ") as A " \
              "GROUP BY s_day " \
              "order BY s_day " %(start_sday, end_sday, start_sday, end_sday)
        print(sql)

        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

    def  get_consumers_quarterly(self, start_sday, end_sday):

        sql = "select CONCAT('Q',QUARTER(createtime),',',YEAR(createtime)) s_day, " \
           "count(DISTINCT PHONEID) consumers, " \
           "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) consumers_ios " \
          "from( " \
          "SELECT createtime,phoneid,p " \
          "from gift_order " \
          "where PRODUCTID=12 " \
          "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
          "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
          "UNION " \
          "SELECT createtime,phoneid,p " \
          "from TICKET_ORDER " \
          "where ORDERSTATUE not in (2,12,21,51,75) " \
          "and DATE_FORMAT(createtime,'%%Y%%m%%d')>=DATE_FORMAT(%s,'%%Y%%m%%d') " \
          "and DATE_FORMAT(createtime,'%%Y%%m%%d')<DATE_FORMAT(%s,'%%Y%%m%%d') " \
          ") as A " \
          "GROUP BY s_day " \
          "order BY s_day " %(start_sday, end_sday, start_sday, end_sday)
        result_model_list = self.db.query_result(sql, self.ModelClass)
        return result_model_list

class NewConsumersDao(object):
    def __init__(self, DBClass=BaseUserMysqlDao, ModelClass=New_consumers):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_consumers_daily(self, querydate_str):

        sql = "SELECT date_format(createtime,'%%Y-%%m-%%d') s_day, count(DISTINCT PHONEID) new_consumers, " \
                "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) new_consumers_ios " \
                "from ( " \
                "SELECT createtime,phoneid,p " \
                "from gift_order " \
                "where PRODUCTID=12 " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')= %s " \
                "UNION " \
                "SELECT createtime,phoneid,p " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')= %s "\
                ") as A " \
                "where PHONEID not in " \
                "( " \
                "SELECT phoneid " \
                "from gift_order " \
                "where PRODUCTID=12 " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s " \
                "UNION " \
                "SELECT phoneid " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s " \
                ") group by s_day " % (querydate_str, querydate_str, querydate_str, querydate_str)

        result_model_list=self.db.query_result(sql, self.ModelClass)
        return result_model_list
        pass


class NewConsumersFromGtDao(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = New_consumers):
        self.db = DBClass()
        self.ModelClass = ModelClass

    def get_consumers_daily(self, querydate_str):
        sql = "SELECT date_format(createtime,'%%Y-%%m-%%d') s_day, count(DISTINCT PHONEID) new_consumers, " \
                "count(distinct case when p LIKE '%%ios%%' then PHONEID else null end ) new_consumers_ios " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')= %s " \
                "and p like '%%gtgj%%' "\
                "and PHONEID not in " \
                "(  " \
                "SELECT phoneid " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')< %s " \
                ") group by s_day " %(querydate_str, querydate_str)

        result_model_list = self.db.query_result(sql, New_consumers)
        return result_model_list



def activeUsersDaoTest():

    activeUser_object = ActiveUsersDao()
    results = activeUser_object.get_users_daily("20150415")

    # results = activeUser_object.get_users_monthly("20150401")
    print(results)
    for result in results:
        print(result)

def newUsersDaoTest():
    newUser_object = NewUsersDao()
    results = newUser_object.get_users_daily("20150412")
    for result in results:
        print(result.s_day, result.new_users)
    pass
def newConsumersDaoTest():
    newConsumers_object = NewConsumersDao()
    results = newConsumers_object.get_consumers_daily("20150412")
    for result in results:
        print(result.s_day, result.new_consumers)
    pass

def newConsumersFromGtDao():
    newConsumersFromGt_object = NewConsumersFromGtDao()
    results = newConsumersFromGt_object.get_consumers_daily("20150415")
    for result in results:
        print(result.s_day, result.new_consumers)
    pass


def orderDaoTest():
    order_object = OrderDao()
    results = order_object.get_orders_daily("20150401", "20150402")
    # results = order_object.get_orders_weekly("20150401", "20150417")
    # results = order_object.get_orders_monthly("20150401", "20150417")
    for result in results:
        print(result)
    pass

def consumersDaoTest():
    consumers_object = ConsumersDao()
    # results = consumers_object.get_consumers_daily("20150401", "20150402")
    # results = consumers_object.get_consumers_weekly("20150401", "20150417")
    # results = consumers_object.get_orders_monthly("20150401", "20150417")
    results = consumers_object.get_consumers_quarterly("20150101", "20150417")
    for result in results:
        print(result)
    pass

if __name__ == '__main__':
    consumersDaoTest()
    # activeUsersDaoTest()
    # newUsersDaoTest()
    # newConsumersDaoTest()
    # newConsumersFromGtDao()

    # orderDaoTest()
    pass