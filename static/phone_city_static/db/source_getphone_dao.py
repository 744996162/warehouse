__author__ = 'Administrator'
import sys

from source_mysql import *

sys.path.append('..')
from phone.domain import hbgj_phoneuser

class PhoneUserDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='hbgj')
        # Mysql.__init__(self,dbtype='local')

    def get_phone_users_all(self):
        file_out='phone_user.txt'
        output_txt=open(file_out,'w')
        sql_phone="select phoneid,PHONE from phone_user"
        sql_mapping="select * from  mobile_area_mapping "
        result=self.get_all(sql_phone)
        users=[]
        if not result:
            return False
        for row in result:
            user= hbgj_phoneuser.Phone_users()
            user.phoneid = row['phoneid']
            user.phone = row['PHONE']
            text=str(user.phoneid)+","+str(user.phone)
            output_txt.write(text+'\n')
            users.append(user)
        return users

    def text_write(self,text,file_out):
        output_txt=open(file_out,'w')
        output_txt.write(text+'\n')
        pass


def test():
    test1=PhoneUserDao()
    # results=test1.get_users_daily()
    results=test1.get_phone_users_all()
    # print(results)
    # results=test1.get_users_monthly()
    # print(results)
    # for row in results:
    #     print(row.s_day,row.active_users,row.active_users_ios,row.active_users_android)
    # print()

if __name__ == '__main__':
    test()
    print("OK")
