__author__ = 'Administrator'
from db.source_hbgj_mysql import Mysql


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

class ThreeCodeDict():
    def __init__(self):
        self.code = ""
        self.name = ""

    def setValues(self,valueList):
        self.code = valueList[0]
        self.name = valueList[1]

    def toString(self):
        out_Str = self.code + "\t" + self.name
        return out_Str

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

def get_code_dict():
    o_CodeDict = CodeDictDao()
    dict_code = o_CodeDict.get_code_dict()
    return dict_code

if __name__ == "__main__":
    dict_code = get_code_dict()
    print(dict_code)

    pass