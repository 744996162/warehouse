__author__ = 'Administrator'
import cx_Oracle

def oracle_con():
    ip = '58.83.130.79'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    db = cx_Oracle.connect('et', 'atet501', dsn_tns)
    cursor = db.cursor()
    return cursor