__author__ = 'Administrator'

from db.source_hbgj_mysql import *

class PhoneId():
    def __init__(self):
        self.phoneid = ""

    def setValues(self, valueList):
        self.phoneid = str(valueList[0])

class BaseUserMysqlDao(Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def query_result(self, sql, model_class):
        result=self.get_all(sql)
        users_model_list = []
        # model_object = model_class()
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

class NewConsumersFromGtDao(Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def get_consumers(self, s1, s2):
        sql = "SELECT DISTINCT PHONEID " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s' " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')>='%s' " \
                "and p like '%%gtgj%%' "\
                "and PHONEID not in " \
                "(  " \
                "SELECT phoneid " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s') " %(s2, s1, s1)
        print(sql)
        result = self.get_all(sql)

        phone_id_list = []
        if not result:
            return []
        for row in result:
            phone_id_list.append(row[0])
        return phone_id_list


class ConsumersFromGtDao(Mysql):
    def __init__(self, dbtype_dao='hbgj79'):
        Mysql.__init__(self, dbtype=dbtype_dao)

    def get_consumers(self, s1, s2):
        sql = "SELECT DISTINCT PHONEID " \
                "from TICKET_ORDER " \
                "where ORDERSTATUE not in (2,12,21,51,75) " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')<'%s' " \
                "and DATE_FORMAT(createtime,'%%Y%%m%%d')>='%s' " \
                "and p like '%%gtgj%%' " %(s2, s1)
        # print(sql)
        result = self.get_all(sql)

        phone_id_list = []
        if not result:
            return []
        for row in result:
            phone_id_list.append(row[0])
        return phone_id_list

def newconsumers(s1, s2):
    o_object = NewConsumersFromGtDao()
    t = o_object.get_consumers(s1, s2)
    # t = o_object.get_consumers("20150101", "20150401")
    print(s1, len(t))
    pass

def consumers(s1, s2):
    o_object = ConsumersFromGtDao()
    t = o_object.get_consumers(s1, s2)
    # t = o_object.get_consumers("20150101", "20150401")
    print(s1, len(t))

if __name__ == "__main__":
    # newconsumers("20140101","20140401")
    # newconsumers("20140401","20140701")
    # newconsumers("20140701","20141001")
    # newconsumers("20141001","20150101")
    # newconsumers("20150101","20150401")


    consumers("20140101","20140401")
    consumers("20140401","20140701")
    consumers("20140701","20141001")
    consumers("20141001","20150101")
    consumers("20150101","20150401")
    pass

