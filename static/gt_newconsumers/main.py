#coding=utf-8
__author__ = 'Administrator'
import logging

import update
import goal_gtgj_newconsmers_dao
import gtgj_new_consumers
import tools
import gtgj_newconsumers_service
import source_gt

def getTxt():
    source_gt.getYestodayTxt()
    pass

def main():
    s_yestoday ="20150309"
    # s_yestoday = tools.getYestoday()
    s_day = s_yestoday[0:4] + "-" + s_yestoday[4:6] + "-" + s_yestoday[6:8]
    o_gt_new_consumers = gtgj_new_consumers.New_consumers()
    i_yestoday_ios_newconsumers_count,i_yestoday_android_newconsumers_count = update.getYestodayNewConsumers(s_day=s_yestoday)
    o_gt_new_consumers.s_day = s_day
    o_gt_new_consumers.new_consumers_ios = i_yestoday_ios_newconsumers_count
    o_gt_new_consumers.new_consumers_android = i_yestoday_android_newconsumers_count
    o_gt_new_consumers.new_consumers = o_gt_new_consumers.new_consumers_ios + o_gt_new_consumers.new_consumers_android
    print(o_gt_new_consumers.s_day, o_gt_new_consumers.new_consumers_ios, o_gt_new_consumers.new_consumers)
    o_gt_new_consumers_list = []
    o_gt_new_consumers_list.append(o_gt_new_consumers)
    o_gt_new_consumers_service = gtgj_newconsumers_service.NewconsumersDailyService(o_gt_new_consumers_list)
    o_gt_new_consumers_service.main()
    pass



if __name__=="__main__":
    # getTxt()
    main()
    pass