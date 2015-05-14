#ecoding=utf-8
__author__ = 'Administrator'

from source_hbgj_mysql import *
from model import PhoneNumber
from model import SourcePhone

class BaseUserMysqlDao(Mysql):
    def __init__(self,dbtype_dao='local'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        model_object = model_class()
        if not result:
            return False
        for row in result:
            model_object = model_class()
            model_object.set0(row[0])
            model_object.set1(row[1])
            model_object.set2(row[2])
            model_object.set3(row[1]-row[2])
            users_model_list.append(model_object)
        return users_model_list

    def query_result_by_setValue(self, sql, model_class):
        result=self.get_all(sql)
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

class Phone(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =SourcePhone):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass

    def get_phonenumbers(self):

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        sql = "select phone,phoneid from phone_user "
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def result_to_txt(self,out_path="data/"):
        result_model_list = self.get_phonenumbers()
        file_name = "phone_result0422"
        file_path = out_path + file_name
        file_out = open(file_path,"a")
        for result_model in result_model_list:
            # print(result_model)
            file_out.write(result_model.toString() + "\n")
        pass


class PhoneDict(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =PhoneNumber):
        self.db = DBClass("local")
        self.ModelClass =ModelClass

    def get_phoneDict(self, city_name):

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        sql = "select mobile from mobile_area_mapping where shi like '%s%%' " % city_name
        print(sql)
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)

        return result_model_list

    def result_to_txt(self, city_name, out_path="data/"):
        result_model_list = self.get_phoneDict(city_name)
        file_name = city_name
        file_path = out_path + file_name + "dict"
        file_out = open(file_path, "a")
        for result_model in result_model_list:
            # print(result_model)
            file_out.write(result_model.toString() + "\n")
        pass
def phoneTest():

    o_Phone = Phone()
    # phone_numbers = o_Phone.get_phonenumbers()
    # for phone_number in phone_numbers:
    #     print(phone_number)
    o_Phone.result_to_txt()

    pass

def phoneDictTest():
    o_phone = PhoneDict()
    result = o_phone.get_phoneDict("上海")
    for phone in result:
        print(phone)

if __name__ == "__main__":
    phoneTest()
    # phoneDictTest()
    pass