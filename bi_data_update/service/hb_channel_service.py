__author__ = 'Administrator'

from db import source_hbgj_channel_dao
from db import goal_channel_dao


from util import dateutil
# from db import source_gtgj_dao
from db import source_hbgj_dao
from db import goal_dao


def hb_channel_active_daily(s_day, e_day):
    try:
        o_source = source_hbgj_channel_dao.ActiveUsersDao()
        o_goal = goal_channel_dao.HbChannelUpdateDao()
        users_results_daily = o_source.get_users_daily(s_day, e_day)
        o_goal.activeDailyUpdate(users_results_daily)
        for user in users_results_daily:
            print(user)
    except Exception as e:
        print(e)


def hb_channel_new_users_daily(s_day, e_day):
    try:
        o_source = source_hbgj_channel_dao.NewUsersDao()
        o_goal = goal_channel_dao.HbChannelUpdateDao()
        users_results_daily = o_source.get_users_daily(s_day, e_day)
        o_goal.newusersDailyUpdate(users_results_daily)
        for user in users_results_daily:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_channel_order_daily(s_day, e_day):
    try:
        o_source = source_hbgj_channel_dao.OrderDao()
        o_goal = goal_channel_dao.HbChannelUpdateDao()
        users_results_daily = o_source.get_orders_daily(s_day, e_day)
        o_goal.orderDailyUpdate(users_results_daily)
        for user in users_results_daily:
            print(user)
    except Exception as e:
        print(e)

    pass

if __name__ == "__main__":
    # o_source = source_hbgj_channel_dao.ActiveUsersDao()
    # users_results_daily = o_source.get_users_daily("20150601", "20150602")
    # for user in users_results_daily:
    #     print(user)


    # hb_channel_active_daily("20150602", "20150619")
    # hb_channel_order_daily("20150601", "20150619")
    #
    # o_source = source_hbgj_channel_dao.NewUsersDao()
    # users_results_daily = o_source.get_users_daily("20150101", "20150102")
    # for user in users_results_daily:
    #     print(user)

    hb_channel_new_users_daily("20150530", "20150619")


    # o_source = source_hbgj_channel_dao.OrderDao()
    # users_results_daily = o_source.get_orders_daily("20150601", "20150602")
    # for user in users_results_daily:
    #     print(user)
    pass