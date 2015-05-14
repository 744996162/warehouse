__author__ = 'Administrator'
import source_gt_uid

def getHis():
    sql="select uid " \
        "from user_order " \

    pass

def getUid(s_day):
    sql="select uid " \
        "from user_order " \
        "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')=%s " % s_day

    sql2="select uid " \
        "from user_order " \
        "where i_status=3 and DATE_FORMAT(create_time,'%%Y%%m%%d')='20150102' "
    print(sql2)
    pass

if __name__=="__main__":
    getUid('20150102')
    pass