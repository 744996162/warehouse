__author__ = 'Administrator'

import datetime

from db import source_gtgj_dao
from db import source_hbgj_dao

today = datetime.datetime.now()

def getThisDay1(dateformat="%Y%m%d"):
    thisDay1 = today.replace(day=1)
    s_thisDay1 = thisDay1.strftime(dateformat)
    return s_thisDay1

def getLastDay1(dateformat="%Y%m%d"):
    lastDay1 = (today.replace(day=1) - datetime.timedelta(1)).replace(day=1)
    s_lastDay1 = lastDay1.strftime(dateformat)
    return s_lastDay1


def main():
    thisDay1 = getThisDay1()
    lastDay1 = getLastDay1()

    print(thisDay1)
    print(lastDay1)

    o_object_hb = source_hbgj_dao.ActiveUsersDao()
    o_object_hb.get_users_uid_monthly_to_txt(lastDay1, data_path="")

    o_object_gt = source_gtgj_dao.ActiveUsersDao()
    o_object_gt.get_users_uid_monthly_to_txt(lastDay1, data_path="")

if __name__ == "__main__":
    main()
    # print("hello")