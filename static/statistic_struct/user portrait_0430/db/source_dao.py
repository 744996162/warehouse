#ecoding=utf-8
__author__ = 'Administrator'

import sys

from db import source_hbgj_mysql
from domain import hb_model
from domain import model

reload(sys)
sys.setdefaultencoding('utf-8')

class BaseUserMysqlDao(object):
    def __init__(self, dbtype):
        self.db = source_hbgj_mysql.Mysql(dbtype=dbtype)
        print(self.db._type)

    def query_result_by_setValue(self, sql, model_class):
        result=self.db.get_all(sql)
        users_model_list = []
        if not result:
            return False
        for row in result:
            value_list = []
            for value in row:
                value_list.append(value)
            o_model = model_class()
            o_model.setValues(value_list)
            users_model_list.append(o_model)
        return users_model_list


class OrderPhoneDao(object):
    """
    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass = hb_model.HbUser):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_user_identity(self):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """
        sql="select TICKET_ORDER.PHONEID,TICKET_ORDERDETAIL.PASSENGERIDCARDNO,TICKET_ORDER.CONTACTPHONE " \
            "from TICKET_ORDERDETAIL " \
            "join TICKET_ORDER " \
            "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
            "where TICKET_ORDER.ORDERSTATUE not in (2,12,21,51,75) " \
            "and DATE_FORMAT(TICKET_ORDER.CREATETIME,'%Y%m%d')<'20150401' " \
            "AND PASSENGERIDTYPE=0 "

        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list



class PhoneDictDao(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass=model.PhoneDict):
        self.dbname = "gtgj89"
        self.db = DBClass(self.dbname)
        # print(self.db)
        self.ModelClass =ModelClass

    def get_result(self):

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        if self.dbname == "gtgj89":
            sql = "select phone_num,province,city from mobile_phone_locale "
        else:
            sql = "select mobile,sheng,shi from mobile_area_mapping "
        # print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def result_to_txt(self, city_name, out_path="data/"):
        result_model_list = self.get_result()
        file_name = city_name
        file_path = out_path + file_name + "dict"
        file_out = open(file_path, "a")
        for result_model in result_model_list:
            # print(result_model)
            file_out.write(result_model.toString() + "\n")
        pass

    def get_phone_dict(self):
        dict_city = {}
        dict_sheng = {}
        result_model_list = self.get_result()
        for result_model in result_model_list:
            phone = str(result_model.phone)
            sheng = result_model.sheng
            shi = result_model.shi
            dict_city[phone] = shi
            dict_sheng[phone] = sheng
        return dict_city, dict_sheng

class CodeDictDao(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =model.ThreeCodeDict):
        self.db = DBClass("local")
        self.ModelClass =ModelClass

    def get_result(self):

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        sql = "select threecode,cityname from airport_info "
        print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)

        return result_model_list

    def result_to_txt(self, city_name, out_path="data/"):
        result_model_list = self.get_result()
        file_name = city_name
        file_path = out_path + file_name + "dict"
        file_out = open(file_path, "a")
        for result_model in result_model_list:
            # print(result_model)
            file_out.write(result_model.toString() + "\n")
        pass

    def get_code_dict(self):
        dict_city = {}
        result_model_list = self.get_result()
        for result_model in result_model_list:
            phone = result_model.code
            city = result_model.name
            dict_city[phone] = city
        return dict_city



# def testOrderPhone():
#
#     o_Phone = OrderPhoneDao()
#     # phone_numbers = o_Phone.get_phonenumbers()
#     # for phone_number in phone_numbers:
#     #     print(phone_number)
#     o_Phone.result_to_txt()

def testOrderPhoneDao():
    o_OrderPhoneDao = OrderPhoneDao()
    users_result = o_OrderPhoneDao.get_user_identity()
    for user in users_result:
        print user
    # print([user for user in users_result])


def testPhoneDictDao():
    o_PhoneDict = PhoneDictDao()
    dict_city, dict_sheng = o_PhoneDict.get_phone_dict()
    print(dict_city)
    pass

if __name__ == "__main__":
    # testOrderPhone()
    # phoneDictTest()
    # testPhoneDictDao()
    # testOrderPhoneDao()
    testPhoneDictDao()

    pass