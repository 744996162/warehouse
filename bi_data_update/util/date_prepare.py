__author__ = 'Administrator'
import datetime

today = datetime.datetime.now()

def getToday(dateformat="%Y%m%d"):
    today = datetime.datetime.now()
    s_today = today.strftime(dateformat)
    return s_today


def getYestoday(dateformat="%Y%m%d"):
    yestoday = today + datetime.timedelta(days=-1)
    s_yestoday = yestoday.strftime(dateformat)
    return s_yestoday

def getHisday(delta=1,dateformat="%Y%m%d"):
    yestoday = today + datetime.timedelta(days=-delta)
    s_yestoday = yestoday.strftime(dateformat)
    return s_yestoday


def getThisMonday(dateformat="%Y%m%d"):
    weekday = today.isoweekday()
    delta = -1 + weekday
    thisMonday = today+datetime.timedelta(days=-delta)
    s_thisMonday = thisMonday.strftime(dateformat)
    return s_thisMonday

def getLastMonday(dateformat="%Y%m%d"):
    weekday = today.isoweekday()
    delta = 6 + weekday
    lastMonday = today+datetime.timedelta(days=-delta)
    s_lastMonday = lastMonday.strftime(dateformat)
    return s_lastMonday

def getHisMonday(delta=1, dateformat="%Y%m%d"):
    weekday = today.isoweekday()
    delta = 7*(delta-1) + 6 + weekday
    hisMonday = today+datetime.timedelta(days=-delta)
    s_hisMonday = hisMonday.strftime(dateformat)

    return s_hisMonday


def getLastDay1(dateformat="%Y%m%d"):
    lastDay1 = (today.replace(day=1) - datetime.timedelta(1)).replace(day=1)
    s_lastDay1 = lastDay1.strftime(dateformat)
    return s_lastDay1

def getThisDay1(dateformat="%Y%m%d"):
    thisDay1 = today.replace(day=1)
    s_thisDay1 = thisDay1.strftime(dateformat)
    return s_thisDay1


def getHisDay1(delta=1, dateformat="%Y%m%d"):
    temp_date = today.replace(day=1)
    for i in range(delta):
        temp_date = (temp_date - datetime.timedelta(1)).replace(day=1)
    s_hisDay1 = temp_date.strftime(dateformat)
    return s_hisDay1

if __name__ == "__main__":
    print(getHisday(2))
    print(getYestoday())
    print(getThisMonday())
    print(getLastMonday())
    print(getHisMonday(2))

    pass







