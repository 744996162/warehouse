#coding=utf-8
__author__ = 'Administrator'
import datetime
def test():
    today=datetime.datetime.now()
    t=today.strftime('%Y%m%d')

    weekday=today.strftime("%w")
    # week=today.isoweekday()
    week=today.strftime("%U")

    x=today.replace()
    print(t,week)

def gt_getWeeklyDate(date=datetime.datetime.now()):
    #计算八周前的周日
    weekday=date.isoweekday()
    delta=56+weekday
    date2=date+datetime.timedelta(days=-delta)
    date_str=date2.strftime('%Y%m%d')
    return date_str

def gt_getMonthlyDate(date=datetime.datetime.now()):
    #计算一个月前的1号
    date2=date+datetime.timedelta(days=-32)
    date3=date2.replace(day=1)
    date3_str=date3.strftime('%Y%m%d')
    return date3_str
    pass


def hb_getWeeklyDate(date=datetime.datetime.now()):
    #计算两周前的周一
    weekday=date.isoweekday()
    delta=6+weekday
    date2=date+datetime.timedelta(days=-delta)
    date_str=date2.strftime('%Y-%m-%d')
    return date_str

def hb_getMonthlyDate(date=datetime.datetime.now()):
    #计算这个月的1号，缓7天(防止数据出问题)
    date2=date+datetime.timedelta(days=-7)
    date3=date2.replace(day=1)
    date3_str=date3.strftime('%Y-%m-%d')
    return date3_str



if __name__=="__main__":
    today=datetime.datetime.now()
    today=datetime.date(2014,9,21)
    # week=gt_getWeeklyDate(today)
    # month=gt_getMonthlyDate(today)
    week=hb_getWeeklyDate(today)
    month=hb_getMonthlyDate()
    print(week,month)
    pass
