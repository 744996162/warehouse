__author__ = 'Administrator'

from util import dateutil
from db import source_gtgj_dao
from db import source_hbgj_dao

from db import goal_dao



def gt_active_daily(s_day):
    try:
        o_source = source_gtgj_dao.ActiveUsersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_results_daily = o_source.get_users_daily(s_day)
        o_goal.activeDailyUpdate(users_results_daily)
        for user in users_results_daily:
            print(user)
    except Exception as e:
        print(e)

def gt_active_weekly(s_day):
    try:
        o_source = source_gtgj_dao.ActiveUsersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_results_weekly = o_source.get_users_weekly(s_day)
        o_goal.activeWeeklyUpdate(users_results_weekly)
        for user in users_results_weekly:
            print(user)
    except Exception as e:
        print(e)
    pass

def gt_active_monthly(s_day):
    try:
        o_source = source_gtgj_dao.ActiveUsersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_results_monthly = o_source.get_users_monthly(s_day)
        o_goal.activeMonthlyUpdate(users_results_monthly)
        for user in users_results_monthly:
            print(user)
    except Exception as e:
        print(e)
    pass

def gt_newusers_daily(s_day):

    try:
        o_source = source_gtgj_dao.NewUsersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_result_daily = o_source.get_users_daily(s_day)
        o_goal.newusersDailyUpdate(users_result_daily)
        for user in users_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass


def gt_consumers_daily(s_day):
    try:
        o_source = source_gtgj_dao.ConsumersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_result_daily = o_source.get_consumers_daily(s_day)
        o_goal.consumersDailyUpdate(users_result_daily)
        for user in users_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass

def gt_consumers_weekly(s_day):
    try:
        o_source = source_gtgj_dao.ConsumersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_result_weekly = o_source.get_consumers_weekly(s_day)
        o_goal.consumersWeeklyUpdate(users_result_weekly)
        for user in users_result_weekly:
            print(user)
    except Exception as e:
        print(e)
    pass

def gt_consumers_monthly(s_day):
    try:
        o_source = source_gtgj_dao.ConsumersDao()
        o_goal = goal_dao.GtUpdateDao()
        users_result_monthly = o_source.get_consumers_monthly(s_day)
        o_goal.consumersMonthlyUpdate(users_result_monthly)
        for user in users_result_monthly:
            print(user)
    except Exception as e:
        print(e)
    pass


def gt_newconsumers_daily(s_day):
    try:
        o_source = source_gtgj_dao.NewConsumersDao()
        o_goal = goal_dao.GtUpdateDao()
        user_result_daily = o_source.get_consumers_daily(s_day)
        o_goal.newconsumersDailyUpdate(user_result_daily)
        for user in user_result_daily:
            print(user)
    except Exception as e:
        print(e)
    pass


if __name__ == "__main__":
    # today = dateutil.DateUtil.getToday()
    yestoday= dateutil.DateUtil.getYestaday()
    # print(yestoday)
    # gt_update_daily()
    # gt_newusers_daily(yestoday)
    # gt_active_weekly(yestoday)
    print(yestoday)
    gt_consumers_daily(yestoday)