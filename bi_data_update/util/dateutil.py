#encoding=utf-8
import datetime
import time
class DateUtil:

    @staticmethod
    def getToday():
        now_time = datetime.datetime.now()
        # yes_time = now_time + datetime.timedelta(days=-1)
        return now_time.strftime('%Y%m%d')
        # return time.strftime('%Y-%m-%d',time.localtime(tim.e.time()))

    @staticmethod
    def getYestaday():
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        return yes_time.strftime('%Y%m%d')
        # return time.strftime('%Y-%m-%d',time.localtime(time.time()))



    @staticmethod
    def str2str(date_str, fmt_src, fmt_dst):
        date = datetime.datetime.strptime(date_str, fmt_src)
        return date.strftime(fmt_dst)

	''' get the last time in seconds of the date in fmt_src '''
    @staticmethod
    def getlast_insecond(date_str_src, fmt_src):
        date_str_dest = DateUtil.str2str(date_str_src, fmt_src, '%Y-%m-%d')
        return date_str_dest + " 23:59:59"

    @staticmethod
    def getfirst_insecond(date_str_src, fmt_src):
        date_str_dest = DateUtil.str2str(date_str_src, fmt_src, '%Y-%m-%d')
        return date_str_dest + " 00:00:00"

    @staticmethod
    def get_date(year, month, day):
        date = datetime.datetime(year, month, day)

    @staticmethod
    def get_date_str(year, month, day):
        date = datetime.datetime(year, month, day)
        return DateUtil.date2str(date, '%Y-%m-%d')

    @staticmethod
    def is_leap(year):
        if year%4 != 0:
            return False
        else:
            if year%100 == 0 and year%400 != 0:
                return False
            else:
                return True

    @staticmethod
    def get_daysofmonth(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            if DateUtil.is_leap(year):
                return 29
            else:
                return 28

    @staticmethod
    def is_weekend(date_str, fmt='%Y-%m-%d'):
        date = DateUtil.str2date(date_str, fmt)
        return DateUtil.is_weekend2(date)

    @staticmethod
    def is_weekend2(date):
        dayofweek = date.isoweekday()
        if dayofweek in [6, 7]:
            return True
        else:
            return False

    @staticmethod
    def get_weekendsofmonth(year, month):
        days = DateUtil.get_daysofmonth(year, month)
        weekends = []
        for i in range(days):
            tmp_date = datetime.datetime(year, month, i+1)
            if DateUtil.is_weekend2(tmp_date):
                weekends.append(DateUtil.date2str(tmp_date, '%Y-%m-%d'))
        return weekends

    @staticmethod
    def get_worktimeofday(date):
        plus1 = datetime.timedelta(hours=8)
        plus2 = datetime.timedelta(hours=18)
        date_start = date+plus1
        date_end = date+plus2
        return DateUtil.date2str(date_start), DateUtil.date2str(date_end)

    @staticmethod
    def get_weektimeofmonth(year, month):
        days = DateUtil.get_daysofmonth(year, month)
        weekdays_start = []
        weekdays_end = []
        for i in range(days):
            tmp_date = datetime.datetime(year, month, i+1)
            if not DateUtil.is_weekend2(tmp_date):
                tmp_start, tmp_end = DateUtil.get_worktimeofday(tmp_date)
                weekdays_start.append(tmp_start)
                weekdays_end.append(tmp_end)
        return weekdays_start, weekdays_end

    @staticmethod
    def date2str(date, fmt_dst='%Y-%m-%d %H:%M:%S'):
        if not date:
            return None
        return date.strftime(fmt_dst)

    @staticmethod
    def str2date(date_str, fmt_dst='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.strptime(date_str, fmt_dst)

    @staticmethod
    def minus_days(date_str1, date_str2, fmt='%Y-%m-%d'):
        minus = DateUtil.str2date(date_str2, fmt)-DateUtil.str2date(date_str1, fmt)
        return minus.days

    @staticmethod
    def minus_insecond(date_str1, date_str2, fmt='%Y-%m-%d %H:%M:%S'):
        minus = DateUtil.str2date(date_str2, fmt) - DateUtil.str2date(date_str1, fmt)
        return minus.seconds

    @staticmethod
    def plus_hours(date_str, num, fmt='%Y-%m-%d %H:%M:%S'):
        date_dst = DateUtil.str2date(date_str, '%Y-%m-%d')+datetime.timedelta(hours=num)
        return DateUtil.date2str(date_dst, fmt)

    @staticmethod
    def minus_seconds(date, num, fmt='%Y-%m-%d %H:%M:%S'):
        date_dst = date-datetime.timedelta(seconds=num)
        return DateUtil.date2str(date_dst, fmt)

    @staticmethod
    def minus_minutes(date_str, num, fmt='%Y-%m-%d %H:%M:%S'):
        date = DateUtil.str2date(date_str)
        date_dst = date-datetime.timedelta(minutes=num)
        return DateUtil.date2str(date_dst, fmt)

    @staticmethod
    def plus_minutes(date_str, num, fmt='%Y-%m-%d %H:%M:%S'):
        return DateUtil.minus_minutes(date_str, -num, fmt)

    @staticmethod
    def now_date():
        return datetime.datetime.now()

    @staticmethod
    def yeaterday_str(fmt='%Y-%m-%d'):
        yesterday = DateUtil.now_date() - datetime.timedelta(days=1)
        return DateUtil.date2str(yesterday, fmt)

    @staticmethod
    def plus_days(date_str1, num, fmt='%Y-%m-%d'):
        date_dst = DateUtil.str2date(date_str1, fmt)+datetime.timedelta(days=num)
        return DateUtil.date2str(date_dst, fmt)

    @staticmethod
    def from_to(date_str_from, date_str_to, fmt='%Y-%m-%d'):
        days = DateUtil.minus_days(date_str_from, date_str_to, fmt)
        for i in range(days):
            yield DateUtil.plus_days(date_str_from, i, fmt)
    #@staticmethod
    #def get_worktime(year, month):


def test():
    #print DateUtil.str2str('2013-04-12', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S')
    #print DateUtil.getlast_insecond('2013-04-12', '%Y-%m-%d')
    #print DateUtil.getfirst_insecond('2013-04-12 12:12:12', '%Y-%m-%d %H:%M:%S')
    #print DateUtil.minus_days('2013-04-13', '2013-04-15')
    #print DateUtil.plus_days('2013-05-09', 9)
    #print DateUtil.plus_hours('2013-05-10', 4)
    #print DateUtil.minus_seconds('2013-04-12 12:12:12', 10)
    #print DateUtil.minus_insecond('2013-04-12 12:12:12', '2013-04-12 12:12:13')
    print DateUtil.get_daysofmonth(2013, 12)
    print DateUtil.is_weekend('2013-10-21')
    print DateUtil.get_weektimeofmonth(2013, 10)
    print DateUtil.get_date_str(2013, 10, 9)
    print DateUtil.yeaterday_str()
if __name__ == '__main__':
    test()