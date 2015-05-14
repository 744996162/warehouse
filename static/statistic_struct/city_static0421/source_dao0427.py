#ecoding=utf-8
__author__ = 'Administrator'

from source_hbgj_mysql import *
from model import PhoneNumber
from model import SourcePhone
from model import PhoneDict
from model import OrderDetail
from model import ThreeCodeDict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

class OrderPhoneDao(object):
    """


    """
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =OrderDetail):
        self.db = DBClass("hbgj79")
        self.ModelClass =ModelClass



    def get_orderdetail(self,s_day,end_day):

    # """
    #     s_day format("%Y-%m-%d")
    #     end_day format("%Y-%m-%d")
    # """

        sql = "select TICKET_ORDERDETAIL.FLYDATE,TICKET_ORDERDETAIL.DEPCODE, TICKET_ORDERDETAIL.ARRCODE, TICKET_ORDER.CONTACTPHONE,TICKET_ORDER.PHONEID  " \
                "from TICKET_ORDERDETAIL " \
                "join TICKET_ORDER " \
                "on TICKET_ORDERDETAIL.ORDERID = TICKET_ORDER.ORDERID " \
                "where TICKET_ORDER.ORDERSTATUE in(5,52,53) " \
                "AND FLYDATE >= '%s' " \
                "AND FLYDATE <= '%s' " % (s_day, end_day)
        print(sql)

                # "AND FLYDATE = '2015-04-27' "

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        # sql = "select phone,phoneid from phone_user "
        result_model_list = self.db.query_result_by_setValue(sql, self.ModelClass)
        return result_model_list

    def result_to_txt(self, s_day, end_day, file_path=""):
        result_model_list = self.get_orderdetail(s_day, end_day)
        file_path = file_path
        file_out = open(file_path, "a")
        for result_model in result_model_list:
            # print(result_model)
            file_out.write(result_model.toString() + "\n")
        pass


class PhoneDictDao(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =PhoneDict):
        self.db = DBClass("gtgj89")
        self.ModelClass =ModelClass

    def get_result(self):

        # sql = "select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%%91ZS%%' or USER_CHANNEL LIKE '%%appstore%%' or USER_CHANNEL LIKE '%%juwan%%' or USER_CHANNEL LIKE '%%91PGZS%%' or USER_CHANNEL LIKE '%%kuaiyong%%' or USER_CHANNEL LIKE '%%TBT%%' or USER_CHANNEL LIKE '%%PPZS%%' then 1 else 0 end ) ios_activeusers " \
        #        "from HBZJ_USER where USER_LOGINDATE>=to_date(%s , 'yyyymmdd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')" % querydate_str
        sql = "select phone_num,province,city from mobile_phone_locale "
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

    def get_phone_dict(self):
        dict_city = {}
        dict_sheng = {}
        result_model_list = self.get_result()
        for result_model in result_model_list:
            phone = result_model.phone
            sheng = result_model.sheng
            shi = result_model.shi
            dict_city[phone] = shi
            dict_sheng[phone] = sheng

        return dict_city,dict_sheng

class CodeDictDao(object):
    def __init__(self, DBClass = BaseUserMysqlDao, ModelClass =ThreeCodeDict):
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


def testOrderPhone():

    o_Phone = OrderPhoneDao()
    # phone_numbers = o_Phone.get_phonenumbers()
    # for phone_number in phone_numbers:
    #     print(phone_number)
    o_Phone.result_to_txt()

    pass
def testPhoneDictDao():
    o_PhoneDict = PhoneDictDao()
    dict_city,dict_sheng = o_PhoneDict.get_phone_dict()
    print(dict_city)
    pass

if __name__ == "__main__":
    # testOrderPhone()
    # phoneDictTest()
    testPhoneDictDao()
    pass