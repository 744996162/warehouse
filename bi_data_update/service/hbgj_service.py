__author__ = 'Administrator'

from util import dateutil
# from db import source_gtgj_dao
from db import source_hbgj_dao
from db import goal_dao


def hb_active_daily(s_day):
    try:
        o_source = source_hbgj_dao.ActiveUsersDao()
        o_goal = goal_dao.HbUpdateDao()
        users_results_daily = o_source.get_users_daily(s_day)
        o_goal.activeDailyUpdate(users_results_daily)
        for user in users_results_daily:
            print(user)
    except Exception as e:
        print(e)

def hb_active_weekly(s_day):
    try:
        o_source = source_hbgj_dao.ActiveUsersDao()
        o_goal = goal_dao.HbUpdateDao()
        users_results_weekly = o_source.get_users_weekly(s_day)
        o_goal.activeWeeklyUpdate(users_results_weekly)
        for user in users_results_weekly:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_active_monthly(s_day):
    try:
        o_source = source_hbgj_dao.ActiveUsersDao()
        o_goal = goal_dao.HbUpdateDao()
        users_results_monthly = o_source.get_users_monthly(s_day)
        o_goal.activeMonthlyUpdate(users_results_monthly)
        for user in users_results_monthly:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_newusers_daily(s_day):

    try:
        o_source = source_hbgj_dao.NewUsersDao()
        o_goal = goal_dao.HbUpdateDao()
        users_result_daily = o_source.get_users_daily(s_day)
        o_goal.newusersDailyUpdate(users_result_daily)
        for user in users_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass


def hb_consumers_daily(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.ConsumersDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_daily = o_source.get_consumers_daily(s_sday, e_sday)
        o_goal.consumersDailyUpdate(user_result_daily)
        for user in user_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_consumers_weekly(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.ConsumersDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_weekly = o_source.get_consumers_weekly(s_sday, e_sday)
        o_goal.consumersWeeklyUpdate(user_result_weekly)
        for user in user_result_weekly:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_consumers_monthly(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.ConsumersDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_monthly = o_source.get_consumers_monthly(s_sday, e_sday)
        o_goal.consumersMonthlyUpdate(user_result_monthly)
        for user in user_result_monthly:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_consumers_quarterly(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.ConsumersDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_quarterly = o_source.get_consumers_quarterly(s_sday, e_sday)
        o_goal.consumersQuarterlyUpdate(user_result_quarterly)
        for user in user_result_quarterly:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_orders_daily(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.OrderDao()
        o_goal = goal_dao.HbUpdateDao()
        order_result_daily = o_source.get_orders_daily(s_sday, e_sday)
        o_goal.orderDailyUpdate(order_result_daily)
        for order in order_result_daily:
            print(order)
    except Exception as e:
        print(e)
    pass

def hb_orders_weekly(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.OrderDao()
        o_goal = goal_dao.HbUpdateDao()
        order_result_weekly = o_source.get_orders_weekly(s_sday, e_sday)
        o_goal.orderWeeklyUpdate(order_result_weekly)
        for order in order_result_weekly:
            print(order)
    except Exception as e:
        print(e)
    pass

def hb_orders_monthly(s_sday, e_sday):
    try:
        o_source = source_hbgj_dao.OrderDao()
        o_goal = goal_dao.HbUpdateDao()
        order_result_monthly = o_source.get_orders_monthly(s_sday, e_sday)
        o_goal.orderMonthlyUpdate(order_result_monthly)
        for order in order_result_monthly:
            print(order)
    except Exception as e:
        print(e)
    pass

def hb_newconsumers_daily(s_day):
    try:
        o_source = source_hbgj_dao.NewConsumersDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_daily = o_source.get_consumers_daily(s_day)
        o_goal.newconsumersDailyUpdate(user_result_daily)
        for user in user_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass

def hb_newconsumers_from_GT_daily(s_day):
    try:
        o_source = source_hbgj_dao.NewConsumersFromGtDao()
        o_goal = goal_dao.HbUpdateDao()
        user_result_daily = o_source.get_consumers_daily(s_day)
        o_goal.newconsumersFromGtDailyUpdate(user_result_daily)
        for user in user_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass

if __name__ == "__main__":
    # today = dateutil.DateUtil.getToday()
    yestoday= dateutil.DateUtil.getYestaday()
    print(yestoday)
    # gt_update_daily()

    # hb_newconsumers_daily(yestoday)
    hb_newconsumers_from_GT_daily("20150414")
    hb_newconsumers_from_GT_daily(yestoday)
    # hb_active_daily(yestoday)
    # gt_active_weekly(yestoday)