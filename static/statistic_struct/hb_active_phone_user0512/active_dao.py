__author__ = 'Administrator'
from db import source_oracle
from db import mysql

def get_active_users_oneday():
    sql = "select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5),sum(case when p LIKE '%%91ZS%%' or p LIKE '%%appstore%%' or p LIKE '%%juwan%%' or p LIKE '%%91PGZS%%' or p LIKE '%%kuaiyong%%' or p LIKE '%%TBT%%' or p LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
              "from ACTIVE_USER_LOG where createtime>=to_date(%s, 'yyyymmdd') group by to_char(createtime,'yyyy-mm-dd') order by  to_char(createtime,'yyyy-mm-dd')" % querydate_str

    con = source_oracle.oracle_con79()
    cursor = con.cursor()
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    s = []
    if not result:
        return  False
    for row in result:
        s.append(row[0])

    print(len(s))
    return s


def get_phone_users_all():
    pass


if __name__ == "__main__":



    pass