#ecoding=utf-8
__author__ = 'Administrator'
import cx_Oracle
from conf.conf import DBConf

# import sys
import os
# reload(sys)
# sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def oracle_con90():
    ip = '58.83.130.90'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    con = cx_Oracle.connect('et', 'atet501', dsn_tns)
    # cursor = con.cursor()
    return con

def oracle_con79():
    ip = '58.83.130.79'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    con = cx_Oracle.connect('flightdyn', 'flight0515', dsn_tns)
    # cursor = con.cursor()
    return con


class Oracle(object):
    #连接池对象
    _oracle_con_pool = None

    def __init__(self,dbtype="test"):
        self._conn = Oracle.__getcon(dbtype)
        self._cursor = self._conn.cursor
        self._type = dbtype
        pass

    @staticmethod
    def __getcon(dbtype="test"):
        _conf = DBConf.getInst()
        if Oracle._oracle_con_pool is None:
            if dbtype == "hbdt79":
                dsn_tns = cx_Oracle.makedsn(_conf.get_oracle('iphbdt79'), _conf.get_oracle('porthbdt79'), _conf.get_oracle("sidhbdt79"))
                Oracle._oracle_con_pool = cx_Oracle.connect(_conf.get_oracle('usernamehbdt79'), _conf.get_oracle('passwordhbdt79'), dsn_tns)
            elif dbtype == "hbgj90":
                dsn_tns = cx_Oracle.makedsn(_conf.get_oracle('iphbgj90'), _conf.get_oracle('porthbgj90'), _conf.get_oracle("sidhbgj90"))
                Oracle._oracle_con_pool = cx_Oracle.connect(_conf.get_oracle('usernamehbgj90'), _conf.get_oracle('passwordhbgj90'), dsn_tns)
            else:
                dsn_tns = cx_Oracle.makedsn(_conf.get_oracle('iptest'), _conf.get_oracle('porttest'), _conf.get_oracle("sidtest"))
                Oracle._oracle_con_pool = cx_Oracle.connect(_conf.get_oracle('usernametest'), _conf.get_oracle('passwordtest'), dsn_tns)

        return Oracle._oracle_con_pool





def hbdt_state_not_end(s_day):

    sql = "select count(*) num from DAY_FLY_DTINFO " \
          "where DTFS_FLIGHTDATE = '%s' and (DTFS_FLIGHTSTATE != '到达' and DTFS_FLIGHTSTATE != '取消') " \
          "and dtfs_flightdepcode in (select THREE_WORDS_CODE from AIRPORT_NATION_INFO) and dtfs_flightarrcode in (select THREE_WORDS_CODE from AIRPORT_NATION_INFO) "   % s_day

    # sql_u = sql.decode('utf-8')
    # sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate
    con = oracle_con79()
    cursor = con.cursor()
    print(sql)

    cursor.execute(sql)
    result = cursor.fetchall()
    # users=[]
    s = []
    if not result:
        return  False
    for row in result:
        # user = hbgj_new_users.New_users()
        # user.s_day = row[0]
        # user.new_users = row[1]
        # user.new_users_ios = row[2]
        # # t=row[1]-row[2]
        # user.new_users_android=row[1]-row[2]
        s.append(row[0])
        # print user.s_day,user.new_users

    return s


def test():
    o_oracle = Oracle(dbtype='hbgj90')
    # sql1="select * from  car_area "
    print(o_oracle._conn)
    # sql_test.update(sql2)
    # sql_test.end()
    pass


if __name__=="__main__":
    # test()

    # t = oracle_con90()
    s = hbdt_state_not_end("2015-03-20")
    # print(t.cursor())
    print(s)
    # print sys.getdefaultencoding()
    pass



