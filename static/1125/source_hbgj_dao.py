__author__ = 'Administrator'
import cx_Oracle
import hbgj_active_users

def oracle_con():
    ip = '58.83.130.79'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    db = cx_Oracle.connect('et', 'atet501', dsn_tns)
    cursor = db.cursor()
    return cursor


def hbgj_active_user_ios():
    # sql="select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5) user_num from DEVICE_USER_LOG group by to_char(createtime,'yyyy-mm-dd') order by to_char(createtime,'yyyy-mm-dd')"

    # sql2="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id) from HBZJ_USER where USER_LOGINDATE>=to_date('2014-09-04', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    # sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%91ZS%' or USER_CHANNEL LIKE '%appstore%' or USER_CHANNEL LIKE '%juwan%' or USER_CHANNEL LIKE '%91PGZS%' or USER_CHANNEL LIKE '%kuaiyong%' or USER_CHANNEL LIKE '%TBT%' or USER_CHANNEL LIKE '%PPZS%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date('2014-11-10', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    # sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate
    sql_ios="select distinct(userid),p,platform from ACTIVE_USER_LOG where p like '%ios%' and  p like '%hbgj%' and (p not like '%,3.9%' and p not like '%,4.0%' and p not like '%,4.1%')"
    cursor = oracle_con()
    cursor.execute(sql_ios)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_active_users.Active_users()
        user.p = row[1]
        user.platform = row[2]
        users.append(user)
        # print user.s_day,user.new_users
    return users

def hbgj_active_user_android():
    # sql="select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5) user_num from DEVICE_USER_LOG group by to_char(createtime,'yyyy-mm-dd') order by to_char(createtime,'yyyy-mm-dd')"

    # sql2="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd')  s_day,count(distinct user_id) from HBZJ_USER where USER_LOGINDATE>=to_date('2014-09-04', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    # sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%91ZS%' or USER_CHANNEL LIKE '%appstore%' or USER_CHANNEL LIKE '%juwan%' or USER_CHANNEL LIKE '%91PGZS%' or USER_CHANNEL LIKE '%kuaiyong%' or USER_CHANNEL LIKE '%TBT%' or USER_CHANNEL LIKE '%PPZS%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date('2014-11-10', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    # sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate
    sql_ios="select distinct(userid),p,platform from ACTIVE_USER_LOG where p like '%android%' and  p like '%hbgj%' and (p not like '%,3.9%' and p not like '%,4.0%' and p not like '%,4.1%')"
    cursor = oracle_con()
    cursor.execute(sql_ios)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_active_users.Active_users()
        user.p = row[1]
        user.platform = row[2]
        users.append(user)
        # print user.s_day,user.new_users
    return users


hbgj_version_ios=[""]
hbgj_version_android=[""]
ios_version=["ios8","ios7","ios6","ios5","ios4"]
android_version=["android.5.0","android.4.4","android.4.3","android.4.2","android.4.1","android.4.0","android.3","android.2.3","android.2.2","android.2.1","android.2.0","android.1.6","android.1.5"]

def test_ios():
    # new_users=hbgj_new_user()
    # for user in new_users:
    #     print user.s_day,user.new_users,user.new_users_ios,user.new_users_android

    # active_users=hbgj_active_user_daily()
    result_file="G:/hb_ios_oldversion.txt"
    result_output=open(result_file,'w')
    active_users=hbgj_active_user_ios()
    # active_users=hbgj_active_user_monthly()
    for user in active_users:
        result_output.write(user.p+'\n')
        print(user.p)


def test_android():
    # new_users=hbgj_new_user()
    # for user in new_users:
    #     print user.s_day,user.new_users,user.new_users_ios,user.new_users_android

    # active_users=hbgj_active_user_daily()
    result_file="G:/hb_android_oldversion.txt"
    result_output=open(result_file,'w')
    active_users=hbgj_active_user_android()
    # active_users=hbgj_active_user_monthly()
    for user in active_users:
        result_output.write(user.p+'\n')
        print(user.p)
    #
    # new_users=hbgj_new_user()
    # for user in new_users:
    #     print user.s_day,user.new_users

def test():
    print(len(android_version),android_version)
    pass

if __name__=="__main__":
    # test_ios()
    # test_android()
    test()
    print "hello"
    pass




