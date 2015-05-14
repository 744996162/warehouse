__author__ = 'Administrator'

from db import source_gtgj_mysql
import datetime

def getYestoday(dateformat="%Y%m%d"):
    today = datetime.datetime.now()
    yestoday = today + datetime.timedelta(days=-1)
    s_yestoday = yestoday.strftime(dateformat)
    return s_yestoday

    pass

def getData():
    yestoday = "'" +  getYestoday() + "'"

    sql = "SELECT count(DISTINCT userid) num FROM user_statistics "  \
            "where DATE_FORMAT(end_time,'%Y%m%d')>=" + yestoday

    print(sql)

    mysql = source_gtgj_mysql.Mysql(dbtype="gtgj89")
    results = mysql.get_all(sql)


    if not results:
        return False
    for row in results:
        print(row[0])
        return str(row[0])


def value_to_txt():
    yestoday = getYestoday()
    value = str(getData())

    file_out = open("out.txt", "a")
    file_out.write(yestoday + "\t" + value + "\n")

    pass

if __name__ == "__main__":
    value_to_txt()
    # getData()
    # print(yestoday)
    pass