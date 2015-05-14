#coding=utf-8
__author__ = 'zhangchao'
from DBUtils.PooledDB import PooledDB
from pymysql.cursors import DictCursor
import pymysql as MySQLdb
import sys, string
sys.path.append('..')
from conf.conf import *

class Mysql(object):
    #连接池对象
    _mysql_pool = None
    def __init__(self, dbtype='local'):
        self._conn = Mysql.__get_conn(dbtype)
        self._cursor = self._conn.cursor()
        self._type = dbtype

    @staticmethod
    def __get_conn(dbtype='local'):
        _conf = DBConf.getInst()
        if Mysql._mysql_pool is None:
         #   MySQLdb.install_as_MySQLdb()
            if dbtype == 'gtgj102':
                Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=_conf.get_mysql('hostgtgj102'), port=string.atoi(_conf.get_mysql('portgtgj102')), user=_conf.get_mysql('usergtgj102'), passwd=_conf.get_mysql('passwordgtgj102'), database=_conf.get_mysql('databasegtgj102'), charset='utf8')

            elif dbtype == "gtgj89":
                 Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=_conf.get_mysql('hostgtgj89'), port=string.atoi(_conf.get_mysql('portgtgj89')), user=_conf.get_mysql('usergtgj89'), passwd=_conf.get_mysql('passwordgtgj89'), database=_conf.get_mysql('databasegtgj89'), charset='utf8')

            elif dbtype == "hbgj79":
                 Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=_conf.get_mysql('hosthbgj79'), port=string.atoi(_conf.get_mysql('porthbgj79')), user=_conf.get_mysql('userhbgj79'), passwd=_conf.get_mysql('passwordhbgj79'), database=_conf.get_mysql('databasehbgj79'), charset='utf8')

            elif dbtype == "hbgj79_account":
                 Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=_conf.get_mysql('hosthbgj79_account'), port=string.atoi(_conf.get_mysql('porthbgj79_account')), user=_conf.get_mysql('userhbgj79_account'), passwd=_conf.get_mysql('passwordhbgj79_account'), database=_conf.get_mysql('databasehbgj79_account'), charset='utf8')

            elif dbtype == "bi79":
                Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, host=_conf.get_mysql('hostbi79'), port=string.atoi(_conf.get_mysql('portbi79')), user=_conf.get_mysql('userbi79'), passwd=_conf.get_mysql('passwordbi79'), database=_conf.get_mysql('databasebi79'), charset='utf8')

            elif dbtype == "local":
                Mysql._mysql_pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,host=_conf.get_mysql('hostlocal'), port=string.atoi(_conf.get_mysql('portlocal')), user=_conf.get_mysql('userlocal'), passwd=_conf.get_mysql('passwordlocal'), database=_conf.get_mysql('databaselocal'), charset='utf8', cursorclass=DictCursor)
        return Mysql._mysql_pool.connection()

    def get_all(self, sql, params=None):
        if params is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, params)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def get_one(self, sql, params=None):
        if params is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, params)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def get_many(self, sql, num, params=None):
        if params is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, params)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insert_one(self, sql, value):
        self._cursor.execute(sql, value)
        return self.__get_insertid()

    def insert_many(self, sql, values):
        count = self._cursor.executemany(sql, values)
        return count

    def __get_insertid(self):
        self._cursor.execute('select @@IDENTITY as id')
        result = self._cursor.fetchall()
        return result[0]['id']

    def update(self, sql, params=None):
        if params is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, params)
        return count

    def delete(self, sql, params=None):
        return self.__query(sql, params)

    def __query(self, sql, params=None):
        if params is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, params)
        return count

    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

def test():
    sql_test=Mysql(dbtype='hbgj')
    sql1="select * from  car_area "
    print(sql_test._cursor.execute(sql1))
    # sql_test.update(sql2)
    sql_test.end()
    pass


if __name__=="__main__":
    test()
    pass