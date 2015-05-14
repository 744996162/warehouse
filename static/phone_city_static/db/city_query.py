
__author__ = 'Administrator'
import sys

from source_mysql import *

sys.path.append('..')


class PhoneUserDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='local')
        # Mysql.__init__(self,dbtype='local')

    def query_city(self,phone_number):


        sql_phone="select %s from mobile_area_mapping"
        sql_mapping="select sheng,shi from mobile_area_mapping where mobile=%s"

        arg=[phone_number]
        result=self.get_one(sql_mapping,arg)
        if not result:
            return  "0","0"
        else:
            return result['sheng'],result['shi']


def test():
    test1=PhoneUserDao()
    # results=test1.get_users_daily()
    sheng,shi=test1.query_city(1304682)
    print shi


if __name__ == '__main__':
    test()
    print("OK")
