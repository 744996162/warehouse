__author__ = 'Administrator'
import cx_Oracle
import query_date


def oracle_con():
    ip = '58.83.130.90'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    db = cx_Oracle.connect('et', 'atet501', dsn_tns)
    cursor = db.cursor()
    return cursor


def hbgj_lcd(start_date_str,end_date_str):

    sql_all="select count(distinct userid) " \
    "from ACTIVE_USER_LOG " \
    "where createtime>=to_date(2015-04-01, 'yyyy-mm-dd') " \
    "and createtime<to_date(2015-05-01, 'yyyy-mm-dd') " \
    "and userid in(  " \
    "select user_id  " \
    "from HBZJ_USER  " \
    "where USER_LOGINDATE>=to_date(%s, 'yyyy-mm-dd') " \
    "and USER_LOGINDATE<to_date(%s, 'yyyy-mm-dd') " \
    ") "  %(start_date_str, end_date_str)

    sql_ios = "select count(distinct userid) " \
    "from ACTIVE_USER_LOG " \
    "where createtime>=to_date('2015-04-01', 'yyyy-mm-dd') " \
    "and createtime<to_date('2015-05-01', 'yyyy-mm-dd') " \
    "and userid in(  " \
    "select user_id  " \
    "from HBZJ_USER  " \
    "where USER_LOGINDATE>=to_date(%s, 'yyyy-mm-dd') " \
    "and USER_LOGINDATE<to_date(%s, 'yyyy-mm-dd') " \
    "and (USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%') " \
    ") "  % (start_date_str, end_date_str)
    #
    # sql_test="select count(distinct userid) " \
    # "from ACTIVE_USER_LOG " \
    # "where createtime>=to_date('2014-12-01', 'yyyy-mm-dd') " \
    # "and createtime<to_date('2015-01-01', 'yyyy-mm-dd') " \
    # "and userid in(  " \
    # "select user_id  " \
    # "from HBZJ_USER  " \
    # "where USER_LOGINDATE>=to_date('2014-11-01', 'yyyy-mm-dd') " \
    # "and USER_LOGINDATE<to_date('2014-12-01', 'yyyy-mm-dd') " \
    # ") "

    print(sql_ios)
    cursor = oracle_con()
    # cursor.execute(sql_all)
    cursor.execute(sql_ios)
    result = cursor.fetchall()
    users = []
    if not result:
        return False
    for row in result:
        users.append(start_date_str)
        users.append(row[0])
    return users

def test():
    file = open("result_lcd_all201505.txt", 'a')
    # file=open("result_lcd_ios201502.txt",'a')
    for i in range(2, 12, 1):
        end_date_str = query_date.hb_getMonthlyDate_lcd(i)
        start_date_str = query_date.hb_getMonthlyDate_lcd(i+1)
        # print(start_date_str,end_date_str)
        result = hbgj_lcd(start_date_str, end_date_str)
        print(result)
        out_str = str(result)
        file.write(out_str+"\n")
    pass

if __name__ == "__main__":

    # start_date_str="2014-11-01"
    # end_date_str="2014-12-01"

    # start_date_str=query_date.hb_getMonthlyDate_lcd(2)
    # end_date_str=query_date.hb_getMonthlyDate_lcd(1)
    # result=hbgj_lcd(start_date_str,end_date_str)
    # print(result)
    test()




