#coding=utf-8
__author__ = 'Administrator'
import datetime
def test():
    today=datetime.datetime.now()
    t=today.strftime('%Y%m%d')

    #
    weekday=today.strftime("%w")
    # week=today.isoweekday()
    week=today.strftime("%U")

    x=today.replace()
    print(t,week)

def getWeeklyDate(date=datetime.datetime.now()):
    #计算八周前的周一
    weekday=today.isoweekday()
    delta=55+weekday
    date2=date+datetime.timedelta(days=-delta)
    date_str=date2.strftime('%Y%m%d')
    return date_str

def getMonthlyDate(date=datetime.datetime.now()):
    #计算两个月前的1号
    date2=date+datetime.timedelta(days=-58)
    date3=date2.replace(day=1)
    date3_str=date3.strftime('%Y%m%d')
    return date3_str
    pass


if __name__=="__main__":
    today=datetime.datetime.now()
    today=datetime.date(2014,11,20)
    week=getWeeklyDate()
    month=getMonthlyDate(today)
    print(week,month)
    pass
