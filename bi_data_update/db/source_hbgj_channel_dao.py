__author__ = 'zhangchao'
from source_hbgj_mysql import *
from source_hbgj_oracle import *
from domain.hbgj_channel_model import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')

# update hbgj_activeusers daily/weekly/monthly
# update newusers daily

# update hbgj_newconsumers daily
# update hbgj_from_gt_newconsumers daily


class BaseUserMysqlDao(Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        Mysql.__init__(self, dbtype=dbtype_dao)

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
    def query_result_by_setValue(self, sql, model_class):
        cursor = oracle_con()
        cursor.execute(sql)
        result = cursor.fetchall()
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
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass=Active_users):
        self.db = DBClass()
        self.ModelClass = ModelClass
    def get_users_daily(self, s_day, e_day):

        sql = "select distinct to_char(createtime,'yyyy-mm-dd') s_day, " \
            "SOURCE, " \
            "count(distinct userid) num "  \
            "from ACTIVE_USER_LOG " \
            "where createtime>=to_date(%s,'yyyymmdd') " \
            "and createtime<to_date(%s,'yyyymmdd') " \
            "group by to_char(createtime,'yyyy-mm-dd'), SOURCE " \
            "ORDER BY to_char(createtime,'yyyy-mm-dd'),num desc " % (s_day, e_day)


        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_users_weekly(self, s_day):

        sql = "select to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') s_day, " \
            "SOURCE, " \
            "count(distinct userid) num "  \
            "from ACTIVE_USER_LOG " \
            "where createtime>=to_date(%s, 'yyyymmdd')" \
            "group by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd'), SOURCE " \
            "order by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd'), num desc " % s_day
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def get_users_monthly(self, s_day):
        sql = "select to_char(trunc(createtime,'mm'),'yyyy-mm-dd') s_day, " \
            "SOURCE, " \
            "count(distinct userid) num "  \
            "from ACTIVE_USER_LOG " \
            "where createtime>=to_date(%s, 'yyyymmdd') " \
            "group by to_char(trunc(createtime,'mm'),'yyyy-mm-dd'), SOURCE " \
            "order by to_char(trunc(createtime,'mm'),'yyyy-mm-dd'), num desc " % s_day
        result_model_list=self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list


class NewUsersDao(object):
    def __init__(self, DBClass = BaseUserOracleDao, ModelClass =New_users):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_users_daily(self, s_day, e_day):
        sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day, " \
        "USER_CHANNEL, " \
        "count(*) num " \
        "from HBZJ_USER " \
        "where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') " \
        "and USER_LOGINDATE<to_date(%s, 'yyyymmdd') " \
        "group by to_char(USER_LOGINDATE,'yyyy-mm-dd'),USER_CHANNEL " \
        "ORDER BY s_day,num desc " %(s_day, e_day)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)

        return result_model_list

class OrderDao(object):
    def __init__(self, DBClass=BaseUserMysqlDao, ModelClass=Orders_source):
        self.db = DBClass()
        self.ModelClass =ModelClass

    def get_orders_daily(self, s_day, e_day):


        sql = "SELECT DATE_FORMAT(TR.createtime,'%%Y-%%m-%%d') s_day, p,PAYPRICE, 1 order_count, " \
            "(SELECT COUNT(1) FROM TICKET_ORDERDETAIL TOD2 WHERE TOD2.ORDERID=TR.ORDERID) TICKET_COUNT " \
            "FROM TICKET_ORDER TR " \
            "where TR.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TR.createtime,'%%Y%%m%%d')>=%s " \
            "and DATE_FORMAT(TR.createtime,'%%Y%%m%%d')<%s   " %(s_day, e_day)

        source_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)

        goal_model_list = orderModelList_source_to_goal(source_model_list)

        result_model_list = meargeList(goal_model_list)
        return result_model_list

def activeUsersDaoTest():

    activeUser_object = ActiveUsersDao()
    # results = activeUser_object.get_users_daily("20150601", "20150603")
    # results = activeUser_object.get_users_weekly("20150601")
    results = activeUser_object.get_users_monthly("20150601")

    print(results)
    for result in results:
        print(result)

def newUsersDaoTest():
    newUser_object = NewUsersDao()
    results = newUser_object.get_users_daily("20150601", "20150603")
    for result in results:
        print(result.s_day, result.new_users)
    pass



def orderDaoTest():
    order_object = OrderDao()
    results = order_object.get_orders_daily("20150401", "20150417")
    for result in results:
        print(result)
    pass

# def test():
#     order_object = OrderDao()
#     order_source_list = order_object.get_orders_daily("20150401", "20150403")
#
#
#     s_day_list = []
#     channel_list = []
#
#
#     channel_set = set(channel_list)
#     s_day_set = set(s_day_list)
#     data_dict = defaultdict(dict)
#
#     # for s_day in
#
#     for order_source in order_source_list:
#         s_day = order_source.s_day
#         p = order_source.p
#         payprice = order_source.payprice
#         order_count = order_source.order_count
#         ticket_count = order_source.ticket_count
#         channel = p.strip().split(",")[0]
#
#         s_day_list.append(s_day)
#         channel_list.append(channel)
#
#         temp_dict = defaultdict(list)
#         temp_dict[channel] = [payprice, order_count, ticket_count]
#
#         data_dict[s_day] = temp_dict
#         # data_dict['channel'] = channel
#         # data_dict['payprice'] = payprice
#         # data_dict['order_count'] = order_count
#         # data_dict['ticket_count'] = ticket_count
#
#
#     channel_set = set(channel_list)
#     s_day_set = set(s_day_list)
#
#
#
#     print(data_dict)
#     #
#     # for s_day in s_day_set:
#     #     for channel in channel_set:
#     #         o_orders_goal = Orders_goal()
#     #
#     #
#     #
#     #
#     #
#     #
#     #     print(s_day,p,channel,payprice,order_count,ticket_count)
#
#
#
# def test2():
#     order_object = OrderDao()
#     order_source_list = order_object.get_orders_daily("20150401", "20150403")
#
#
#     s_day_list = []
#     channel_list = []
#
#
#     channel_set = set(channel_list)
#     s_day_set = set(s_day_list)
#
#
#     data_list = []
#
#
#     for order_source in order_source_list:
#         data_dict = dict()
#         s_day = order_source.s_day
#         p = order_source.p
#         payprice = order_source.payprice
#         order_count = order_source.order_count
#         ticket_count = order_source.ticket_count
#         channel = p.strip().split(",")[0]
#
#         data_dict['s_day'] = s_day
#         data_dict['channel'] = channel
#         data_dict['payprice'] = payprice
#         data_dict['order_count'] = order_count
#         data_dict['ticket_count'] = ticket_count
#         # data_list.append([s_day, channel, payprice, order_count, ticket_count])
#         data_list.append(data_dict)
#
#     df = DataFrame(data_list)
#     df_result = df.groupby([df['channel'], df['s_day']]).sum()
#
#     print(df_result, type(df_result))
#
#     # print(df.groupby([df[0], df[1]]).sum())
#     # print(df)
#     #
#     # for name, group in df.groupby(level=['s_day', 'channel']):
#     #     print(name,group)
#
#
# def test3():
#     order_object = OrderDao()
#     order_source_list = order_object.get_orders_daily("20150401", "20150403")
#
#
#     s_day_list = []
#     channel_list = []
#
#
#
#     for order_source in order_source_list:
#
#         s_day = order_source.s_day
#         p = order_source.p
#         channel = p.strip().split(",")[0]
#         s_day_list.append(s_day)
#         channel_list.append(channel)
#     channel_set = set(channel_list)
#     s_day_set = set(s_day_list)
#
#     order_dict = defaultdict(dict)
#     amount_dict = dict(dict())
#     ticket_dict = dict(dict())
#
#     for order_source in order_source_list:
#         temp_dict = defaultdict(list)
#         s_day = order_source.s_day
#         p = order_source.p
#         payprice = order_source.payprice
#         order_count = order_source.order_count
#         ticket_count = order_source.ticket_count
#         channel = p.strip().split(",")[0]
#         temp_dict[channel] = [payprice, order_count, ticket_count]
#         order_dict[s_day].append(temp_dict)
#         print(temp_dict)
#     print(order_dict)
#
#
# def test4():
#
#     order_object = OrderDao()
#     order_source_list = order_object.get_orders_daily("20150401", "20150403")
#
#
#     s_day_list = []
#     channel_list = []
#
#     channel_set = set(channel_list)
#     s_day_set = set(s_day_list)
#
#
#     data_list = []
#
#
#     for order_source in order_source_list:
#         data_dict = dict()
#         s_day = order_source.s_day
#         p = order_source.p
#         payprice = order_source.payprice
#         order_count = order_source.order_count
#         ticket_count = order_source.ticket_count
#         channel = p.strip().split(",")[0]
#
#         data_dict['s_day'] = s_day
#         data_dict['channel'] = channel
#         data_dict['payprice'] = payprice
#         data_dict['order_count'] = order_count
#         data_dict['ticket_count'] = ticket_count
#
#         data_list.append([s_day,channel,payprice,order_count,ticket_count])
#     print(data_list)
#     from itertools import groupby
#     from operator import itemgetter
#     iterator = groupby(data_list, itemgetter(1))
#     for key, items in iterator:
#         print key
#         for subitem in items:
#             print subitem
#     # print "\n"
#
#     # print(iterator.next())
#     pass
#
#
#
# def test5():
#     order_object = OrderDao()
#     order_source_list = order_object.get_orders_daily("20150401", "20150601")
#
#     data_list = []
#
#
#     for order_source in order_source_list:
#         data_dict = dict()
#         s_day = order_source.s_day
#         p = order_source.p
#         payprice = order_source.payprice
#         order_count = order_source.order_count
#         ticket_count = order_source.ticket_count
#         channel = p.strip().split(",")[0]
#         o_order_goal = Orders_goal()
#         o_order_goal.setValues([s_day, channel, payprice, order_count, ticket_count])
#
#         data_list.append(o_order_goal)
#
#     return data_list



if __name__ == '__main__':
    # activeUsersDaoTest()
    # newUsersDaoTest()
    # orderDaoTest()


    orderDaoTest()
    # activeUsersDaoTest()
    # newUsersDaoTest()
    # newConsumersDaoTest()
    # newConsumersFromGtDao()

    # orderDaoTest()
    pass