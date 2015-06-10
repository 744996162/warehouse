__author__ = 'Administrator'
from service import gtgj_service
from service import hbgj_service
from util.date_prepare import *

def hb_update():
    yestoday = getYestoday()
    today = getToday()
    his10DaysBefore = getHisday(15)
    this_Monday = getThisMonday()
    his_2_Monday = getHisMonday(delta=2)
    this_day1 = getThisDay1()
    last_day1 =getLastDay1()

    # hbgj_service.hb_active_daily(his10DaysBefore)
    # hbgj_service.hb_active_weekly(his_2_Monday)
    hbgj_service.hb_active_monthly(last_day1)
    #
    # hbgj_service.hb_consumers_daily(his10DaysBefore, today)
    # hbgj_service.hb_consumers_weekly(his_2_Monday, today)
    hbgj_service.hb_consumers_monthly(last_day1, today)
    # # hbgj_service.hb_consumers_quarterly("20090101", "20150416")
    #
    #
    # hbgj_service.hb_orders_daily(his10DaysBefore, today)
    # hbgj_service.hb_orders_weekly(his_2_Monday, today)
    hbgj_service.hb_orders_monthly(last_day1, today)


    # hbgj_service.hb_newusers_daily("20150422")

    # hbgj_service.hb_newconsumers_daily(yestoday)
    # hbgj_service.hb_newconsumers_from_GT_daily(yestoday)


    # hbgj_service.hb_newconsumers_daily("20150424")
    # hbgj_service.hb_newconsumers_from_GT_daily("20150424")

def gt_update():
    # yestoday = getYestoday()
    yestoday = getHisday(4)
    this_Monday = getThisMonday()
    his_2_Monday = getHisMonday(delta=2)
    this_day1 = getThisDay1()
    last_day1 =getLastDay1()

    # gtgj_service.gt_active_daily(yestoday)
    # gtgj_service.gt_active_weekly(this_Monday)
    # gtgj_service.gt_active_monthly(this_day1)
    #
    # gtgj_service.gt_newusers_daily(yestoday)

    # gtgj_service.gt_consumers_daily(yestoday)
    # gtgj_service.gt_consumers_weekly(his_2_Monday)
    gtgj_service.gt_consumers_monthly(last_day1)

if __name__ == "__main__":
    # hb_update()
    gt_update()
    pass



